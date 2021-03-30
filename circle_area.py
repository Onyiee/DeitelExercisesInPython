# 6.20 (Circle Area) Write an application that prompts the user for the radius of a circle and uses
# a method called circleArea to calculate the area of the circle.

def circle_area(r):
    pi = 3.142

    area_of_circle = pi * r * r
    return area_of_circle


if __name__ == '__main__':
    r = int(input("Enter the radius of the circle: "))
    area = circle_area(r)
    print(area)
