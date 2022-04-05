from abc import ABCMeta, abstractmethod


class Quack(metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass


class SimpleQuack(Quack):

    def quack(self):
        print("quack!!!!")


class LoudQuack(Quack):

    def quack(self):
        print("Fucking Loud!!!!!!!!")


class QuietQuack(Quack):

    def quack(self):
        print("quiet")
