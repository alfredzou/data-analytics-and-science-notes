from math import pi


def circle_area(r):
    if type(r) not in (int, float):
        raise TypeError("A circle radius must be an integer or float.")
    if r < 0:
        raise ValueError("A circle radius cannot be negative.")
    return pi * (r ** 2)
