from abc import ABCMeta, abstractmethod
from copy import deepcopy


class IPrototype(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def clone():
        pass


class MyClass(IPrototype):
    def __init__(self, field):
        self.field = field

    def clone(self, mode):
        if mode == 1:
            # a shallow copy
            field = self.field
        if mode == 2:
            # a shallow copy level 2
            field = self.field.copy()
        if mode == 3:
            field = deepcopy(self.field)
        return type(self)(field)

    def __str__(self):
        return f'id={id(self)}\tfield={self.field}\tidField={id(self.field)}\ttypeField={type(self.field)}'


a = MyClass(['name', ['lol', 'hello'], ['test']])

b = a.clone(1)

b.field[0] = 'my car'

print(a)
print(b,"\n")

b = a.clone(2)

b.field[1] = ['arick']

print(a)
print(b, "\n")

b = a.clone(2)

b.field[1][0] = 'arick'

print(a)
print(b, "\n")

b = a.clone(3)

b.field[1][0] = 'what'

print(a)
print(b, "\n")