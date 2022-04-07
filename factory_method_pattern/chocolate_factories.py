from abc import ABCMeta, abstractmethod
from chocolates import DarkChocolate, WhiteChocolate


class ChocolateFactory(metaclass=ABCMeta):

    @abstractmethod
    def produce_chocolate(self, chocolate_type):
        pass


class SweetChocolateFactory(ChocolateFactory):
    # 쪼꼬릿에 설탕을 겁나 넣는 공장

    def __init__(self):
        pass

    def produce_chocolate(self, chocolate_type):
        if chocolate_type == "DarkChocolate":
            return DarkChocolate(sweetness=80).get_name()
        elif chocolate_type == "WhiteChocolate":
            return WhiteChocolate(sweetness=80).get_name()


class BitterChocolateFactory(ChocolateFactory):
    # 쪼꼬릿에 설탕을 별로 안넣는 공장

    def __init__(self):
        pass

    def produce_chocolate(self, chocolate_type):
        if chocolate_type == "DarkChocolate":
            return DarkChocolate(sweetness=30).get_name()
        elif chocolate_type == "WhiteChocolate":
            return WhiteChocolate(sweetness=30).get_name()
