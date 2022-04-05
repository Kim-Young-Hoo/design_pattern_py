from abc import ABCMeta, abstractmethod


class Display(metaclass=ABCMeta):

    @abstractmethod
    def display(self):
        pass


class SimpleDisplay(Display):
    def display(self):
        print("display!!!!")


class ImageDisplay(Display):

    def display(self):
        print("I M A G E")


class VideoDisplay(Display):
    def display(self):
        print("V I D E O")
