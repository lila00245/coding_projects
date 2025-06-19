
#-----------------------------------------------------------#
#               length conversion functions                 #        
#-----------------------------------------------------------#
# includes:                                                 #                    
#    - inches, centimeters, feet,                           #  
#    - meters, yards, miles, kilometers                     #    
#-----------------------------------------------------------#

def inches_to_centimeters(inches: float) -> float:
    """Convert inches to centimeters."""
    return inches * 2.54

def centimeters_to_inches(centimeters: float) -> float:
    """Convert centimeters to inches."""
    return centimeters / 2.54

def feet_to_meters(feet: float) -> float:
    """Convert feet to meters."""
    return feet * 0.3048

def meters_to_feet(meters: float) -> float:
    """Convert meters to feet."""
    return meters / 0.3048

def yards_to_meters(yards: float) -> float:
    """Convert yards to meters."""
    return yards * 0.9144

def meters_to_yards(meters: float) -> float:
    """Convert meters to yards."""
    return meters / 0.9144

def miles_to_kilometers(miles: float) -> float:
    """Convert miles to kilometers."""
    return miles * 1.60934

def kilometers_to_miles(kilometers: float) -> float:
    """Convert kilometers to miles."""
    return kilometers / 1.60934 

def feet_to_inches(feet: float) -> float:
    """Convert feet to inches."""
    return feet * 12

def inches_to_feet(inches: float) -> float:
    """Convert inches to feet."""
    return inches / 12

def yards_to_feet(yards: float) -> float:
    """Convert yards to feet."""
    return yards * 3

def feet_to_yards(feet: float) -> float:
    """Convert feet to yards."""
    return feet / 3

def miles_to_feet(miles: float) -> float:
    """Convert miles to feet."""
    return miles * 5280

def feet_to_miles(feet: float) -> float:
    """Convert feet to miles."""
    return feet / 5280

def kilometers_to_feet(kilometers: float) -> float:
    """Convert kilometers to feet."""
    return kilometers * 3280.84

def feet_to_kilometers(feet: float) -> float:
    """Convert feet to kilometers."""
    return feet / 3280.84

def yards_to_miles(yards: float) -> float:
    """Convert yards to miles."""
    return yards / 1760

def miles_to_yards(miles: float) -> float:
    """Convert miles to yards."""
    return miles * 1760

def kilometers_to_yards(kilometers: float) -> float:
    """Convert kilometers to yards."""
    return kilometers * 1093.61

def yards_to_kilometers(yards: float) -> float:
    """Convert yards to kilometers."""
    return yards / 1093.61




#-----------------------------------------------------------#
#               weight conversion functions                 #
#-----------------------------------------------------------#
# includes:                                                 #
#    - pounds, kilograms, ounces,                           #
#    - grams, tons                                          #
#-----------------------------------------------------------#

def pounds_to_kilograms(pounds: float) -> float:
    """Convert pounds to kilograms."""
    return pounds * 0.45359237

def kilograms_to_pounds(kilograms: float) -> float:
    """Convert kilograms to pounds."""
    return kilograms / 0.45359237

def ounces_to_grams(ounces: float) -> float:
    """Convert ounces to grams."""
    return ounces * 28.3495

def grams_to_ounces(grams: float) -> float:
    """Convert grams to ounces."""
    return grams / 28.3495

def tons_to_kilograms(tons: float) -> float:
    """Convert tons to kilograms."""
    return tons * 907.18474

def kilograms_to_tons(kilograms: float) -> float:
    """Convert kilograms to tons."""
    return kilograms / 907.18474

#-----------------------------------------------------------#
#               temperature conversion functions            #
#-----------------------------------------------------------#
# includes:                                                 #
#    - Celsius, Fahrenheit, Kelvin                          #
#-----------------------------------------------------------#

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin: float) -> float:
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


#-----------------------------------------------------------#
#               volume conversion functions                 #    
#-----------------------------------------------------------#
# includes:                                                 #
#    - liters, gallons, milliliters,                        #   
#    - fluid ounces, cups, pints, quarts                    #
#-----------------------------------------------------------#

def liters_to_gallons(liters: float) -> float:
    """Convert liters to gallons."""
    return liters * 0.264172

def gallons_to_liters(gallons: float) -> float:
    """Convert gallons to liters."""
    return gallons / 0.264172

def milliliters_to_fluid_ounces(milliliters: float) -> float:
    """Convert milliliters to fluid ounces."""
    return milliliters * 0.033814

def fluid_ounces_to_milliliters(fluid_ounces: float) -> float:
    """Convert fluid ounces to milliliters."""
    return fluid_ounces / 0.033814

def cups_to_milliliters(cups: float) -> float:
    """Convert cups to milliliters."""
    return cups * 236.588

def milliliters_to_cups(milliliters: float) -> float:
    """Convert milliliters to cups."""
    return milliliters / 236.588

def pints_to_liters(pints: float) -> float:
    """Convert pints to liters."""
    return pints * 0.473176

def liters_to_pints(liters: float) -> float:
    """Convert liters to pints."""
    return liters / 0.473176

def quarts_to_liters(quarts: float) -> float:
    """Convert quarts to liters."""
    return quarts * 0.946353

def liters_to_quarts(liters: float) -> float:
    """Convert liters to quarts."""
    return liters / 0.946353

def cups_to_quarts(cups: float) -> float:
    """Convert cups to quarts."""
    return cups / 4

def quarts_to_cups(quarts: float) -> float:
    """Convert quarts to cups."""
    return quarts * 4

#-----------------------------------------------------------#
#               time conversion functions                   #
#-----------------------------------------------------------#
# includes:                                                 #
#    - seconds, minutes, hours, days                        #
#    - weeks, months, years                                 #
#-----------------------------------------------------------#

def seconds_to_minutes(seconds: float) -> float:
    """Convert seconds to minutes."""
    return seconds / 60

def minutes_to_seconds(minutes: float) -> float:
    """Convert minutes to seconds."""
    return minutes * 60

def hours_to_minutes(hours: float) -> float:
    """Convert hours to minutes."""
    return hours * 60

def minutes_to_hours(minutes: float) -> float:
    """Convert minutes to hours."""
    return minutes / 60

def days_to_hours(days: float) -> float:
    """Convert days to hours."""
    return days * 24

def hours_to_days(hours: float) -> float:
    """Convert hours to days."""
    return hours / 24

def weeks_to_days(weeks: float) -> float:
    """Convert weeks to days."""
    return weeks * 7

def days_to_weeks(days: float) -> float:
    """Convert days to weeks."""
    return days / 7

def months_to_days(months: float) -> float:
    """Convert months to days."""
    return months * 30.44  # Average days in a month

def days_to_months(days: float) -> float:
    """Convert days to months."""
    return days / 30.44  # Average days in a month

def years_to_days(years: float) -> float:
    """Convert years to days."""
    return years * 365.25  # Average days in a year

def days_to_years(days: float) -> float:
    """Convert days to years."""
    return days / 365.25  # Average days in a year

def weeks_to_months(weeks: float) -> float:
    """Convert weeks to months."""
    return weeks / 4.34524  # Average weeks in a month

def months_to_weeks(months: float) -> float:
    """Convert months to weeks."""
    return months * 4.34524  # Average weeks in a month

def hours_to_years(hours: float) -> float:
    """Convert hours to years."""
    return hours / (24 * 365.25)  # Average hours in a year

def years_to_hours(years: float) -> float:
    """Convert years to hours."""
    return years * (24 * 365.25)  # Average hours in a year

def minutes_to_years(minutes: float) -> float:
    """Convert minutes to years."""
    return minutes / (60 * 24 * 365.25)  # Average minutes in a year

def years_to_minutes(years: float) -> float:
    """Convert years to minutes."""
    return years * (60 * 24 * 365.25)  # Average minutes in a year

def seconds_to_years(seconds: float) -> float:
    """Convert seconds to years."""
    return seconds / (60 * 60 * 24 * 365.25)  # Average seconds in a year

def years_to_seconds(years: float) -> float:
    """Convert years to seconds."""
    return years * (60 * 60 * 24 * 365.25)  # Average seconds in a year

def weeks_to_years(weeks: float) -> float:
    """Convert weeks to years."""
    return weeks / 52.1775  # Average weeks in a year

def years_to_weeks(years: float) -> float:
    """Convert years to weeks."""
    return years * 52.1775  # Average weeks in a year

def weeks_to_hours(weeks: float) -> float:
    """Convert weeks to hours."""
    return weeks * 168  # 24 hours * 7 days

def hours_to_weeks(hours: float) -> float:
    """Convert hours to weeks."""
    return hours / 168  # 24 hours * 7 days

def days_to_years(days: float) -> float:
    """Convert days to years."""
    return days / 365.25  # Average days in a year

def years_to_days(years: float) -> float:
    """Convert years to days."""
    return years * 365.25  # Average days in a year

def days_to_hours(days: float) -> float:
    """Convert days to hours."""
    return days * 24  # 24 hours in a day

def hours_to_days(hours: float) -> float:
    """Convert hours to days."""
    return hours / 24  # 24 hours in a day

def days_to_minutes(days: float) -> float:
    """Convert days to minutes."""
    return days * 1440  # 24 hours * 60 minutes

def minutes_to_days(minutes: float) -> float:
    """Convert minutes to days."""
    return minutes / 1440  # 24 hours * 60 minutes

def weeks_to_minutes(weeks: float) -> float:
    """Convert weeks to minutes."""
    return weeks * 10080  # 7 days * 24 hours * 60 minutes

def minutes_to_weeks(minutes: float) -> float:
    """Convert minutes to weeks."""
    return minutes / 10080  # 7 days * 24 hours * 60 minutes

def seconds_to_minutes(seconds: float) -> float:
    """Convert seconds to minutes."""
    return seconds / 60  # 60 seconds in a minute

def minutes_to_seconds(minutes: float) -> float:
    """Convert minutes to seconds."""
    return minutes * 60  # 60 seconds in a minute

def seconds_to_hours(seconds: float) -> float:
    """Convert seconds to hours."""
    return seconds / 3600  # 3600 seconds in an hour

def hours_to_seconds(hours: float) -> float:
    """Convert hours to seconds."""
    return hours * 3600  # 3600 seconds in an hour

def seconds_to_days(seconds: float) -> float:
    """Convert seconds to days."""
    return seconds / 86400  # 86400 seconds in a day

def days_to_seconds(days: float) -> float:
    """Convert days to seconds."""
    return days * 86400  # 86400 seconds in a day

def seconds_to_weeks(seconds: float) -> float:
    """Convert seconds to weeks."""
    return seconds / 604800  # 604800 seconds in a week

def weeks_to_seconds(weeks: float) -> float:
    """Convert weeks to seconds."""
    return weeks * 604800  # 604800 seconds in a week

def months_to_seconds(months: float) -> float:
    """Convert months to seconds."""
    return months * 2629800  # Average seconds in a month (30.44 days)

def seconds_to_months(seconds: float) -> float:
    """Convert seconds to months."""
    return seconds / 2629800  # Average seconds in a month (30.44 days)

def months_to_hours(months: float) -> float:
    """Convert months to hours."""
    return months * 730.48  # Average hours in a month (30.44 days)

def hours_to_months(hours: float) -> float:
    """Convert hours to months."""
    return hours / 730.48  # Average hours in a month (30.44 days)

def months_to_minutes(months: float) -> float:
    """Convert months to minutes."""
    return months * 43829.1  # Average minutes in a month (30.44 days)

def minutes_to_months(minutes: float) -> float:
    """Convert minutes to months."""
    return minutes / 43829.1  # Average minutes in a month (30.44 days)

def months_to_days(months: float) -> float:
    """Convert months to days."""
    return months * 30.44  # Average days in a month

def days_to_months(days: float) -> float:
    """Convert days to months."""
    return days / 30.44  # Average days in a month

def years_to_seconds(years: float) -> float:
    """Convert years to seconds."""
    return years * 31557600  # Average seconds in a year (365.25 days)

def seconds_to_years(seconds: float) -> float:
    """Convert seconds to years."""
    return seconds / 31557600  # Average seconds in a year (365.25 days)

def years_to_minutes(years: float) -> float:
    """Convert years to minutes."""
    return years * 525949.2  # Average minutes in a year (365.25 days)

def minutes_to_years(minutes: float) -> float:
    """Convert minutes to years."""
    return minutes / 525949.2  # Average minutes in a year (365.25 days)

def months_to_years(months: float) -> float:
    """Convert months to years."""
    return months / 12  # 12 months in a year

def years_to_months(years: float) -> float:
    """Convert years to months."""
    return years * 12  # 12 months in a year

#-----------------------------------------------------------#
#               'nerd' conversion functions                 #
#-----------------------------------------------------------#
# includes:                                                 #
#    - bytes,              
#-----------------------------------------------------------#

## to be continued...