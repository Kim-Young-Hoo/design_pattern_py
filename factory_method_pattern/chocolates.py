from abc import ABCMeta, abstractmethod


class Chocolate(metaclass=ABCMeta):

    def __init__(self, sweetness):
        self.sweetness = sweetness

    @abstractmethod
    def get_name(self):
        pass


class WhiteChocolate(Chocolate):

    def __init__(self, sweetness):
        super().__init__(sweetness)

    def get_name(self):
        return "White Chocolate : {sweetness}%".format(sweetness=self.sweetness)


class DarkChocolate(Chocolate):

    def __init__(self, sweetness):
        super().__init__(sweetness)

    def get_name(self):
        return "Dark Chocolate : {sweetness}%".format(sweetness=self.sweetness)
