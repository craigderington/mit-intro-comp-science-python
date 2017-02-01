#! /usr/bin/python
from math import pi, tan


def polysum(n, s):
    """
    This function should sum the area and square of the perimeter of the regular polygon.
    The function returns the sum, rounded to 4 decimal places.
    example formula: area = s**2(n) / (4 * tangent) * (180 / n)
    tan is the tangent function calculated in degrees
    :param n: number of polygon sides
    :param s: length of the side
    :return: sum of the area in decimal
    """
    area = (0.25 * n * s**2) / tan(pi / n)
    perimeter = ((n * s) ** 2)
    total_sum = area + perimeter
    return round(total_sum, 4)


poly_area = polysum(12, 64)
print(poly_area)

# 12, 64 = 635683.4403




