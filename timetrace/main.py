import sys
import time
import numpy as np
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
import pyqtgraph as pg
from PySide2.QtCore import Qt, QThread, Signal, Slot
import nidaqmx
from ui_timetrace import Ui_timetrace


class DAQReader(QThread):
    data_updated = Signal(np.ndarray, np.ndarray)

    def __init__(self, task_name, sampleFreq, refreshTime, samples, windowTime, sizeArray, timeOut):
        super().__init__()
        self.task_name = task_name
        self.sampleFreq = sampleFreq
        self.refreshTime = refreshTime
        self.samples = samples
        self.windowTime = windowTime
        self.sizeArray = sizeArray
        self.timeOut = timeOut
        self.running = False
        self.tasks = []


    def DigPulseTrainCount(self, frequency, duty_cycle, samples):

        task = nidaqmx.task.Task()
        status = task.co_channels.add_co_pulse_chan_freq(
            counter='Dev1/ctr1',
            name_to_assign_to_channel=u'',
            units=nidaqmx.constants.FrequencyUnits.HZ,
            idle_state=nidaqmx.constants.Level.LOW,
            initial_delay=0.0,
            freq=frequency,
            duty_cycle=duty_cycle
        )
        status = task.timing.cfg_implicit_timing(
            sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS,
            samps_per_chan=samples
        )
        self.tasks.append(task)
        return status

    def run(self):
        self.running = True
        dev = 'Dev1'
        if self.running:
            status = self.DigPulseTrainCount(self.sampleFreq, 0.5, self.samples * self.windowTime)
            print(f'NI: Set Pulse : {status}')
        read_task = nidaqmx.Task()
        self.tasks.append(read_task)

        try:
            # Adds voltage channel
            #read_task.ai_channels.add_ai_voltage_chan(
            #    physical_channel=dev + '/ai2',
            #    name_to_assign_to_channel="",
            #    terminal_config=nidaqmx.constants.TerminalConfiguration.DIFF,
            #    min_val=-10,
            #    max_val=10
            #)

            # Adds counter input channel (counter 0)
            read_task.ci_channels.add_ci_count_edges_chan(
                counter=dev + '/ctr0',
                name_to_assign_to_channel='',
                edge=nidaqmx.constants.Edge.RISING,
                initial_count=0,
                count_direction=nidaqmx.constants.CountDirection.COUNT_UP
            )
            # Configures the sampling clock
            status = read_task.timing.cfg_samp_clk_timing(
                rate=self.sampleFreq,
                source='/Dev1/PFI13',
                active_edge=nidaqmx.constants.Edge.RISING,
                sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS,
                samps_per_chan=self.sizeArray
            )
            print(f'NI Configure the clock : {status}')

            t = np.arange(0, self.samples) / self.samples * self.windowTime - self.windowTime
            data = np.zeros(self.samples)
            read_task.start()
            print(f'Samples = {self.samples}')
            # The Size array is the number of samples per second times the size of the window I want to acquire
            print(f'SizeArray = {self.sizeArray}')
            counts_array = np.array([])
            counts = 0

            while self.running:
                # So whats happening here is that we set the sampling clock to take 1000 samples per second (sampling
                # frequency) and we telling the task to read 100 samples, i.e. the time that the card will acquire those
                # data is 0.1 seconds, the refresh time.

                read_data = read_task.read(
                    number_of_samples_per_channel=self.samples,
                    timeout=self.timeOut
                )
                read_data = np.array(read_data)
                read_data = np.diff(read_data)
                mean_data = np.mean(read_data) * self.sampleFreq

                data[0] = mean_data
                data = np.roll(data, -1)
                t += self.refreshTime

                self.data_updated.emit(t, data)
        finally:
            for task in self.tasks:
                task.stop()


    def stop(self):
        self.running = False


class MainWindow(QWidget, Ui_timetrace):
    def __init__(self, daq_reader):
        super().__init__()

        self.setupUi(self)

        self.daq_reader = daq_reader
        self.daq_reader.data_updated.connect(self.update_plot)

        self.run_cps_button.clicked.connect(self.start_daq_reader)
        self.stop_button.clicked.connect(self.stop_daq_reader)

        self.configure_plots()

    def configure_plots(self):

        self.cps_plot.setLabel('left', 'Intensity (counts per second')
        self.cps_plot.setLabel('bottom', 'Time (sec)')
        self.cps_plot.setLimits(xMin=0)

        self.cps_dataline = self.cps_plot.plot([], [], pen='yellow')

    def start_daq_reader(self):
        self.daq_reader.start()

    def stop_daq_reader(self):
        self.daq_reader.stop()
        self.daq_reader.quit()

    @Slot(np.ndarray, np.ndarray)
    def update_plot(self, time, data):

        self.time = time
        self.data = data

        self.cps_dataline.setData(self.time, self.data, clear=True, pen='b')

        self.cps_label.setText(str(round(self.data[-1])))

    def closeEvent(self, event):
        self.stop_daq_reader()
        super().closeEvent(event)


if __name__ == '__main__':
    task_name = "Dev1/ai0"

    sampleFreq = 1000 # Number of samples per second
    refreshTime = 0.1 # Time to acquire samples (time to iterate)
    samples = int(sampleFreq * refreshTime) # Number of samples each iteration
    windowTime = 10 # Size of the window in seconds
    sizeArray = int(windowTime * sampleFreq) # Number of samples in the window
    timeOut = refreshTime * 1.2 # Time to raise an error for NI
    reader = DAQReader(task_name, sampleFreq, refreshTime, samples, windowTime, sizeArray, timeOut)

    app = QApplication(sys.argv)
    main_window = MainWindow(reader)
    main_window.show()
    sys.exit(app.exec_())
