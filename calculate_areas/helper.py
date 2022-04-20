import math


def right_triangle_area(height, base):
    height, base = float(height), float(base)
    return (height*base)/2


def equilateral_area(side):
    side = float(side)
    return math.sqrt(3)*(side**2)/4


def square_area(side):
    side = float(side)
    return side**2


def rectangle_area(height, width):
    height, width = float(height), float(width)
    return (height*width)


def trapezium_area(side1, side2, height):
    side1, side2, height = float(side1), float(side2), float(height)
    return ((side1+side2)*height)/2
