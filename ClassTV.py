# Create a Python Code for creating the Class named TV and a Test Driver program named TestTV
# that will create two objects from Class TV and will produce the following output:
# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

# create class
class TV:
    def __init__(self, name, channel, volume_level, on_off):   # create class instances
        self.name = name
        self.channel = channel
        self.volume_level = volume_level
        self.on_off = on_off

# create required methods
    def turn_on(self):
        self.on_off = "on"
        return "TV is turned on."

    def turn_off(self):
        self.on_off = "off"
        return "TV is turned off."

    def get_channel(self):
        print(f"{self.name}'s channel is {self.channel}.")

    def set_channel(self, new_channel):
        self.channel = new_channel

    def get_volume(self):
        print(f"{self.name}'s volume level is {self.volume_level}.")

    def set_volume(self, new_volume):
        self.volume_level = new_volume

    def channel_up(self):
        self.channel = self.channel + 1
        return self.channel

    def channel_down(self):
        self.channel = self.channel - 1
        return self.channel

    def volume_up(self):
        self.volume_level = self.volume_level + 1
        return self.channel

    def volume_down(self):
        self.volume_level = self.volume_level - 1
        return self.channel

    def print_details(self):
        print(f"{self.name}'s channel is {self.channel} and volume level is {self.volume_level}.")
