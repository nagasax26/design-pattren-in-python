import time
from abc import ABCMeta, abstractmethod
from datetime import datetime


class ISwitch(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def execute():
        pass


class SwitchOffCommand(ISwitch):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class SwitchOnCommand(ISwitch):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class Light:
    "The Receiver"

    @staticmethod
    def turn_on():
        print('Light turned ON')

    @staticmethod
    def turn_off():
        print('Light turned OFF')


class Switch:
    "The Invoker"

    def __init__(self):
        self.commands = {}
        self.history = []

    def show_history(self):
        for h in self.history:
            print(
                f"{datetime.fromtimestamp(h[0]).strftime('%H:%M:%S')}",
                f" : {h[1]}"
            )

    def register(self, command_name, command):
        self.commands[command_name] = command

    def execute(self, command_name):
        if command_name in self.commands.keys():
            self.commands[command_name].execute()
            self.history.append((time.time(), command_name))
        else:
            print(f'command {command_name} is not recognized')

    def replay_last_of(self, number_to_replay):
        commands = self.history[-number_to_replay:]
        for command in commands:
            self.commands[command[1]].execute()


light = Light()

switch_on = SwitchOnCommand(light)
switch_off = SwitchOffCommand(light)

switch = Switch()

switch.register('on', switch_on)
switch.register('off', switch_off)

switch.execute('on')
switch.execute('off')
switch.execute('on')
switch.execute('on')
switch.execute('off')

switch.show_history()
switch.replay_last_of(2)
