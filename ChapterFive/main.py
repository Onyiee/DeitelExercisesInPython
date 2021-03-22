# 5.12 (Calculating the Product of Odd Integers) Write an application that calculates the product
# of the odd integers from 1 to 15

product = 1
for i in range(1, 16, 2):
    product = i * product


def product_of_odd_numbers(product):
    return product


print(product_of_odd_numbers(product))
