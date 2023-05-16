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
        volume_level = int(input("Choose volume level from 1-7: "))

        # create objects for class TV
        tv = TV(name, channel, volume_level)

        # call methods
        tv.print_details()

        # ask user for more input
        more_input = input("Would you like to try again? ")
        print("\n")
        if more_input == "yes":
            continue
        elif more_input == "no":
            break

        def func_list():  # create a function to print list of class TV functions
            method_list = input("Would you like to see other available tv functions? ").lower()
            if method_list == "yes":
                for func in dir(TV):
                    if func.startswith('__'):
                        continue
                    else:
                        print(func)
            elif method_list == "no":
                print("Thank you!")
                exit()

except ValueError:
    print("Invalid input. Please try again.")