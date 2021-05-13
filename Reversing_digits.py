# 6.26 (Reversing Digits) Write a method that takes an integer value and returns the number
# with its digits reversed. For example, given the number 7631, the method should return 1367.
# Incorporate the method into an application that reads a value from the user and displays
# the result

# my_list = [7981]
#
#
# def reversing_digits(my_list):
#
#     for x in (my_list):
#         my_new_list = my_list.append(x)
#         return my_new_list


def reversing_digits():
    numbers = list(input("enter numbers: "))

    for number in numbers:

        new_list = numbers.append(number)
        print(new_list)

print(reversing_digits())







