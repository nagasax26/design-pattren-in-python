from abc import ABCMeta, abstractmethod


class IObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        pass

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        pass

    @staticmethod
    @abstractmethod
    def notify():
        pass


class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(count):
        pass


class Observer(IObserver):

    def notify(self, count):
        print(f'Count has changed: {count}')


class Observable(IObservable):
    def __init__(self):
        self.observers = []
        self.count = 0

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.notify(self.count)

    def set_count(self, count):
        self.count = count
        self.notify()


observable1 = Observable()
observable2 = Observable()

observer = Observer()
observable1.subscribe(observer)
observable2.subscribe(observer)

observable1.set_count(12)
observable1.set_count(52)

observable1.unsubscribe(observer)

observable1.set_count(42)

observable2.set_count(90)
