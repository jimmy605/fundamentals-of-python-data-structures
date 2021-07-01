import math

"""
1.
Write a program that takes the radius of a sphere (a floating-point number) as input and outputs the sphere’s diameter, circumference, surface area, and volume."""


def sphere_calcs():
    radius = float(input('Enter the radius of the sphere: '))

    calcs = {
        'diameter': radius * 2,
        'circumference': 2 * math.pi * radius,
        "surface area": math.pi * ((radius * 2) ** 2),
        'volume': (1.25 * math.pi) * (radius ** 3)
    }

    for k, v in calcs.items():
        print(f'{k}: {v:.3f}')

sphere_calcs()
