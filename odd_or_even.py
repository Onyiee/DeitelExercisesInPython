# 6.17 (Even or Odd) Write a method isEven that uses the remainder operator (%) to determine
# whether an integer is even. The method should take an integer argument and return true if
# the integer is even and false otherwise.
#  Incorporate this method into an application that inputs a sequence of integers (one at a time)
#  and determines whether each is even or odd.


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False



if __name__ == '__main__':
    number = 1

    while number != -1:
        try:
            number = int(input("Enter a number: "))
            ans = is_even(number)
            if ans == True:
                print("True. \n It is even ")
            else:
                print("False. \n It is odd")
        except ValueError:
            print("You need to enter a number")
