from abc import ABCMeta, abstractmethod
from math import cos


class ICommand(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def execute(self, num):
        pass

    @staticmethod
    @abstractmethod
    def undo(self, num):
        pass


class AddNumber(ICommand):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, num):
        self.calculator.add(num)

    def undo(self, num):
        self.calculator.subtract(num)


class SubtractNumber(ICommand):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self, num):
        self.calculator.subtract(num)

    def undo(self, num):
        self.calculator.add(num)


class Operation:
    def __init__(self):
        self.commands = {}
        self.history = []
        self.undo_history = []

    def register(self, command_name, command):
        self.commands[command_name] = command

    def execute(self, command_name, num):
        if command_name in self.commands.keys():
            self.commands[command_name].execute(num)
            self.history.append((command_name, num))
        else:
            print(f'command {command_name} is not found')

    def undo(self):
        if not len(self.history):
            print('NO COMMANDS')
        else:
            command = self.history.pop(-1)
            self.commands[command[0]].undo(command[1])
            self.undo_history.append((command[0], command[1]))

    def redo(self):
        if not len(self.undo_history):
            print('NO COMMANDS')
        else:
            command = self.undo_history.pop(-1)
            self.commands[command[0]].execute(command[1])
            self.history.append((command[0], command[1]))

    def show_history(self):
        for op in self.history:
            print(f'{op[0]} {op[1]}')

    def repeat_last(self, number):
        histories = self.history[-number:]
        for h in histories:
            self.execute(h[0], h[1])


class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result = self.result + num

    def subtract(self, num):
        self.result = self.result - num


calculator = Calculator()

add_number = AddNumber(calculator)
subtract_number = SubtractNumber(calculator)

operation = Operation()

operation.register('add', add_number)
operation.register('sub', subtract_number)

operation.execute('add', 10)
operation.execute('sub', 4)
operation.execute('add', 8)

operation.show_history()
print(f'RESULT = {calculator.result}')

operation.undo()
operation.undo()
operation.undo()
operation.undo()

operation.show_history()
print(f'RESULT = {calculator.result}')


operation.redo()
operation.redo()
operation.redo()

operation.show_history()
print(f'RESULT = {calculator.result}')
