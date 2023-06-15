import sys
import data_timetrace
import gui_timetrace
import logic_timetrace
from PySide2.QtWidgets import QApplication

sampleFreq = 1000  # Number of samples per second
refreshTime = 0.1  # Time to acquire samples (time to iterate)
samples = int(sampleFreq * refreshTime)  # Number of samples each iteration
windowTime = 10  # Size of the window in seconds
sizeArray = int(windowTime * sampleFreq)  # Number of samples in the window
timeOut = refreshTime * 1.2  # Time to raise an error for NI

reader = logic_timetrace.DAQReader(sampleFreq, refreshTime, samples, windowTime, sizeArray, timeOut)

app = QApplication()
form = gui_timetrace.MainWindow(daq_reader=reader)

form.show()
sys.exit(app.exec_())


