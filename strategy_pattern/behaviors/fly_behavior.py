from abc import ABCMeta, abstractmethod


class Fly(metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass


class SimpleFly(Fly):
    def fly(self):
        print("fly!!!!")


class RoundFly(Fly):

    def fly(self):
        print("fly round round round!")


class UpDownFly(Fly):
    def fly(self):
        print("fly up and down!")
