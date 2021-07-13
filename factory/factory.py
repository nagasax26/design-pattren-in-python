from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def __str__(self):
        """Must implement"""

    @staticmethod
    @abstractmethod
    def create_object():
        """Create an Object"""


class BigChair(IChair):

    def __str__(self):
        return f'The Chair has a Width of {self.width} and depth {self.depth} and height of {self.height}'

    def __init__(self):
        self.width = 80
        self.depth = 86
        self.height = 60

    def create_object(self):
        return self


class SmallChair(IChair):

    def __str__(self):
        return f'The Chair has a Width of {self.width} and depth {self.depth} and height of {self.height}'

    def __init__(self):
        self.width = 30
        self.depth = 36
        self.height = 30

    def create_object(self):
        return self


class ChairFactory:
    @staticmethod
    def get_chair(name):
        if name == 'big_chair':
            return BigChair()
        if name == 'small_chair':
            return SmallChair()
        return None


chair_factory = ChairFactory.get_chair('big_chair')
print(chair_factory)
chair_factory = ChairFactory.get_chair('small_chair')
print(chair_factory)