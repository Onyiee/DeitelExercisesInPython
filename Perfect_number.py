# (Perfect Numbers) An integer number is said to be a perfect number if its factors, including
# 1 (but not the number itself), sum to the number. For example, 6 is a perfect number, because 6 =
# 1 + 2 + 3. Write a method isPerfect that determines whether parameter number is a perfect number.
# Use this method in an application that displays all the perfect numbers between 1 and 1000. Display
# the factors of each perfect number to confirm that the number is indeed perfect. Challenge the
# computing power of your computer by testing numbers much larger than 1000. Display the results.
number = 0


def perfect_numbers(number):
    sum_of_factors = 0

    for x in range(1, number):
        if number % x == 0:
            sum_of_factors = x + sum_of_factors

    if sum_of_factors == number:
        return True
    else:
        return False


num = int(input("Enter a number: "))
ans = perfect_numbers(num)
print(ans)
