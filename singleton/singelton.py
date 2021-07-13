class Product:
    def __init__(self):
        self.items = []

    def add(self, name):
        self.items.append(name)


class Singleton:
    product = Product()

    def __new__(cls, *args, **kwargs):
        return cls

    @classmethod
    def add(cls, name):
        cls.product.add(name)


Singleton().add('tesla')
Singleton().add('honda')
Singleton().add('kia')

print(Singleton().product.items)