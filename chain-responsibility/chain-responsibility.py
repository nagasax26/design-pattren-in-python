from abc import ABCMeta, abstractmethod


class IDispenser(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def next_successor(successor):
        pass

    @staticmethod
    @abstractmethod
    def handle(amount):
        pass


class Dispenser1(IDispenser):
    def __init__(self):
        self.successor = None

    def next_successor(self, successor):
        self.successor = successor

    def handle(self, amount):
        print(f'Dispense {amount} of 1$')


class Dispenser10(IDispenser):
    def __init__(self):
        self.successor = None

    def next_successor(self, successor):
        self.successor = successor

    def handle(self, amount):
        if amount >= 10:
            total = amount // 10
            reminder = amount % 10
            print(f'Dispense {total} of 10$')
            if reminder != 0:
                self.successor.handle(reminder)
        else:
            self.successor.handle(amount)


class Dispenser20(IDispenser):
    def __init__(self):
        self.successor = None

    def next_successor(self, successor):
        self.successor = successor

    def handle(self, amount):
        if amount >= 20:
            total = amount // 20
            reminder = amount % 20
            print(f'Dispense {total} of 20$')
            if reminder != 0:
                self.successor.handle(reminder)
        else:
            self.successor.handle(amount)


class Dispenser50(IDispenser):
    def __init__(self):
        self.successor = None

    def next_successor(self, successor):
        self.successor = successor

    def handle(self, amount):
        if amount >= 50:
            total = amount // 50
            reminder = amount % 50
            print(f'Dispense {total} of 50$')
            if reminder != 0:
                self.successor.handle(reminder)
        else:
            self.successor.handle(amount)


class ATMDispenser:
    def __init__(self):
        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()
        self.chain4 = Dispenser1()

        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)
        self.chain3.next_successor(self.chain4)

    def start(self, amount):
        self.chain1.handle(amount)


atm = ATMDispenser()
atm.start(345)