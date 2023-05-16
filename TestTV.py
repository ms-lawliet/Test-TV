# Create a Python Code for creating the Class named TV and a Test Driver program named TestTV
# that will create two objects from Class TV and will produce the following output:
# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

from ClassTV import TV    # import class TV from ClassTV.py file

try:
    # ask for user input
    name = input("Enter name of tv: ")
    channel = int(input("Choose channel from 1-30: "))
    volume_level = int(input("Choose volume level from 0-7: "))
    on_off = input("Would you like to turn on your tv? (on or off) ")

    # create objects
    tv1 = TV(name, channel, volume_level, on_off)
    tv2 = TV(name, channel, volume_level, on_off)

    # call methods
    tv1.get_channel()
    tv1.print_details()

except ValueError:
    print("Invalid input. Please try again.")
