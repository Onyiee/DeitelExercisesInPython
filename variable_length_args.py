# 7.14 (Variable-Length Argument List) Write an application that calculates the product of a series
#         of integers that are passed to method product using a variable-length argument list.
#         Test your method with several calls, each with a different number of arguments.

def product(*args):
    product_of_integers = 1
    for _ in args:
        product_of_integers = product_of_integers * _
    return product_of_integers


