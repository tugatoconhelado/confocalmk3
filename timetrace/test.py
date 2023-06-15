from PySide2.QtCore import QObject, Signal
from dataclasses import dataclass, asdict


class SignalWrapper(QObject):
    valueChanged = Signal(object)

    def __init__(self):

        super().__init__()


class SignalDescriptor:
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
        self.wrapper.valueChanged.emit(obj)


@dataclass
class MyObject:

    wrapper = SignalWrapper()

    value1: int = SignalDescriptor(wrapper)
    value2: int = SignalDescriptor(wrapper)
    value3: int = SignalDescriptor(wrapper)


def handle_value_changed(obj):
    print("Value changed: value1={}, value2={}, value3={}".format(obj.value1, obj.value2, obj.value3))

my_obj = MyObject(value1=10, value2=20, value3=30)
my_obj.wrapper.valueChanged.connect(handle_value_changed)
my_obj.value1 = 100
my_obj.value2 = 200
my_obj.value3 = 1
print(my_obj.__init__)
