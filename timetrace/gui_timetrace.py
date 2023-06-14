import sys
import numpy as np
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtCore import Qt, QThread, Signal, Slot
from ui_timetrace import Ui_timetrace

class MainWindow(QWidget, Ui_timetrace):


    def __init__(self, daq_reader = None):
        super().__init__()

        self.daq_reader = daq_reader
        #self.daq_reader.data_updated.connect(self.update_plot)

        self.init_gui()



    def init_gui(self):

        self.setupUi(self)
        self.configure_plots()


        #validator =


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

    app = QApplication()
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
