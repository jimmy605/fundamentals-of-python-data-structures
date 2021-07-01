"""
2.
An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee’s total weekly pay.
"""


def weekly_pay():
    HOURLY_RATE = float(input('Enter the hourly rate: '))

    reg_hrs = float(input('Enter total regular hours worked: '))
    over_hrs = float(input('Enter total overtime hours worked: '))

    pay = (reg_hrs + (over_hrs * 1.5)) * HOURLY_RATE

    return f'Your total weekly pay is ${pay:,.2f}'


print(weekly_pay())
