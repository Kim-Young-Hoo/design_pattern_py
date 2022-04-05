from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from observable import Observable


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def display(self):
        pass


class PhoneDisplay(Observer):

    def __init__(self, display_name, observable: 'Observable'):
        self.temperature = None
        self.display_name = display_name
        self.observable = observable

    def update(self):
        self.temperature = self.observable.get_temperature()

    def display(self):
        print("{display_name}: {temperature} celsius".format(display_name=self.display_name, temperature=self.temperature))


class ComputerDisplay(Observer):

    def __init__(self, display_name, observable: 'Observable'):
        self.temperature = None
        self.display_name = display_name
        self.observable = observable

    def update(self):
        self.temperature = self.observable.get_temperature()

    def display(self):
        print("{display_name}: {temperature} celsius".format(display_name=self.display_name, temperature=self.temperature))
