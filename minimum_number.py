# 6.23 (Find the Minimum) Write a method minimum3 that returns the smallest of three floating
# point numbers. Use the Math.min method to implement minimum3. Incorporate the method into an
# application that reads three values from the user, determines the smallest value and displays
# the result.


def minimum3(first_number, second_number, third_number):
    if first_number < second_number and first_number < third_number:
        minimum_number = first_number
        return minimum_number
    if second_number < first_number and second_number < third_number:
        minimum_number = second_number
        return minimum_number
    if third_number < first_number and third_number < second_number:
        minimum_number = third_number
        return minimum_number


if __name__ == '__main__':
    try:
        first_number = float(input("Enter a number: "))
        second_number = float(input("Enter a second number: "))
        third_number = float(input("Enter a third number: "))
        min_number = (minimum3(first_number, second_number, third_number))
        print(f"The minimum number is {min_number}")
    except ValueError:
        print("This program accepts only numbers.Enter a number.")
