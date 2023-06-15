import numpy as np
import nidaqmx
from PySide2.QtCore import QThread, Signal


class DAQReader(QThread):

    data_updated = Signal(np.ndarray, np.ndarray)

    def __init__(self, sample_frequency, refresh_time, samples, window_time, size_array, time_out):

        super().__init__()
        self.sampleFreq = sample_frequency
        self.refreshTime = refresh_time
        self.samples = samples
        self.windowTime = window_time
        self.sizeArray = size_array
        self.timeOut = time_out
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
            read_task.ai_channels.add_ai_voltage_chan(
                physical_channel=dev + '/ai2',
                name_to_assign_to_channel="",
                terminal_config=nidaqmx.constants.TerminalConfiguration.DIFF,
                min_val=-10,
                max_val=10
            )

            # Adds counter input channel (counter 0)
            #read_task.ci_channels.add_ci_count_edges_chan(
            #    counter=dev + '/ctr0',
            #    name_to_assign_to_channel='',
            #    edge=nidaqmx.constants.Edge.RISING,
            #    initial_count=0,
            #    count_direction=nidaqmx.constants.CountDirection.COUNT_UP
            #)
            # Configures the sampling clock
            status = read_task.timing.cfg_samp_clk_timing(
                rate=self.sampleFreq,
                source=u'', #'/Dev1/PFI13',
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

