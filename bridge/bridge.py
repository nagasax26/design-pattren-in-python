from abc import ABCMeta, abstractmethod


class IShape(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def draw():
        pass


class Square(IShape):
    def __init__(self, implementer):
        self.implementer = implementer

    def draw(self):
        self.implementer.draw_implementation()


class Circle(IShape):
    def __init__(self, implementer):
        self.implementer = implementer

    def draw(self):
        self.implementer.draw_implementation()


class IShapeImplementer(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def draw_implementation():
        pass


class SquareImplementer(IShapeImplementer):
    @staticmethod
    def draw_implementation():
        print("********")
        print("*      *")
        print("*      *")
        print("*      *")
        print("*      *")
        print("********")


class CircleImplementer(IShapeImplementer):
    @staticmethod
    def draw_implementation():
        print("  *****  ")
        print("*       *")
        print(" *     * ")
        print("  *****  ")


circle = Circle(CircleImplementer)
square = Square(SquareImplementer)

circle.draw()
square.draw()