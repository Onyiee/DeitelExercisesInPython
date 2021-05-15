# 5.16 (Bar Chart Printing Program) One interesting application of computers is to display
# graphs and bar charts. Write an application that reads five numbers between 1 and 30. For each
# number that’s read, your program should display the same number of adjacent asterisks.
# For example, if your program reads the number 7, it should display *******. Display the bars of asterisks after
# you read all five numbers.

def display_bar_chart(list_of_numbers):
    for number in list_of_numbers:
        new_list = number * '*'
        print(new_list)


numbers = [2, 3, 4, 5, 6]
display_bar_chart(numbers)
