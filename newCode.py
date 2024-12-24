from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver
class Light:
    def turn_on(self):
        print("The light is ON")

    def turn_off(self):
        print("The light is OFF")

# Concrete Command for turning on the light
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

# Concrete Command for turning off the light
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command_history = []

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()
        self.command_history.append(self.command)

    def press_undo(self):
        if self.command_history:
            last_command = self.command_history.pop()
            last_command.undo()

# Client Code
if __name__ == "__main__":
    # Receiver
    light = Light()

    # Concrete Commands
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Invoker
    remote = RemoteControl()

    # Turning the light on
    remote.set_command(light_on)
    remote.press_button()  # Output: The light is ON

    # Turning the light off
    remote.set_command(light_off)
    remote.press_button()  # Output: The light is OFF

    # Undo the last command
    remote.press_undo()  # Output: The light is ON
