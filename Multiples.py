# 6.16 (Multiples) Write a method isMultiple that determines, for a pair of integers, whether the
# second integer is a multiple of the first. The method should take two integer arguments and return
# true if the second is a multiple of the first and false otherwise. [Hint: Use the remainder operator.]
# Incorporate this method into an application that inputs a series of pairs of integers (one pair at a
# time) and determines whether the second value in each pair is a multiple of the first.

def is_multiple():
    first_number = int(input("Enter an integer: "))
    second_number = int(input("Enter another number: "))
    if second_number % first_number == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_multiple())
