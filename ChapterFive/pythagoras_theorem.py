# 5.21 (Pythagorean Triples) A right triangle can have sides whose lengths are all integers. The set
# of three integer values for the lengths of the sides of a right triangle is called a Pythagorean triple.
# The lengths of the three sides must satisfy the relationship that the sum of the squares of two of the
# sides is equal to the square of the hypotenuse. Write an application that displays a table of the
# Pythagorean triples for side1, side2 and the hypotenuse, all no larger than 500. Use a triple-nested
# for loop that tries all possibilities. This method is an example of “brute-force” computing. You’ll
# learn in more advanced computer science courses that for many interesting problems there’s no
# known algorithmic approach other than using sheer brute force.
import math

for side1 in range(1, 500):
    for side2 in range(1, 500):
        for hypotenuse in range(1, 500):
            if (side1 * side1) + (side2 * side2) == hypotenuse * hypotenuse:
                print(f"side1 {side1} plus side2 {side2} is  hypotenuse {hypotenuse}")
