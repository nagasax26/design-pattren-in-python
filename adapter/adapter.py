from abc import ABCMeta, abstractmethod


class A:
    def method_a(self):
        print('method a called')


class B:
    def method_b(self):
        print('method b called')


class IAdapter(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_a():
        pass


class BAdapter(IAdapter):
        def method_a(self):
            return B().method_b()


# Without adapter
classes = [A(), B()]
for c in classes:
    if isinstance(c, B):
        c.method_b()
    else:
        c.method_a()


# with adapter
classes = [A(), BAdapter()]

for c in classes:
    c.method_a()