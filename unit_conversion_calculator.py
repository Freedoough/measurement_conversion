import math
import time


print("Unit Conversion\n\n") # Program title
time.sleep(1)


def imperial_convert():
    while True: # Imperial system unit conversion loop
        first_unit = str(input("Unit to convert from?\n (1): Inches\n (2): Feet\n (3): Yards\n (4): Miles\n (5): Switch Conversion\n (6): Exit Conversion\n> "))

        if first_unit == "1": # Inches conversion to other units
            value = float(input("Enter value to convert:"))
            print(f"{value} inches is {value / 12} feet")
            print(f"{value} inches is {value / 36} yards")
            print(f"{value} inches is {value / 63360} miles")

            time.sleep(1)
        elif first_unit == "2": # Feet conversion to other units
            value = float(input("Enter value to convert:"))
            print(f"{value} feet is {value * 12} inches")
            print(f"{value} feet is {value / 3} yards")
            print(f"{value} feet is {value / 5280} miles")

            time.sleep(1)
        elif first_unit == "3": # Yards conversion to other units
            value = float(input("Enter value to convert:"))
            print(f"{value} yards is {value * 36} inches")
            print(f"{value} yards is {value * 3} feet")
            print(f"{value} yards is {value / 1760} miles")

            time.sleep(1)
        elif first_unit == "4": # Miles conversion to other units
            value = float(input("Enter value to convert:"))
            print(f"{value} miles is {value * 63360} inches")
            print(f"{value} miles is {value * 5280} feet")
            print(f"{value} miles is {value * 1760} yards")

            time.sleep(1)
        elif first_unit == "5": # Switch conversion system
            print("Exiting Imperial Conversion")
            return
        elif first_unit == "6": # Exit program
            print("Exiting Conversion")
            break
        else:
            print("INVALID")
            time.sleep(2)
            

def metric_convert():
    while True:
        first_unit =  str(input("Unit to convert from?\n (1): Milimeters\n (2): Centimeters\n (3): Meters\n (4): Kilometers\n (5): Switch Conversion\n (6): Exit Conversion\n>"))
        value = float(input("Enter value to convert: "))
        if first_unit == "1":
            print(f"{value}mm is {value / 10}cm")
            print(f"{value}mm is {value / 1000}m")
            print(f"{value}mm is {value / 1000000}km")

            time.sleep(1)
        elif first_unit == "2":
            print(f"{value}cm is {value * 10}mm")
            print(f"{value}cm is {value / 100}m")
            print(f"{value}cm is {value /100000}km")

            time.sleep(1)
        elif first_unit == "3":
            print(f"{value}m is {value * 1000}mm")
            print(f"{value}m is {value * 100}cm")
            print(f"{value}m is {value / 1000}km")

            time.sleep(1)
        elif first_unit == "4":
            print(f"{value}km is {value * 1000000}mm")
            print(f"{value}km is {value * 100000}cm")
            print(f"{value}km is {value * 1000}m")

            time.sleep(1)
        elif first_unit == "5":
            print("Switching Conversion\n")
            time.sleep(1)
            return
        elif first_unit == "6":
            print("Exiting program")
            time.sleep(1)
            break
        else:
            print("INVALID")
            time.sleep(2)

def imperial_to_metric():
    while True:
        first_unit = str(input("Unit to convert from?\n (1): Inches\n (2): Feet\n (3): Yards\n (4): Miles\n (5): Switch Conversion\n (6): Exit Conversion\n>"))
        value = float(input("Enter value to convert: "))
        if first_unit == "1":
            print(f"{value} inches is {value * 25.4}mm")
            print(f"{value} inches is {value * 2.54}cm")
            print(f"{value} inches is {value / 39.37}m")
            print(f"{value} inches is ~{value / 39370}km")

            time.sleep(1)
        elif first_unit == "2":
            print(f"{value} feet is {value * 304.8}mm")
            print(f"{value} feet is {value * 30.48}cm")
            print(f"{value} feet is ~{value / 3.281}m")
            print(f"{value} feet is ~{value / 3281}km")

            time.sleep(1)
        elif first_unit == "3":
            print(f"{value} yards is {value * 914.4}mm")
            print(f"{value} yards is {value * 91.44}cm")
            print(f"{value} yards is ~{value / 1.094}m")
            print(f"{value} yards is ~{value / 1094}km")

            time.sleep(1)
        elif first_unit == "4":
            print(f"{value} miles is ~{value * 1,608,000}mm")
            print(f"{value} miles is ~{value * 160900}cm")
            print(f"{value} miles is ~{value * 1609}m")
            print(f"{value} miles is ~{value * 1.609}km")
        elif first_unit == "5":
            print("Switching Conversion")
            time.sleep(1)
            return
        elif first_unit == "6":
            print("Exiting Conversion")
            time.sleep(1)
            break
        else:
            print("INVALID")
            time.sleep(2)

def metric_to_imperial():
    while True:
        first_value = str(input("Unit to convert from?\n (1): Milimeters\n (2): Centimeters\n (3): Meters\n (4): Kilometers\n (5): Switch Conversion\n (6): Exit Conversion\n>"))
        value = float(input("Enter value to convert: "))
        if first_value == "1":
            print("mm")
        elif first_value == "2":
            print("cm")
        elif first_value == "3":
            print("m")
        elif first_value == "4":
            print("km")
        elif first_value == "5":
            print("Switching conversion")
            return
        elif first_value == "6":
            print("Exiting conversion")
            break
        else:
            print("INVALID")
            time.sleep(2)

def get_info():
    while True:
        unit_system = str(input("Which measurement system are you converting?\n (1): Imperial (Freedom Units)\n (2): Metric\n (3): Imp. -> Metric\n (4): Metric -> Imp.\n (5): Exit Program> "))

        if unit_system == "1":
            imperial_convert()
        elif unit_system == "2":
            metric_convert()
        elif unit_system == "3":
            print("Imperial to metric")
        elif unit_system == "4":
            print("Metric to imperial")
        elif unit_system == "5":
            print("Exiting Program")
            break
get_info()