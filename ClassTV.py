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
    # turn tv on
    def turn_on(self):
        self.on_off = "on"
        return "TV is turned on."

    # turn tv off
    def turn_off(self):
        self.on_off = "off"
        return "TV is turned off."

    # get tv channel
    def get_channel(self):
        print(f"{self.name}'s channel is {self.channel}.")

    # set/change tv channel
    def set_channel(self):
        ask_channel = input("Would you like to change the channel? ")
        if ask_channel == "yes":
            new_channel = input("Which channel do you like? (1-120) ")
            self.channel = new_channel
        elif ask_channel == "no":
            print("Thank you.")

    # get volume level of tv
    def get_volume(self):
        print(f"{self.name}'s volume level is {self.volume_level}.")

    # set/change volume level of tv
    def set_volume(self):
        ask_volume = input("Would you like to change the volume level? ")
        if ask_volume == "yes":
            new_volume = input("Which volume level do you like? (1-7) ")
            self.volume_level = new_volume
        elif ask_volume == "no":
            print("Thank you.")

    # change to next channel
    def channel_up(self):
        self.channel = self.channel + 1
        return self.channel

    # change to previous channel
    def channel_down(self):
        self.channel = self.channel - 1
        return self.channel

    # increase volume level
    def volume_up(self):
        self.volume_level = self.volume_level + 1
        return self.channel

    # decrease volume_level
    def volume_down(self):
        self.volume_level = self.volume_level - 1
        return self.channel

    # print details
    def print_details(self):
        print(f"{self.name}'s channel is {self.channel} and volume level is {self.volume_level}.")
