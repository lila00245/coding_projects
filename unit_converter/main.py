from conversion_helpers import *

#------------------------------------------------------------#
#             helper conversion functions                    #
#------------------------------------------------------------#

def convert_units(conversion_type1: str, conversion_type2: str, value: float) -> float:
    """Choose the conversion function based on user input."""
    # Length conversions
    if (conversion_type1 == "inches" or conversion_type1 == "in") and (conversion_type2 == "centimeters" or conversion_type2 == "cm"):
        return inches_to_centimeters(value)
    elif (conversion_type1 == "centimeters" or conversion_type1 == "cm") and (conversion_type2 == "inches" or conversion_type2 == "in"):
        return centimeters_to_inches(value)
    elif (conversion_type1 == "feet" or conversion_type1 == "ft") and (conversion_type2 == "meters" or conversion_type2 == "m"):
        return feet_to_meters(value)
    elif (conversion_type1 == "meters" or conversion_type1 == "m") and (conversion_type2 == "feet" or conversion_type2 == "ft"):
        return meters_to_feet(value)
    elif (conversion_type1 == "yards" or conversion_type1 == "yd") and (conversion_type2 == "meters" or conversion_type2 == "m"):
        return yards_to_meters(value)
    elif (conversion_type1 == "meters" or conversion_type1 == "m") and (conversion_type2 == "yards" or conversion_type2 == "yd"):
        return meters_to_yards(value)
    elif (conversion_type1 == "miles" or conversion_type1 == "mi") and (conversion_type2 == "kilometers" or conversion_type2 == "km"):
        return miles_to_kilometers(value)
    elif (conversion_type1 == "kilometers" or conversion_type1 == "km") and (conversion_type2 == "miles" or conversion_type2 == "mi"):
        return kilometers_to_miles(value)
    elif (conversion_type1 == "feet" or conversion_type1 == "ft") and (conversion_type2 == "inches" or conversion_type2 == "in"):
        return feet_to_inches(value)
    elif (conversion_type1 == "inches" or conversion_type1 == "in") and (conversion_type2 == "feet" or conversion_type2 == "ft"):
        return inches_to_feet(value)
    elif (conversion_type1 == "yards" or conversion_type1 == "yd") and (conversion_type2 == "feet" or conversion_type2 == "ft"):
        return yards_to_feet(value)
    elif (conversion_type1 == "feet" or conversion_type1 == "ft") and (conversion_type2 == "yards" or conversion_type2 == "yd"):
        return feet_to_yards(value)
    elif (conversion_type1 == "miles" or conversion_type1 == "mi") and (conversion_type2 == "feet" or conversion_type2 == "ft"):
        return miles_to_feet(value)
    elif (conversion_type1 == "feet" or conversion_type1 == "ft") and (conversion_type2 == "miles" or conversion_type2 == "mi"):
        return feet_to_miles(value)
    elif (conversion_type1 == "kilometers" or conversion_type1 == "km") and (conversion_type2 == "feet" or conversion_type2 == "ft"):
        return kilometers_to_feet(value)
    elif (conversion_type1 == "feet" or conversion_type1 == "ft") and (conversion_type2 == "kilometers" or conversion_type2 == "km"):
        return feet_to_kilometers(value)
    elif (conversion_type1 == "yards" or conversion_type1 == "yd") and (conversion_type2 == "miles" or conversion_type2 == "mi"):
        return yards_to_miles(value)
    elif (conversion_type1 == "miles" or conversion_type1 == "mi") and (conversion_type2 == "yards" or conversion_type2 == "yd"):
        return miles_to_yards(value)
    elif (conversion_type1 == "kilometers" or conversion_type1 == "km") and (conversion_type2 == "yards" or conversion_type2 == "yd"):
        return kilometers_to_yards(value)
    elif (conversion_type1 == "yards" or conversion_type1 == "yd") and (conversion_type2 == "kilometers" or conversion_type2 == "km"):
        return yards_to_kilometers(value)
    
    # Weight conversions
    elif (conversion_type1 == "pounds" or conversion_type1 == "lb") and (conversion_type2 == "kilograms" or conversion_type2 == "kg"):
        return pounds_to_kilograms(value)
    elif (conversion_type1 == "kilograms" or conversion_type1 == "kg") and (conversion_type2 == "pounds" or conversion_type2 == "lb"):
        return kilograms_to_pounds(value)
    elif (conversion_type1 == "ounces" or conversion_type1 == "oz") and (conversion_type2 == "grams" or conversion_type2 == "g"):
        return ounces_to_grams(value)
    elif (conversion_type1 == "grams" or conversion_type1 == "g") and (conversion_type2 == "ounces" or conversion_type2 == "oz"):
        return grams_to_ounces(value)
    elif (conversion_type1 == "tons" or conversion_type1 == "tn") and (conversion_type2 == "kilograms" or conversion_type2 == "kg"):
        return tons_to_kilograms(value)
    elif (conversion_type1 == "kilograms" or conversion_type1 == "kg") and (conversion_type2 == "tons" or conversion_type2 == "tn"):
        return kilograms_to_tons(value)
    
    # Temperature conversions
    elif (conversion_type1 == "Celsius" or conversion_type1 == "C") and (conversion_type2 == "Fahrenheit" or conversion_type2 == "F"):
        return celsius_to_fahrenheit(value)
    elif (conversion_type1 == "Fahrenheit" or conversion_type1 == "F") and (conversion_type2 == "Celsius" or conversion_type2 == "C"):
        return fahrenheit_to_celsius(value)
    elif (conversion_type1 == "Kelvin" or conversion_type1 == "K") and (conversion_type2 == "Celsius" or conversion_type2 == "C"):
        return kelvin_to_celsius(value)
    elif (conversion_type1 == "Celsius" or conversion_type1 == "C") and (conversion_type2 == "Kelvin" or conversion_type2 == "K"):
        return celsius_to_kelvin(value)
    
    # Volume conversions
    elif (conversion_type1 == "liters" or conversion_type1 == "L") and (conversion_type2 == "gallons" or conversion_type2 == "gal"):
        return liters_to_gallons(value)
    elif (conversion_type1 == "gallons" or conversion_type1 == "gal") and (conversion_type2 == "liters" or conversion_type2 == "L"):
        return gallons_to_liters(value)
    elif (conversion_type1 == "milliliters" or conversion_type1 == "mL") and (conversion_type2 == "fluid ounces" or conversion_type2 == "fl oz"):
        return milliliters_to_fluid_ounces(value)
    elif (conversion_type1 == "fluid ounces" or conversion_type1 == "fl oz") and (conversion_type2 == "milliliters" or conversion_type2 == "mL"):
        return fluid_ounces_to_milliliters(value)
    elif (conversion_type1 == "cups" or conversion_type1 == "c") and (conversion_type2 == "milliliters" or conversion_type2 == "mL"):
        return cups_to_milliliters(value)
    elif (conversion_type1 == "milliliters" or conversion_type1 == "mL") and (conversion_type2 == "cups" or conversion_type2 == "c"):
        return milliliters_to_cups(value)
    elif (conversion_type1 == "pints" or conversion_type1 == "pt") and (conversion_type2 == "liters" or conversion_type2 == "L"):
        return pints_to_liters(value)
    elif (conversion_type1 == "liters" or conversion_type1 == "L") and (conversion_type2 == "pints" or conversion_type2 == "pt"):
        return liters_to_pints(value)
    elif (conversion_type1 == "quarts" or conversion_type1 == "qt") and (conversion_type2 == "liters" or conversion_type2 == "L"):
        return quarts_to_liters(value)
    elif (conversion_type1 == "liters" or conversion_type1 == "L") and (conversion_type2 == "quarts" or conversion_type2 == "qt"):
        return liters_to_quarts(value)
    elif (conversion_type1 == "cups" or conversion_type1 == "c") and (conversion_type2 == "quarts" or conversion_type2 == "qt"):
        return cups_to_quarts(value)
    elif (conversion_type1 == "quarts" or conversion_type1 == "qt") and (conversion_type2 == "cups" or conversion_type2 == "c"):
        return quarts_to_cups(value)
    
    # Time conversions
    elif (conversion_type1 == "seconds" or conversion_type1 == "s") and (conversion_type2 == "minutes" or conversion_type2 == "min"):
        return seconds_to_minutes(value)
    elif (conversion_type1 == "minutes" or conversion_type1 == "min") and (conversion_type2 == "seconds" or conversion_type2 == "s"):
        return minutes_to_seconds(value)
    elif (conversion_type1 == "hours" or conversion_type1 == "hr") and (conversion_type2 == "minutes" or conversion_type2 == "min"):
        return hours_to_minutes(value)
    elif (conversion_type1 == "minutes" or conversion_type1 == "min") and (conversion_type2 == "hours" or conversion_type2 == "hr"):
        return minutes_to_hours(value)
    elif (conversion_type1 == "days" or conversion_type1 == "d") and (conversion_type2 == "hours" or conversion_type2 == "hr"):
        return days_to_hours(value)
    elif (conversion_type1 == "hours" or conversion_type1 == "hr") and (conversion_type2 == "days" or conversion_type2 == "d"):
        return hours_to_days(value)
    elif (conversion_type1 == "weeks" or conversion_type1 == "w") and (conversion_type2 == "days" or conversion_type2 == "d"):
        return weeks_to_days(value)
    elif (conversion_type1 == "days" or conversion_type1 == "d") and (conversion_type2 == "weeks" or conversion_type2 == "w"):
        return days_to_weeks(value)
    elif (conversion_type1 == "months" or conversion_type1 == "mo") and (conversion_type2 == "days" or conversion_type2 == "d"):
        return months_to_days(value)
    elif (conversion_type1 == "days" or conversion_type1 == "d") and (conversion_type2 == "months" or conversion_type2 == "mo"):
        return days_to_months(value)
    elif (conversion_type1 == "years" or conversion_type1 == "y") and (conversion_type2 == "days" or conversion_type2 == "d"):
        return years_to_days(value)
    elif (conversion_type1 == "days" or conversion_type1 == "d") and (conversion_type2 == "years" or conversion_type2 == "y"):
        return days_to_years(value)
    elif (conversion_type1 == "weeks" or conversion_type1 == "w") and (conversion_type2 == "months" or conversion_type2 == "mo"):
        return weeks_to_months(value)
    elif (conversion_type1 == "months" or conversion_type1 == "mo") and (conversion_type2 == "weeks" or conversion_type2 == "w"):
        return months_to_weeks(value)
    elif (conversion_type1 == "years" or conversion_type1 == "y") and (conversion_type2 == "months" or conversion_type2 == "mo"):
        return years_to_months(value)
    elif (conversion_type1 == "months" or conversion_type1 == "mo") and (conversion_type2 == "years" or conversion_type2 == "y"):
        return months_to_years(value)
    elif (conversion_type1 == "weeks" or conversion_type1 == "w") and (conversion_type2 == "years" or conversion_type2 == "y"):
        return weeks_to_years(value)
    elif (conversion_type1 == "years" or conversion_type1 == "y") and (conversion_type2 == "weeks" or conversion_type2 == "w"):
        return years_to_weeks(value)
    elif (conversion_type1 == "seconds" or conversion_type1 == "s") and (conversion_type2 == "hours" or conversion_type2 == "hr"):
        return seconds_to_hours(value)
    elif (conversion_type1 == "hours" or conversion_type1 == "hr") and (conversion_type2 == "seconds" or conversion_type2 == "s"):
        return hours_to_seconds(value)
    
    elif (conversion_type1 == "minutes" or conversion_type1 == "min") and (conversion_type2 == "hours" or conversion_type2 == "hr"):
        return minutes_to_hours(value)
    elif (conversion_type1 == "hours" or conversion_type1 == "hr") and (conversion_type2 == "minutes" or conversion_type2 == "min"):
        return hours_to_minutes(value)
    elif (conversion_type1 == "seconds" or conversion_type1 == "s") and (conversion_type2 == "days" or conversion_type2 == "d"):
        return seconds_to_days(value)
    elif (conversion_type1 == "days" or conversion_type1 == "d") and (conversion_type2 == "seconds" or conversion_type2 == "s"):
        return days_to_seconds(value)
    elif (conversion_type1 == "minutes" or conversion_type1 == "min") and (conversion_type2 == "days" or conversion_type2 == "d"):
        return minutes_to_days(value)
    elif (conversion_type1 == "days" or conversion_type1 == "d") and (conversion_type2 == "minutes" or conversion_type2 == "min"):
        return days_to_minutes(value)
    elif (conversion_type1 == "seconds" or conversion_type1 == "s") and (conversion_type2 == "weeks" or conversion_type2 == "w"):
        return seconds_to_weeks(value)
    elif (conversion_type1 == "weeks" or conversion_type1 == "w") and (conversion_type2 == "seconds" or conversion_type2 == "s"):
        return weeks_to_seconds(value)
    elif (conversion_type1 == "minutes" or conversion_type1 == "min") and (conversion_type2 == "weeks" or conversion_type2 == "w"):
        return minutes_to_weeks(value)
    elif (conversion_type1 == "weeks" or conversion_type1 == "w") and (conversion_type2 == "minutes" or conversion_type2 == "min"):
        return weeks_to_minutes(value)
    elif (conversion_type1 == "seconds" or conversion_type1 == "s") and (conversion_type2 == "months" or conversion_type2 == "mo"):
        return seconds_to_months(value)
    elif (conversion_type1 == "months" or conversion_type1 == "mo") and (conversion_type2 == "seconds" or conversion_type2 == "s"):
        return months_to_seconds(value)
    elif (conversion_type1 == "minutes" or conversion_type1 == "min") and (conversion_type2 == "months" or conversion_type2 == "mo"):
        return minutes_to_months(value)
    elif (conversion_type1 == "months" or conversion_type1 == "mo") and (conversion_type2 == "minutes" or conversion_type2 == "min"):
        return months_to_minutes(value)
    elif (conversion_type1 == "seconds" or conversion_type1 == "s") and (conversion_type2 == "years" or conversion_type2 == "y"):
        return seconds_to_years(value)
    elif (conversion_type1 == "years" or conversion_type1 == "y") and (conversion_type2 == "seconds" or conversion_type2 == "s"):
        return years_to_seconds(value)
    elif (conversion_type1 == "minutes" or conversion_type1 == "min") and (conversion_type2 == "years" or conversion_type2 == "y"):
        return minutes_to_years(value)

    # 'Nerd' conversions (placeholder for future implementations)

    # Add any additional conversions here as needed
    else:
        raise ValueError(f"Conversion from {conversion_type1} to {conversion_type2} is not supported.")
    
def help() -> None:
    """Display help information for the unit converter."""
    print("\nhere is the list of available conversions:")
    print("\tLength: ")
    print("\t\tinches(in), centimeters(cm), feet(ft), meters(m), yards(yd), miles(mi), kilometers(km)")
    print("\tWeight: ")
    print("\t\tpounds(lb), kilograms(kg), ounces(oz), grams(g), tons(t)")
    print("\tTemperature: ")
    print("\t\tCelsius(C), Fahrenheit(F), Kelvin(K)")
    print("\tVolume: ")
    print("\t\tliters(L), gallons(G), milliliters(mL), fluid ounces(oz), cups(c), pints(pt), quarts(qt)")
    print("\tTime: ")
    print("\t\tseconds(s), minutes(min), hours(h), days(d), weeks(w), months(mo), years(y)\n")

def conversion_loop(start_or_end:str, conversion_types) -> str:
    while True:
        try:
            conversion_type = input(f"choose your {start_or_end} conversion type: ")
            if conversion_type.lower() in ["help", "h"]:
                help()
                raise ValueError
            if conversion_type not in conversion_types:
                print(f"\tinvalid conversion type: {conversion_type}. please choose from the available types.")
                raise ValueError
            return conversion_type
        except ValueError:
            continue
    
def value_loop() -> float:
    """Loop to get a valid numeric value from the user."""
    while True:
        try:
            value = float(input("enter the value to convert: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

#-----------------------------------------------------------#
#               main function       
#-----------------------------------------------------------#

def main() -> None:

    print("\nwelcome to the unit converter!")
    print("type 'help' or 'h' for a list of available conversions.")
    print("conversion types are case-sensitive.\n")

    conversion_types = [
        # full names for the conversion types
        "inches", "centimeters", "feet", "meters", "yards", "miles", "kilometers",
        "pounds", "kilograms", "ounces", "grams", "tons",
        "Celsius", "Fahrenheit", "Kelvin",
        "liters", "gallons", "milliliters", "fluid ounces", "cups", "pints", "quarts",
        "seconds", "minutes", "hours", "days", "weeks", "months", "years",
        
        # abbreviations for the conversion types
        "in", "cm", "ft", "m", "yd", "mi", "km",
        "lb", "kg", "oz", "g", "tn",
        "C", "F", "K",
        "L", "gal", "mL", "fl oz", "c", "pt", "qt",
        "s", "min", "hr", "d", "w", "mo", "y"
    ]

    conversion_type1 = conversion_loop("starting", conversion_types)
    conversion_type2 = conversion_loop("ending", conversion_types)

    # Check if the conversion types are the same
    if conversion_type1 == conversion_type2:
        print(f"\t{conversion_type1} is the same as {conversion_type2}. No conversion needed.")
        return
    
    value = value_loop()        
    result = convert_units(conversion_type1, conversion_type2, value)

    print(f"{value} {conversion_type1} is equal to {result} {conversion_type2}\n")

if __name__ == "__main__":
    main()