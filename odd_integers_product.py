# 5.12 (Calculating the Product of Odd Integers) Write an application that calculates the product
# of the odd integers from 1 to 15.


def odd_integers_product():
    product = 1
    for number in range(1, 16):
        if number % 2 != 0:
            product = product * number
    return product

