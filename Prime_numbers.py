# 6.25 (Prime Numbers) A positive integer is prime if it’s divisible by only 1 and itself.
# For example,
# 2, 3, 5 and 7 are prime, but 4, 6, 8 and 9 are not. The number 1, by definition, is not prime.
# a) Write a method that determines whether a number is prime.
# b) Use this method in an application that determines and displays all the prime numbers
# less than 10,000. How many numbers up to 10,000 do you have to test to ensure that
# you’ve found all the primes?
# c) Initially, you might think that n/2 is the upper limit for which you must test to see
# whether a number n is prime, but you need only go as high as the square root of n. Rewrite the program
import math


def prime_numbers(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_numbers2(number):
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True


def prime_numbers3(number):
    for i in range(2, (number // 2)):
        if number % i == 0:
            return False
    return True


for i in range(2, 10000):
    if prime_numbers(i):
        print(i)
