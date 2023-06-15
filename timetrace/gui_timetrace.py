import sys
import numpy as np
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtCore import Qt, QThread, Signal, Slot
from PySide2.QtGui import QDoubleValidator, QIntValidator
from ui_timetrace import Ui_timetrace
from logic_timetrace import DAQReader


class MainWindow(QWidget, Ui_timetrace):

    parameter_signal = Signal(int)

    def __init__(self, daq_reader = None):

        super().__init__()

        self.daq_reader = daq_reader
        self.daq_reader.data_updated.connect(self.update_plot)
        self.init_gui()
        self.parameter_signal.emit(10)

    def init_gui(self):

        self.setupUi(self)
        self.configure_plots()

        # Set the input validators
        float_validator = QDoubleValidator()
        int_validator = QIntValidator()
        self.refresh_time_edit.setValidator(float_validator)
        self.window_time_edit.setValidator(float_validator)
        self.samp_freq_edit.setValidator(int_validator)

        # Connect button press events
        self.run_cps_button.clicked.connect(self.start_daq_reader)
        self.stop_button.clicked.connect(self.stop_daq_reader)

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

        self.cps_dataline.setData(self.time, self.data, clear=True)

        self.cps_label.setText(str(round(self.data[-1])))

    def closeEvent(self, event):
        self.stop_daq_reader()
        super().closeEvent(event)


if __name__ == '__main__':

    sampleFreq = 1000 # Number of samples per second
    refreshTime = 0.1 # Time to acquire samples (time to iterate)
    samples = int(sampleFreq * refreshTime) # Number of samples each iteration
    windowTime = 10 # Size of the window in seconds
    sizeArray = int(windowTime * sampleFreq) # Number of samples in the window
    timeOut = refreshTime * 1.2 # Time to raise an error for NI

    reader = DAQReader(sampleFreq, refreshTime, samples, windowTime, sizeArray, timeOut)

    app = QApplication()
    form = MainWindow(daq_reader=reader)

    form.show()
    sys.exit(app.exec_())
