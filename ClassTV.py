# this is the separate file for the class

from colorama import Fore, Back, Style


class TV:   # create class
    def __init__(self, name, channel, volume_level):   # create class instances
        self.name = name
        self.channel = channel
        self.volume_level = volume_level

# create required methods
    # turn tv on
    def turn_on(self):
        return "TV is turned on."

    # turn tv off
    def turn_off(self):
        return "TV is turned off."

    # get tv channel
    def get_channel(self):
        print(Fore.BLUE + f"{self.name}'s channel is {self.channel}.")

    # set/change tv channel
    def set_channel(self):
        ask_channel = input(Fore.CYAN + "Would you like to change the channel? ").lower()
        if ask_channel == "yes":
            new_channel = input("Which channel do you like? (1-120) ")
            self.channel = new_channel
        elif ask_channel == "no":
            print("Thank you.")
        else:
            raise Exception("Yes or no only.")

    # get volume level of tv
    def get_volume(self):
        print(Fore.BLUE + f"{self.name}'s volume level is {self.volume_level}.")

    # set/change volume level of tv
    def set_volume(self):
        ask_volume = input(Fore.CYAN + "Would you like to change the volume level? ").lower()
        if ask_volume == "yes":
            new_volume = input("Which volume level do you like? (1-7) ")
            self.volume_level = new_volume
        elif ask_volume == "no":
            pass
        else:
            raise Exception("Yes or no only.")

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
        print(Fore.BLUE + f"{self.name}'s channel is {self.channel} and volume level is {self.volume_level}.")

    # print list of class TV functions
    def func_list(self):
        method_list = input(Fore.RESET + "Would you like to see other available tv functions? ").lower()
        if method_list == "yes":
            print(Fore.YELLOW + "List of available tv functions:")
            for func in dir(TV):
                if func.startswith('__'):
                    continue
                else:
                    print(Fore.GREEN + func)
        elif method_list == "no":
            print("Thank you!")
            exit()
        else:
            raise Exception("Yes or no only.")

