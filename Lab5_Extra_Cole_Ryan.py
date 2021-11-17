def display_title():
    print("Feet and Meters Converter")

def display_menu():
    print("")
    print("Conversion Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

def to_meters(feet):
    meters = feet * 0.3048
    return meters

def to_feet(meters):
    feet = meters / 0.3048
    return feet

display_title()
again = "y"
while again == "y":
    display_menu()
    choice = input("Select a conversion (a/b):")
    print("")
    choice = choice.lower()
    if choice == "a":
        feet = int(input("Enter feet:"))
        meters = to_meters(feet)
        print(round(meters, 2), "meters")
    elif choice == "b":
        meters = int(input("Enter meters:"))
        feet = to_feet(meters)
        print(round(feet, 2), "feet")
    else:
        print("invalid entry")
    print("")
    again = input("Would you like to perform another conversion? (y/n):")
    again = again.lower()
print("")
print("Thanks, bye!")
