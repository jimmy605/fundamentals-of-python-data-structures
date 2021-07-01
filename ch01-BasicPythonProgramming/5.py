""" 
5.
- 10% down payment
- 12% annual interest rate
- 5% monthly payments of the list purchase price minus the down payment

Need headers for the payment schedule for the lifetime of the loan. Each row should contain
- The month number (beggining with 1)
- The current total balance owed
- The interest owed for that month
- The amount of principal owed for that month
- The payment for that month
- The balance remaining after payment


"""


def tidBit():
    # Purchase price
    purchase_price = float(input('Enter the purchase price: '))

    # Constant variables
    DOWN_PAYMENT = 0.10
    ANNUAL_INTEREST = 0.12
    MONTHLY_PAYMENTS = purchase_price * 0.9 * 0.05

    # Variables
    month = 1
    total_balance = purchase_price - DOWN_PAYMENT

    # Print the header for the program
    header = ['Month', 'Total Balance', 'Interest',
              'Principal', 'Payment', 'Remaining']
    print(
        f'{header[0]:^6}{header[1]:^16}{header[2]:^12}{header[3]:^14}{header[4]:^10}{header[5]:^12}')

    # While loop that's true if total_balance > 0
    while total_balance > 0:
        interest_owed = total_balance * ANNUAL_INTEREST / 12
        principal_owed = MONTHLY_PAYMENTS

        if principal_owed > total_balance:
            principal_owed = total_balance

        print(f'{month:^5}{total_balance:^15,.2f}{interest_owed:^16,.2f}{principal_owed:^10,.2f}{principal_owed + interest_owed:^13,.2f}{total_balance - (principal_owed + interest_owed):^10,.2f}')

        # Update data
        total_balance -= (MONTHLY_PAYMENTS + interest_owed)
        month += 1


tidBit()
