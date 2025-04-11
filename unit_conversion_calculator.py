import math
import time
import sys
from types import UnionType

# add unit abbreviations in menu options and use them in calculation output

print("Unit Conversion\n\n") # Program title
time.sleep(1)


def imperial_convert():
    while True: # Imperial system unit conversion loop

        print("Imperial system distance measurement conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Inches (in)\n (2): Feet (ft)\n (3): Yards (yd)\n (4): Miles (mi)\n (5): Switch Conversion\n (6): Exit Program\n> ").rstrip())

        if first_unit in ["1", "2", "3", "4", "5", "6"]:
            
            if first_unit == "5": # Switch conversion system
                print("Switching Conversion\n")
                time.sleep(1)
                return
            elif first_unit == "6": # Exit program
                print("Exiting Program")
                sys.exit()

            else:

                units = {
                    "1": "Inches",
                    "2": "Feet",
                    "3": "Yards",
                    "4": "Miles"
                    }

                selected_unit = units[first_unit]

                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter a numeric value.\n")
                        time.sleep(2)

                if first_unit == "1": # Inches conversion to other units
                    print(f"{value} in. is {value / 12} ft.")
                    print(f"{value} in. is {value / 36} yds.")
                    print(f"{value} in. is {value / 63360} mi.")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2": # Feet conversion to other units
                    print(f"{value} ft. is {value * 12} in.")
                    print(f"{value} ft. is {value / 3} yds.")
                    print(f"{value} ft. is {value / 5280} mi.")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "3": # Yards conversion to other units
                    print(f"{value} yds. is {value * 36} in.")
                    print(f"{value} yds. is {value * 3} ft.")
                    print(f"{value} yds is {value / 1760} mi.")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "4": # Miles conversion to other units
                    print(f"{value} mi. is {value * 63360} in.")
                    print(f"{value} mi. is {value * 5280} ft.")
                    print(f"{value} mi. is {value * 1760} yds.")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")
            
def metric_convert():
    while True:

        print("Metric system distance measurement conversion:\n")
        time.sleep(1)

        first_unit =  str(input("Unit to convert from?\n (1): Milimeters\n (2): Centimeters\n (3): Meters\n (4): Kilometers\n (5): Switch Conversion\n (6): Exit Program\n> ").rstrip())
        
        if first_unit in ["1", "2", "3", "4", "5", "6"]:
            if first_unit == "5":
                print("Switching Conversion\n")
                time.sleep(1)
                return 
            elif first_unit == "6":
                print("Exiting program")
                time.sleep(1)
                sys.exit()
            else:

                units = {
                    
                    "1": "Milimeters",
                    "2": "Centimeters",
                    "3": "Meters",
                    "4": "Kilometers"                   
                    }

                selected_unit = units[first_unit]

                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter a numeric value.\n")
                        time.sleep(2)  
                        
                if first_unit == "1":
                    print(f"{value}mm is {value / 10}cm")
                    print(f"{value}mm is {value / 1000}m")
                    print(f"{value}mm is {value / 1000000}km")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2":
                    print(f"{value}cm is {value * 10}mm")
                    print(f"{value}cm is {value / 100}m")
                    print(f"{value}cm is {value /100000}km")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "3":
                    print(f"{value}m is {value * 1000}mm")
                    print(f"{value}m is {value * 100}cm")
                    print(f"{value}m is {value / 1000}km")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "4":
                    print(f"{value}km is {value * 1000000}mm")
                    print(f"{value}km is {value * 100000}cm")
                    print(f"{value}km is {value * 1000}m")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

def imperial_to_metric():
    while True:

        print("Imperial to Metric system distance conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Inches\n (2): Feet\n (3): Yards\n (4): Miles\n (5): Switch Conversion\n (6): Exit Program\n> ").rstrip())
        
        if first_unit in ["1", "2", "3", "4", "5", "6"]:

            if first_unit == "5":
                print("Switching Conversion\n")
                time.sleep(1)
                return 
            elif first_unit == "6":
                print("Exiting Program")
                time.sleep(1)
                sys.exit()
            else:

                unit = {
                    "1": "Inches",
                    "2": "Feet",
                    "3": "Yards",
                    "4": "Miles"
                    }

                selected_unit = unit[first_unit]

                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter a numeric value.\n")
                        time.sleep(2)

                if first_unit == "1":
                    print(f"{value} in. is {value * 25.4}mm")
                    print(f"{value} in. is {value * 2.54}cm")
                    print(f"{value} in. is {value / 39.37}m")
                    print(f"{value} in. is ~{value / 39370}km")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2":
                    print(f"{value} ft is {value * 304.8}mm")
                    print(f"{value} ft is {value * 30.48}cm")
                    print(f"{value} ft is ~{value / 3.281}m")
                    print(f"{value} ft is ~{value / 3281}km")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "3":
                    print(f"{value} yds is {value * 914.4}mm")
                    print(f"{value} yds is {value * 91.44}cm")
                    print(f"{value} yds is ~{value / 1.094}m")
                    print(f"{value} yds is ~{value / 1094}km")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "4":
                    print(f"{value} mi. is ~{value * 1,608,000}mm")
                    print(f"{value} mi. is ~{value * 160900}cm")
                    print(f"{value} mi. is ~{value * 1609}m")
                    print(f"{value} mi. is ~{value * 1.609}km")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

def metric_to_imperial():
    while True:

        print("Metric to Imperial system distance conversion:\n")
        time.sleep(1)

        first_value = str(input("Unit to convert from?\n (1): Milimeters\n (2): Centimeters\n (3): Meters\n (4): Kilometers\n (5): Switch Conversion\n (6): Exit Program\n> ").rstrip())
        
        if first_value in ["1", "2", "3", "4", "5", "6"]:

            if first_value == "5":
                print("Switching Conversion\n")
                time.sleep(1)
                return 
            elif first_value == "6":
                print("Exiting Program")
                sys.exit()
            else:

                unit = {
                    "1": "Milimeters",
                    "2": "Centimeters",
                    "3": "Meters",
                    "4": "Kilometers"                   
                    }

                selected_unit = unit[first_value]

                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}):").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter a numeric value.\n")
                        time.sleep(2)

                if first_value == "1":
                    print(f"{value}mm is {value / 25.4} in.")
                    print(f"{value}mm is {value / 304.8} ft")
                    print(f"{value}mm is {value / 914.4} yds")
                    print(f"{value}mm is ~{value / 1,608,000} mi.")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_value == "2":
                    print(f"{value}cm is {value / 2.54} in.")
                    print(f"{value}cm is {value / 30.48} ft")
                    print(f"{value}cm is {value / 91.44} yds")
                    print(f"{value}cm is ~{value / 160900} mi.")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_value == "3":
                    print(f"{value}m is {value * 39.37} in.")
                    print(f"{value}m is ~{value * 3.281} ft")
                    print(f"{value}m is ~{value * 1.094} yds")
                    print(f"{value}m is ~{value / 1609} mi.")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)

                elif first_value == "4":
                    print(f"{value}km is ~{value * 39370} in.")
                    print(f"{value}km is ~{value * 3281} ft")
                    print(f"{value}km is ~{value * 1094} yds")
                    print(f"{value}km is ~{value / 1.609} mi.")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

def imperial_mass():
    while True:
        print("Imperial mass measurement conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Ounces (oz)\n (2): Pounds (lb)\n (3): US Tons (tn)\n (4): Switch Conversion\n (5): Exit Program\n> ").rstrip())

        if first_unit in ["1", "2", "3", "4", "5"]:

            if first_unit == "4":
                print("Switching Conversion\n")
                time.sleep(1)
                return
            elif first_unit == "5":
                print("Exiting Program")
                sys.exit()

            else:

                unit = {
                    "1": "Ounces",
                    "2": "Pounds",
                    "3": "US Tons"
                    }

                selected_unit = unit[first_unit]

                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter a numeric value.\n")
                        time.sleep(2)

                if first_unit == "1":
                    print(f"{value} oz is {value / 16} lbs") 
                    print(f"{value} oz is {value / 3200} tn")
                        
                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2":
                    print(f"{value}lbs is {value * 16} oz")
                    print(f"{value} lbs is {value * 2000} tn")
                        
                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "3":
                    print(f"{value}tn is {value * 32000} oz")
                    print(f"{value} tn is {value * 2000} lbs")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

def metric_mass():
    while True:

        print("Metric system mass measurement conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Milligram (mg)\n (2): Gram (g)\n (3): Kilogram (kg)\n (4): Switch conversion\n (5): Exit Program\n> ").rstrip())
        
        if first_unit in ["1", "2", "3", "4", "5"]:

            if first_unit == "4":
                print("Switching Conversion\n")
                time.sleep(1)
                return
            elif first_unit == "5":
                print("Exiting Program")
                sys.exit()

            else:

                unit = {
                    "1": "Miligram",
                    "2": "Gram",
                    "3": "Kilogram"                   
                    }

                selected_unit = unit[first_unit]
                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter a numeric value. \n")

                if first_unit == "1":
                    print(f"{value} mg is {value / 1000} g")
                    print(f"{value} mg is {value / 32000} kg")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2":
                    print(f"{value} g is {value * 1000} mg")
                    print(f"{value} g is {value / 1000} kg")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "3":
                    print(f"{value} kg is {value / 1000000} mg")
                    print(f"{value} kg is {value * 1000} g")
                    
                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

def imp_to_metric_mass():
    while True:

        print("Imperial to Metric mass conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Ounces (oz)\n (2): Pounds (lb)\n (3): US Tons (tn)\n (4): Switch Conversion\n (5): Exit Program\n> ").rstrip())

        if first_unit in ["1", "2", "3", "4", "5"]:
            if first_unit == "4":
                print("Switching Conversion\n")
                time.sleep(1)
                return
            elif first_unit == "5":
                print("Exiting Program")
                sys.exit()

            else:

                unit = {
                    "1": "Ounces",
                    "2": "Pounds",
                    "3": "US Tons"                   
                    }

                selected_unit = unit[first_unit]

                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter numeric value.\n")
                        time.sleep(2)

                if first_unit == "1":
                    print(f"{value} oz is ~{value * 28350} mg")
                    print(f"{value} oz is ~{value * 28.35} g")
                    print(f"{value} oz is {value / 35.274} kg")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2":
                    print(f"{value} lb is ~{value * 453600} mg")
                    print(f"{value} lb is ~{value * 453.6} g")
                    print(f"{value} lb is ~{value / 2.205} kg")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "3":
                    print(f"{value} tn is ~{value * 907200000} mg")
                    print(f"{value} tn is ~{value * 907200} g")
                    print(f"{value} tn is ~{value * 907.2} kg")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

def metric_to_imp_mass():
    while True:

        print("Metric to Imperial mass conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Milligrams (mg)\n (2): Grams (g)\n (3): Kilograms\n (4): Switch Conversion\n (5): Exit Program\n> ").rstrip())
        
        if first_unit in ["1", "2", "3", "4", "5"]:
            if first_unit == "4":
                print("Switching Conversion\n")
                time.sleep(1)
                return
            elif first_unit == "5":
                print("Exiting Program")
                sys.exit()

            else:

                unit = {
                    "1": "Miligrams",
                    "2": "Grams",
                    "3": "Kilograms"                    
                    }

                selected_unit = unit[first_unit]

                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter numeric value.\n")
                        time.sleep(2)

                if first_unit == "1":
                    print(f"{value} mg is ~{value / 28350} oz")
                    print(f"{value} mg is ~{value / 453600} lb")
                    print(f"{value} mg is ~{value / 907200000} tn")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)

                elif first_unit == "2":
                    print(f"{value} g is ~{value / 28.35} oz")
                    print(f"{value} g is ~{value / 453.6} lb")
                    print(f"{value} g is ~{value / 907200} tn")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)

                elif first_unit == "3":
                    print(f"{value} kg is {value * 35.274} oz")
                    print(f"{value} kg is ~{value * 2.205} lb")
                    print(f"{value} kg is ~{value / 907.2} tn")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)

                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

def imperial_speed():
    while True:

        print("Imperial Speed Conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Miles per hour (Mph)\n (2): Feet per second (Fps)\n (3): Switch Conversion\n (4): Exit Program\n> ").rstrip())
        
        if first_unit in ["1", "2", "3", "4"]:
            if first_unit == "3":
                print("Switching Conversion\n")
                time.sleep(1)
                return
            elif first_unit == "4":
                print("Exiting Program")
                sys.exit()
            else:

                unit = {
                    "1": "Miles per hour",
                    "2": "Feet per second",
                    }

                selected_unit = unit[first_unit]
                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter numeric value.\n")
                        time.sleep(2)

                if first_unit == "1":
                    print(f"{value} mph is ~{value * 1.467} fps")
                    print(f"{value} mph is ~{value / 1.151} kts")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2":
                    print(f"{value} fps is ~{value / 1.467} mph")
                    print(f"{value} fps is ~{value / 1.688} kts")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

def metric_speed(): 
    while True:
        print("Metric speed conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Meters per second (m/s)\n (2): Kilometers per hour (kph)\n (3): Switch Conversion\n (4): Exit Program\n> ").rstrip())

        if first_unit in ["1", "2", "3", "4"]:
            if first_unit == "3":
                print("Switching Conversion\n")
                time.sleep(1)
                return
            elif first_unit == "4":
                print("Exiting Program")
                sys.exit()
            else:

                unit = {
                    "1": "Meters per second",
                    "2": "Kilometers per hour"
                    }

                selected_unit = unit[first_unit]

                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter numeric value.\n")
                        time.sleep(2)
                if first_unit == "1":
                    print(f"{value} m/s is {value * 3.6} kph")
                    print(f"{value} m/s is ~{value * 1.944} kts")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2":
                    print(f"{value} kph is {value / 3.6} m/s")
                    print(f"{value} kph is {value / 1.852} kts")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

def imperial_speed_to_metric():
    while True:
        print("Imperial to metric speed conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Miles per hour (mph)\n (2): Feet per second (fps)\n (3): Switch conversion\n (4): Exit Program\n> ").rstrip())
        
        if first_unit in ["1", "2", "3", "4"]:
            if first_unit == "3":
                print("Switching Conversion\n")
                time.sleep(1)
                return
            elif first_unit == "4":
                print("Exiting Program")
                sys.exit()
            else:

                unit = {
                    "1": "Miles per hour",
                    "2": "Feet per second"
                    }

                selected_unit = unit[first_unit]

                while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID iput, please enter numeric value.\n")
                        time.sleep(2)
                if first_unit == "1":
                    print(f"{value} mph is {value / 2.237} m/s")
                    print(f"{value} mph is ~{value * 1.609} kph")
                    print(f"{value} mph is ~{value / 1.151} kts")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2":
                    print(f"{value} fps is ~{value / 3.281} m/s")
                    print(f"{value} fps is ~{value * 1.097} kph")
                    print(f"{value} fps is ~{value / 1.688} kts")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)
       
def metric_speed_to_imperial():
    while True:
        print("Metric to Imperial speed conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Meters per second (m/s)\n (2): Kilometers per hour (kph)\n (3): Switch Conversion\n (4): Exit Program\n> ").rstrip())

        if first_unit in ["1", "2", "3", "4"]:
            if first_unit == "3":
                print("Switching Conversion\n")
                time.sleep(1)
                return
            elif first_unit == "4":
                print("Exiting Program")
                sys.exit()
            else:

                unit = {
                    "1": "Meters per second",
                    "2": "Kilometers per hour"
                    }

                selected_unit = unit[first_unit]

                while True:
                    try:
                        value = float(input(f"Enter value to convert ({first_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter numeric value.\n")
                        time.sleep(2)
                if first_unit == "1":
                    print(f"{value} m/s is ~{value * 3.281} fps")
                    print(f"{value} m/s is {value * 2.237} mph")
                    print(f"{value} m/s is ~{value * 1.944} kts")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2":
                    print(f"{value} kph is ~{value / 1.097} fps")
                    print(f"{value} kph is ~{value / 1.609} mph")
                    print(f"{value} kph is {value / 1.852} kts")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)

def knots():
    while True:
        print("Knots to Metric and Imperial speed conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Knots\n (2): Switch Conversion\n (3): Exit Program\n> ").rstrip())

        if first_unit in ["1", "2", "3"]:
            if first_unit == "2":
                print("Switching Conversion")
                time.sleep(1)
                return
            elif first_unit == "3":
                print("Exiting Program")
                sys.exit()
            else:
                while True:
                    try:
                        value = float(input("Enter value to convert (Knots): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter numeric value.\n")
                        time.sleep(2)
                if first_unit == "1":
                    print("Imperial Conversion:\n")
                    print(f"{value} kts is ~{value * 1.688} fps")
                    print(f"{value} kts is ~{value * 1.151} mph")
                    print("Metric Conversion:\n")
                    print(f"{value} kts is ~{value / 1.944} m/s")
                    print(f"{value} kts is {value * 1.852} kph")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)

def f_to_c():
    while True:
        print("°F to °C Conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): °F \n (2): Switch Conversion\n (3): Exit Program\n> ").rstrip())

        if first_unit in ["1", "2", "3"]:
            if first_unit == "2":
                print("Switching Conversion")
                time.sleep(1)
                return
            elif first_unit == "3":
                print("Exiting Program")
                sys.exit()
            else:
                while True:
                    try:
                        value = float(input("Enter value to convert (°F): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter numeric value.")
                        time.sleep(2)
                if first_unit == "1":
                    print(f"{value} °F is {(value - 32) * 5/9 } °C")
                    print(f"{value} °F is {(value - 32) * 5/9 + 273.15} °K ")
                    
                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)

def c_to_f():
    while True:
        print("°C to °F Conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): °C \n (2): Switch Conversion\n (3): Exit Program\n> ").rstrip())

        if first_unit in ["1", "2", "3"]:
            if first_unit == "2":
                print("Switching Conversion")
                time.sleep(1)
                return
            elif first_unit == "3":
                print("Exiting Program")
                sys.exit()
            else:
                while True:
                    try:
                        value = float(input("Enter value to convert (°C): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter numeric value.")
                        time.sleep(2)
                if first_unit == "1":
                    print(f"{value} °C is {(value * 9/5) + 32 } °F")
                    print(f"{value} °C is {value + 273.15} °K")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)

def kelvin_convert():
    while True:
        print("°K to °C and °F Conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): °K \n (2): Switch Conversion\n (3): Exit Program\n> ").rstrip())

        if first_unit in ["1", "2", "3"]:
            if first_unit == "2":
                print("Switching Conversion")
                time.sleep(1)
                return
            elif first_unit == "3":
                print("Exiting Program")
                sys.exit()
            else:
                while True:
                    try:
                        value = float(input("Enter value to convert (°K): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter numeric value.")
                        time.sleep(2)
                if first_unit == "1":
                    print(f"{value} °K is {(value - 273.15) * 9/5 + 32 } °F")
                    print(f"{value} °K is {value - 273.15} °C")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                else:
                    print("INVALID")
                    time.sleep(2)

def digital_storage_convert(): # bits, bytes, kilobytes, megabytes, gigabytes, terabytes, petabytes, zetabytes?
    while True:
       print("Digital Storage Conversion:\n")
       time.sleep(1)

       first_unit = str(input("Unit to convert from?:\n (1): Bits\n (2): Bytes\n (3): Kilobytes\n (4): Megabytes\n (5): Gigabytes\n (6): Terabytes\n (7): Petabytes\n (8): Exabytes\n (9): Zettabytes\n (10): Switch Conversion\n (11): Exit Program\n > "))

       if first_unit in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            if first_unit == "10":
               print("Switching Conversion\n")
               time.sleep(1)
               return
            elif first_unit == "11":
               print("Exiting Program")
               sys.exit()
            else:

               unit = {
                   "1": "Bits",
                   "2": "Bytes",
                   "3": "Kilobytes",
                   "4": "Megabytes",
                   "5": "Gigabytes",
                   "6": "Terabytes",
                   "7": "Petabytes",
                   "8": "Exabytes",
                   "9": "Zettabytes",                   
                   }

               selected_unit = unit[first_unit]


               while True:
                    try:
                        value = float(input(f"Enter value to convert ({selected_unit}): ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter numeric value.")
                        time.sleep(2)
               if first_unit == "1":
                    # bits
                    print(f"{value} b is {value / 8:,.6f} B")
                    print(f"{value} b is {value / (8 * 1024):,.6f} kB")
                    print(f"{value} b is {value / (8 * 1024 * 1024):,.6f} MB")
                    print(f"{value} b is {value / (8 * 1024 * 1024 * 1024):,.6f} GB")
                    print(f"{value} b is {value / (8 * 1024 * 1024 * 1024 * 1024):,.6f} TB")
                    print(f"{value} b is {value / (8 * 1024 * 1024 * 1024 * 1024 * 1024):,.6f} PB")
                    print(f"{value} b is {value / (8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024):,.6f} EB")
                    print(f"{value} b is {value / (8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024):,.6f} ZB")
                    
                    
                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
               elif first_unit == "2":
                    # bytes
                    print(f"{value} B is {value * 8:,.6f} b")
                    print(f"{value} B is {value / 1024:,.6f} KB")
                    print(f"{value} B is {value / (1024 * 1024):,.6f} MB")
                    print(f"{value} B is {value / (1024 * 1024 * 1024):,.6f} GB")
                    print(f"{value} B is {value / (1024 * 1024 * 1024 * 1024):,.6f} TB")
                    print(f"{value} B is {value / (1024 * 1024 * 1024 * 1024 * 1024):,.6f} PB")
                    print(f"{value} B is {value / (1024 * 1024 * 1024 * 1024 * 1024 * 1024):,.6f} EB")  
                    print(f"{value} B is {value / (1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024):,.6f} ZB")


                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
               elif first_unit == "3":
                    # kilobytes
                    print(f"{value} KB is {value * 1024 * 8:,.6f} b")
                    print(f"{value} KB is {value * 1024:,.6f} B") 
                    print(f"{value} KB is {value / 1024:,.6f} MB")  
                    print(f"{value} KB is {value / (1024 * 1024):,.6f} GB")  
                    print(f"{value} KB is {value / (1024 * 1024 * 1024):,.6f} TB")  
                    print(f"{value} KB is {value / (1024 * 1024 * 1024 * 1024):,.6f} PB") 
                    print(f"{value} KB is {value / (1024 * 1024 * 1024 * 1024 * 1024):,.6f} EB")  
                    print(f"{value} KB is {value / (1024 * 1024 * 1024 * 1024 * 1024 * 1024):6f} ZB")  


                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
               elif first_unit == "4":
                    # megabytes
                    print(f"{value} MB is {value * 1024 * 1024 * 8:,.6f} b")
                    print(f"{value} MB is {value * 1024 * 1024:,.6f} B") 
                    print(f"{value} MB is {value * 1024:,.6f} KB")                    
                    print(f"{value} MB is {value / 1024:,.6f} GB") 
                    print(f"{value} MB is {value / (1024 * 1024):,.6f} TB")  
                    print(f"{value} MB is {value / (1024 * 1024 * 1024):,.6f} PB")  
                    print(f"{value} MB is {value / (1024 * 1024 * 1024 * 1024):,.6f} EB")  
                    print(f"{value} MB is {value / (1024 * 1024 * 1024 * 1024 * 1024):,.6f} ZB")  


                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
               elif first_unit == "5":
                    # gigabytes
                    print(f"{value} GB is {value * 1024 * 1024 * 1024 * 8:,.6f} b")
                    print(f"{value} GB is {value * 1024 * 1024 * 1024:,.6f} B")  
                    print(f"{value} GB is {value * 1024 * 1024} KB")  
                    print(f"{value} GB is {value * 1024:,.6f} MB")                  
                    print(f"{value} GB is {value / 1024:,.6f} TB")  
                    print(f"{value} GB is {value / (1024 * 1024):,.6f} PB")  
                    print(f"{value} GB is {value / (1024 * 1024 * 1024):,.6f} EB")  
                    print(f"{value} GB is {value / (1024 * 1024 * 1024 * 1024):,.6f} ZB")  


                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
               elif first_unit == "6":
                    # terabytes
                    print(f"{value} TB is {value * 1024 * 1024 * 1024 * 1024 * 8:,.6f} b") 
                    print(f"{value} TB is {value * 1024 * 1024 * 1024 * 1024:,.6f} B") 
                    print(f"{value} TB is {value * 1024 * 1024 * 1024:,.6f} KB") 
                    print(f"{value} TB is {value * 1024 * 1024:,.6f} MB") 
                    print(f"{value} TB is {value * 1024:,.6f} GB") 
                    print(f"{value} TB is {value / 1024:,.6f} PB") 
                    print(f"{value} TB is {value / (1024 * 1024):,.6f} EB")  
                    print(f"{value} TB is {value / (1024 * 1024 * 1024):,.6f} ZB")  


                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
               elif first_unit == "7":
                    # petabytes

                    print(f"{value} PB is {value * 1024 * 1024 * 1024 * 1024 * 1024 * 8:,.6f} b")  
                    print(f"{value} PB is {value * 1024 * 1024 * 1024 * 1024 * 1024:,.6f} B") 
                    print(f"{value} PB is {value * 1024 * 1024 * 1024 * 1024:,.6f} KB") 
                    print(f"{value} PB is {value * 1024 * 1024 * 1024:,.6f} MB") 
                    print(f"{value} PB is {value * 1024 * 1024:,.6f} GB") 
                    print(f"{value} PB is {value * 1024:,.6f} TB")  
                    print(f"{value} PB is {value / 1024:,.6f} EB") 
                    print(f"{value} PB is {value / (1024 * 1024):,.6f} ZB")  



                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
               elif first_unit == "8":
                    # exabytes

                    print(f"{value} EB is {value * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 8:,.6f} b") 
                    print(f"{value} EB is {value * 1024 * 1024 * 1024 * 1024 * 1024 * 1024:,.6f} B")
                    print(f"{value} EB is {value * 1024 * 1024 * 1024 * 1024 * 1024:,.6f} KB") 
                    print(f"{value} EB is {value * 1024 * 1024 * 1024 * 1024:,.6f} MB")  
                    print(f"{value} EB is {value * 1024 * 1024 * 1024:,.6f} GB") 
                    print(f"{value} EB is {value * 1024 * 1024:,.6f} TB") 
                    print(f"{value} EB is {value * 1024:,.6f} PB")  
                    print(f"{value} EB is {value / 1024:,.6f} ZB")            
                    
                    
                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
               elif first_unit == "9":
                    # zettabytes

                    print(f"{value} ZB is {value * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 8:,.6f} b") 
                    print(f"{value} ZB is {value * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024:,.6f} B") 
                    print(f"{value} ZB is {value * 1024 * 1024 * 1024 * 1024 * 1024 * 1024:,.6f} KB") 
                    print(f"{value} ZB is {value * 1024 * 1024 * 1024 * 1024 * 1024:,.6f} MB") 
                    print(f"{value} ZB is {value * 1024 * 1024 * 1024 * 1024:,.6f} GB")  
                    print(f"{value} ZB is {value * 1024 * 1024 * 1024:,.6f} TB") 
                    print(f"{value} ZB is {value * 1024 * 1024:,.6f} PB") 
                    print(f"{value} ZB is {value * 1024:,.6f} EB") 

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
               else:
                    print("INVALID")
                    time.sleep(2)
def get_info(): # Initial prompt to get info about which meaurement is being calculated
    while True:
        
        def distance_convert():
            while True:

                print("Distance conversion:\n")
                time.sleep(1)    

                unit_system = str(input("Which measurement system are you converting?\n (1): Imperial (Freedom Units)\n (2): Metric\n (3): Imp. -> Metric\n (4): Metric -> Imp.\n (5): Switch Conversion\n (6): Exit Program\n> "))
            
                if unit_system == "1":
                    imperial_convert()
                elif unit_system == "2":
                    metric_convert()
                elif unit_system == "3":
                    imperial_to_metric()
                elif unit_system == "4":
                    metric_to_imperial()
                elif unit_system == "5":
                    print("Switching Conversion")
                    time.sleep(1)
                    return False
                elif unit_system == "6":
                    print("Exiting Program")
                    time.sleep(1)
                    sys.exit()
                else:
                    print("INVALID")
                time.sleep(2)
                print("\n")
   
        def mass_convert():
            
            while True:
                print("Mass Conversion:\n")
                time.sleep(1)

                unit_system = str(input("Which measurement system are you converting?\n (1): Imperial (Freedom Units)\n (2): Metric\n (3): Imp. -> Metric\n (4): Metric -> Imp.\n (5): Switch Conversion\n (6): Exit Program\n> ").rstrip())

                if unit_system == "1":
                    imperial_mass()
                elif unit_system == "2":
                    metric_mass()
                elif unit_system == "3":
                    imp_to_metric_mass()
                elif unit_system == "4":
                    metric_to_imp_mass()
                elif unit_system == "5":
                    print("Switching Conversion\n")
                    time.sleep(1)
                    return 
                elif unit_system == "6":
                    print("Exiting Program")
                    sys.exit()
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

        def speed_convert():

            while True:
                print("Speed Conversion:\n")
                time.sleep(1)

                unit_system = str(input("Which measurement system are you converting?\n (1): Imperial (Freedom Units)\n (2): Metric\n (3): Imp. -> Metric\n (4): Metric -> Imp.\n (5): Knots\n (6): Switch Conversion\n (7): Exit Program\n> ").rstrip())

                if unit_system == "1":
                    imperial_speed()
                elif unit_system == "2":
                    metric_speed()
                elif unit_system == "3":
                    imperial_speed_to_metric()
                elif unit_system == "4":
                    metric_speed_to_imperial()
                elif unit_system == "5":
                    knots()
                elif unit_system == "6":
                    print("Switching Conversion\n")
                    time.sleep(1)
                    return
                elif unit_system == "7":
                    print("Exiting Program")
                    sys.exit()
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

        def temp_convert():
            while True:
                print("Temperature Conversion:\n")
                time.sleep(1)

                unit_system = str(input("Which measurement are you converting?\n (1): °F\n (2): °C\n (3): °K\n (4): Switch Conversion\n (5): Exit Program\n> ").rstrip())

                if unit_system == "1":
                    f_to_c()
                elif unit_system == "2":
                    c_to_f()
                elif unit_system == "3":
                    kelvin_convert()
                elif unit_system == "4":
                    print("Switching Conversion\n")
                    time.sleep(1)
                    return
                elif unit_system == "5":
                    print("Exiting Program")
                    sys.exit()
                else:
                    print("INVALID")
                    time.sleep(2)
                    print("\n")

        #def digital_storage_convert():
            print("storage")

        # Measurements to add:
        # Volume
        measurement_type = str(input("What type of measurement would you like to convert?\n (1): Distance\n (2): Mass\n (3): Speed\n (4): Temperature\n (5): Digital Storage\n (6): Exit Program\n> ").rstrip())
        
        if measurement_type == "1":
            distance_convert()
        elif measurement_type == "2":
            mass_convert()
        elif measurement_type == "3":
            speed_convert()
        elif measurement_type == "4":
            temp_convert()
        elif measurement_type == "5":
            digital_storage_convert()
        elif measurement_type == "6":
            print("Exiting Program")
            time.sleep(1)
            return False
        else:
            print("INVALID")
            time.sleep(2)
            print("\n")

get_info() # Initial function call for conversion prompts