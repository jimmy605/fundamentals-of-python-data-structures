# 6.
def payroll_department():
    """Write a program that inputs a filename from the user and prints a report to the terminal of the wages paid to the employees for the given period. The report should be in tabular format with the appropriate header. Each line should contain an employee’s name, the hours worked, and the wages paid for that period."""

    # Same syntax as we use a work 210626 year:month:day
    date = input('Enter the week ending date: ')
    new_file = open(f'{date}.txt', 'w')

    # Add the header to the file
    new_file.write(f'    Last name        Wage        Hours Worked\n')

    while True:
        # Input from the user
        last_name = input('Enter workers last name: ')
        hourly_wage = float(input('Enter the workers hourly wage: '))
        hours_worked = input('Enter the workers hours worked: ')
        wages_paid = float(hourly_wage) * float(hours_worked)

        new_file.write(
            f'{last_name:^18}{wages_paid:^10,.2f}{hours_worked:^20}\n')

        next_user = input('Do you wish to enter more data (Y/N): ')
        if next_user not in ['y', 'yes', 'Y', 'YES']:
            new_file.close()
            break


payroll_department()
