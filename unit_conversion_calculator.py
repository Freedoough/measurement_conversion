import math
import time
import sys

# add unit abbreviations in menu options and use them in calculation output

print("Unit Conversion\n\n") # Program title
time.sleep(1)


def imperial_convert():
    while True: # Imperial system unit conversion loop

        print("Imperial system distance measurement conversion:\n")
        time.sleep(1)

        first_unit = str(input("Unit to convert from?\n (1): Inches\n (2): Feet\n (3): Yards\n (4): Miles\n (5): Switch Conversion\n (6): Exit Program\n> ").rstrip())

        if first_unit in ["1", "2", "3", "4", "5", "6"]:
            
            if first_unit == "5": # Switch conversion system
                print("Switching Conversion\n")
                time.sleep(1)
                return
            elif first_unit == "6": # Exit program
                print("Exiting Program")
                sys.exit()

            else:
                while True:
                    try:
                        value = float(input("Enter value to convert: ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter a numeric value.\n")
                        time.sleep(2)

                if first_unit == "1": # Inches conversion to other units
                    print(f"{value} inches is {value / 12} feet")
                    print(f"{value} inches is {value / 36} yards")
                    print(f"{value} inches is {value / 63360} miles")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2": # Feet conversion to other units
                    print(f"{value} feet is {value * 12} inches")
                    print(f"{value} feet is {value / 3} yards")
                    print(f"{value} feet is {value / 5280} miles")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "3": # Yards conversion to other units
                    print(f"{value} yards is {value * 36} inches")
                    print(f"{value} yards is {value * 3} feet")
                    print(f"{value} yards is {value / 1760} miles")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "4": # Miles conversion to other units
                    print(f"{value} miles is {value * 63360} inches")
                    print(f"{value} miles is {value * 5280} feet")
                    print(f"{value} miles is {value * 1760} yards")

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
                while True:
                    try:
                        value = float(input("Enter value to convert: ").rstrip())
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
                while True:
                    try:
                        value = float(input("Enter value to convert: ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter a numeric value.\n")
                        time.sleep(2)

                if first_unit == "1":
                    print(f"{value} inches is {value * 25.4}mm")
                    print(f"{value} inches is {value * 2.54}cm")
                    print(f"{value} inches is {value / 39.37}m")
                    print(f"{value} inches is ~{value / 39370}km")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "2":
                    print(f"{value} feet is {value * 304.8}mm")
                    print(f"{value} feet is {value * 30.48}cm")
                    print(f"{value} feet is ~{value / 3.281}m")
                    print(f"{value} feet is ~{value / 3281}km")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "3":
                    print(f"{value} yards is {value * 914.4}mm")
                    print(f"{value} yards is {value * 91.44}cm")
                    print(f"{value} yards is ~{value / 1.094}m")
                    print(f"{value} yards is ~{value / 1094}km")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_unit == "4":
                    print(f"{value} miles is ~{value * 1,608,000}mm")
                    print(f"{value} miles is ~{value * 160900}cm")
                    print(f"{value} miles is ~{value * 1609}m")
                    print(f"{value} miles is ~{value * 1.609}km")

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
                while True:
                    try:
                        value = float(input("Enter value to convert:").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter a numeric value.\n")
                        time.sleep(2)

                if first_value == "1":
                    print(f"{value}mm is {value / 25.4} inches")
                    print(f"{value}mm is {value / 304.8} feet")
                    print(f"{value}mm is {value / 914.4} yards")
                    print(f"{value}mm is ~{value / 1,608,000} miles")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_value == "2":
                    print(f"{value}cm is {value / 2.54} inches")
                    print(f"{value}cm is {value / 30.48} feet")
                    print(f"{value}cm is {value / 91.44} yards")
                    print(f"{value}cm is ~{value / 160900} miles")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)
                elif first_value == "3":
                    print(f"{value}m is {value * 39.37} inches")
                    print(f"{value}m is ~{value * 3.281} feet")
                    print(f"{value}m is ~{value * 1.094} yards")
                    print(f"{value}m is ~{value / 1609} miles")

                    time.sleep(3)
                    print("\n")
                    time.sleep(1)

                elif first_value == "4":
                    print(f"{value}km is ~{value * 39370} inches")
                    print(f"{value}km is ~{value * 3281} feet")
                    print(f"{value}km is ~{value * 1094} yards")
                    print(f"{value}km is ~{value / 1.609} miles")

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
                while True:
                    try:
                        value = float(input("Enter value to convert: ").rstrip())
                        break
                    except ValueError:
                        print("INVALID input, please enter a numeric value.\n")
                        time.sleep(2)

                        # oz, lbs, tn
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
                while True:
                    try:
                        value = float(input("Enter value to convert: ").rstrip())
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
                while True:
                    try:
                        value = float(input("Enter value to convert: ").rstrip())
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
                while True:
                    try:
                        value = float(input("Enter value to convert: ").rstrip())
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
    #print("mph , fps, knots")
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
                while True:
                    try:
                        value = float(input("Enter value to convert: ").rstrip())
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


def metric_speed(): #print("m/s, kph, knots")
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
                while True:
                    try:
                        value = float(input("Enter value to convert: "))
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
                while True:
                    try:
                        value = float(input("Enter value to convert: "))
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
            elif first_unit == "3":
                print("Exiting Program")
                sys.exit()
            else:
                while True:
                    try:
                        value = float(input("Enter value to convert: ").rstrip())
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

        # Measurements to add:
        # Temperature
        # Volume
        measurement_type = str(input("What type of measurement would you like to convert?\n (1): Distance\n (2): Mass\n (3): Speed\n (4): Exit Program\n> ").rstrip())
        
        if measurement_type == "1":
            distance_convert()
        elif measurement_type == "2":
            mass_convert()
        elif measurement_type == "3":
            speed_convert()
        elif measurement_type == "4":
            print("Exiting Program")
            time.sleep(1)
            return False
        else:
            print("INVALID")
            time.sleep(2)
            print("\n")

get_info() # Initial function call for conversion prompts