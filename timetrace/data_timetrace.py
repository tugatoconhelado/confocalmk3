import numpy as np
import dataclasses
from PySide2.QtCore import QObject, Signal, Property


class SignalWrapper(QObject):

    dataChanged = Signal(object)

    def __init__(self):
        super().__init__()


class ExperimentVariable:

    def __init__(self, wrapper):
        self.wrapper = wrapper

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, "_" + self.name)

    def __set__(self, obj, value):
        setattr(obj, "_" + self.name, value)
        self.wrapper.dataChanged.emit(obj)


@dataclasses.dataclass
class TimeTraceParameterData:

    wrapper = SignalWrapper()
    sampling_frequency: int = ExperimentVariable(wrapper)
    refresh_time: float = ExperimentVariable(wrapper)
    window_time: float = ExperimentVariable(wrapper)


@dataclasses.dataclass
class TimeTraceData(QObject):

    wrapper = SignalWrapper()
    parameters: TimeTraceParameterData = ExperimentVariable(wrapper)
    counts: np.ndarray = ExperimentVariable(wrapper)
    time_array: np.ndarray = ExperimentVariable(wrapper)

    def __post_init__(self):

        super().__init__()


if __name__ == '__main__':

    def handle_parameter_changed(obj):

        print(obj)

    def handle_data_changed(obj):
        print(obj)

    pdata = TimeTraceParameterData(1000, 0.1, 5)
    ttdata = TimeTraceData(pdata, np.array([]), np.array([]))
    pdata.wrapper.dataChanged.connect(handle_parameter_changed)
    ttdata.wrapper.dataChanged.connect(handle_data_changed)

    ttdata.counts = np.array([1,2,3])
    print(pdata.sampling_frequency * pdata.window_time, type(pdata.sampling_frequency))