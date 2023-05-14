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
        return

    def turn_off(self):
        return

    def get_channel(self):
        print(f"{self.name}'s channel is {self.channel}.")
        
# create objects
# call methods
