from abc import ABCMeta, abstractmethod
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from observer import Observer




class Observable(metaclass=ABCMeta):

    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def get_temperature(self):
        pass

    @abstractmethod
    def change_temperature(self):
        pass


class WeatherStation(Observable):

    def __init__(self):
        self.observers = []
        self.temperature = 30

    def add(self, observer: 'Observer'):
        self.observers.append(observer)

    def remove(self, observer: 'Observer'):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def get_temperature(self):
        return self.temperature

    def change_temperature(self):
        self.temperature += random.randint(-5, 5)
