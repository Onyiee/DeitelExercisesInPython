# (Gas Mileage) Drivers are concerned with the mileage their automobiles get. One driver has
# kept track of several trips by recording the miles driven and gallons used for each tankful. Develop
# a Java application that will input the miles driven and gallons used (both as integers) for each trip.
# The program should calculate and display the miles per gallon obtained for each trip and print the
# combined miles per gallon obtained for all trips up to this point. All averaging calculations should
# produce floating-point results. Use class Scanner and sentinel-controlled repetition to obtain the
# data from the user.

def gas_mileage():
    total_miles_per_gallon = 0
    miles_driven = int(input("Enter the miles driven or -1 to quit: "))
    gallons_used = int(input("Enter the gallons used or -1 to quit: "))

    while miles_driven != -1:
        miles_per_gallon = miles_driven / gallons_used
        print(f"miles per gallon is {miles_per_gallon}")
        miles_driven = int(input("Enter the miles driven"))
        gallons_used = int(input("Enter the gallons used"))
        total_miles_per_gallon += miles_per_gallon
    print(f"The total miles per gallon is {total_miles_per_gallon}")


gas_mileage()
