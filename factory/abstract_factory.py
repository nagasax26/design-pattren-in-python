from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_dimensions():
        "Get Chair Dimensions"


class BigChair(IChair):
    def __init__(self):
        self.width = 60
        self.depth = 60
        self.height = 60

    def get_dimensions(self):
        return {
            'width': self.width,
            'depth': self.depth,
            'height': self.height
        }


class MediumChair(IChair):
    def __init__(self):
        self.width = 30
        self.depth = 30
        self.height = 30

    def get_dimensions(self):
        return {
            'width': self.width,
            'depth': self.depth,
            'height': self.height
        }


class SmallChair(IChair):
    def __init__(self):
        self.width = 10
        self.depth = 10
        self.height = 10

    def get_dimensions(self):
        return {
            'width': self.width,
            'depth': self.depth,
            'height': self.height
        }


class ChairFactory:
    @staticmethod
    def get_chair(name):
        if name == 'big_chair':
            return BigChair()
        if name == 'medium_chair':
            return MediumChair()
        if name == 'small_chair':
            return SmallChair()
        return None


class ITable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_dimensions():
        "Get Chair Dimensions"


class BigTable(ITable):
    def __init__(self):
        self.width = 60
        self.depth = 60
        self.height = 60

    def get_dimensions(self):
        return {
            'width': self.width,
            'depth': self.depth,
            'height': self.height
        }


class MediumTable(ITable):
    def __init__(self):
        self.width = 30
        self.depth = 30
        self.height = 30

    def get_dimensions(self):
        return {
            'width': self.width,
            'depth': self.depth,
            'height': self.height
        }


class SmallTable(ITable):
    def __init__(self):
        self.width = 10
        self.depth = 10
        self.height = 10

    def get_dimensions(self):
        return {
            'width': self.width,
            'depth': self.depth,
            'height': self.height
        }


class TableFactory:
    @staticmethod
    def get_table(name):
        if name == 'big_table':
            return BigTable()
        if name == 'medium_table':
            return MediumTable()
        if name == 'small_table':
            return SmallTable()
        return None


class IFurnitureFactory(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_furniture(name):
        """get furniture"""


class FurnitureFactory(IFurnitureFactory):

    @staticmethod
    def get_furniture(name):
        if name in ['small_chair', 'medium_chair', 'big_chair']:
            return ChairFactory.get_chair(name)
        if name in ['small_table', 'medium_table', 'big_table']:
            return TableFactory.get_table(name)


abstract_factory = FurnitureFactory.get_furniture('small_chair')
print(abstract_factory.__class__)

abstract_factory = FurnitureFactory.get_furniture('big_table')
print(abstract_factory.__class__)