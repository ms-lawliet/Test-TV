# This is the main program

# Create a Python Code for creating the Class named TV and a Test Driver program named TestTV
# that will create two objects from Class TV and will produce the following output:
# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

from ClassTV import TV    # import class TV from ClassTV.py file

try:
    # ask for user input
    while True:
        name = input("Enter name of tv: ")
        channel = int(input("Choose channel from 1-120: "))
        if channel < 1 or channel > 120:
            raise Exception("Out of range. Please try again.")

        volume_level = int(input("Choose volume level from 1-7: "))
        if volume_level > 7 or volume_level < 1:
            raise Exception("Out of range. Please try again.")

        # create objects for class TV
        tv = TV(name, channel, volume_level)

        # call methods
        tv.set_channel()
        tv.print_details()

        # ask user for more input
        more_input = input("Would you like to try again? (yes or no) ")
        if more_input == "yes":
            continue
        elif more_input == "no":
            break
        else:
            raise Exception("Yes or no only.")

except ValueError:
    print("Invalid input. Please try again.")