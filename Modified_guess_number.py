# 6.31 (Guess the Number Modification) Modify the program of Exercise 6.30 to count the number of guesses
# the player makes. If the number is 10 or fewer, display Either you know the secret
# or you got lucky! If the player guesses the number in 10 tries, display Aha! You know the secret!
# If the player makes more than 10 guesses, display You should be able to do better! Why should it
# take no more than 10 guesses? Well, with each “good guess,” the player should be able to eliminate
# half of the numbers, then half of the remaining numbers, and so on.

from random import randint

count = 1


def ten_or_less_message(count):
    if count == 10:
        return "Aha! You know the secret!"
    random_message = randint(1, 2)
    if random_message == 1:
        return "You got lucky!"
    if random_message == 2:
        return "You know the secret"


def greater_than_ten_message():
    return "You should be able to do better!"


def modified_guess_game(guessed_number):
    global count
    random_number = randint(1, 10)
    guessed_number = int(guessed_number)
    if guessed_number == random_number and count <= 10:
        print(ten_or_less_message(count))
    if guessed_number == random_number and count > 10:
        print(greater_than_ten_message())
    count += 1
    if guessed_number != random_number:
        modified_guess_game(input("Guess a number between 1 and 10: "))


print(modified_guess_game(input("Guess a number between 1 and 10: ")))
