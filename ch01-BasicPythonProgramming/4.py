"""
4.
The German mathematician Gottfried Leibniz developed the following method to approximate the value of π:
π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
Write a program that allows the user to specify the number of iterations used in this approximation and displays the resulting value.
"""


def calTotal(num_iters):
    """Returns the total of the fractions for Gottfried"""
    total = 1
    sign_positive = True

    for num in range(3, num_iters + 3, 2):
        if num == 3:
            total -= 1 / 3
        elif sign_positive:
            total += 1 / num
            sign_positive = False
        else:
            total -= 1 / num
            sign_positive = True

    return f'{4 * total:.3f}'


print(calTotal(1500))
