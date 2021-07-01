import random 

# User inputs the number to be guessed and the lower/upper bounds that can be guessed
# Computer does the guessing but need to think about allowing for the change in the lower and upper bounds
# User to provide hints such as "<" or ">" and "=" when the computer guesses correctly
# Track the number of guesses the computer takes
# Output "You're cheating!" if the computer takes longer than the maximum guesses needed

"""
1. Review the while loop. Think about the function returns for the elif and else. Think that's the only outstanding stuff plus refactoring.
"""

def main():
    # User enters the data
    answer, lower, upper = user_inputs()
    
    # Computer takes a guess
    guess = computer_guess(lower, upper)
    
    while True:
        # Print out answer/guess
        check_guess(answer, guess)
        
        # User input "<", ">" or "=" depending on the guess
        tbc = input('"<", ">" or "=":')
        
        if tbc == '=':
            print('Congrats you got it correct.')
            break 
        elif tbc == '<':
            print(f'Incorrect, the answer is lower than {guess}')
            print(lower, guess - 1)
            guess = computer_guess(lower, guess - 1)
            
        else:
            print(f'Incorrect, the answer is higher than {guess}')
            print(guess + 1, upper)
            guess = computer_guess(guess + 1, upper)


def user_inputs():
    """User inputs the number to be guessed and the lower/upper bounds that can be guessed. returning a list of 3 elements"""
    
    lower_bound = int(input('Enter the lower bound: '))
    upper_bound = int(input('Enter the upper bound: '))
    
    guess_num = int(input('Enter the number for the computer to guess: '))
    
    while guess_num < lower_bound or guess_num > upper_bound:
        guess_num = int(input(f'Enter a number between {lower_bound} - {upper_bound} for the computer to guess: '))

    return [guess_num, lower_bound, upper_bound]


def computer_guess(lower, upper):
    """Take the lower and upper bound numbers and return the number closest to the middle. This is the computers guess"""

    # return (upper - lower) // 2 + 1
    return (lower + upper) // 2


def check_guess(answer, guess):
    """Takes the list data from user_inputs()"""
    # Print out the answer for the user plus the computers guess so the user can review
    print(f'The answer is {answer} and the computer guessed {guess}')


if __name__ == '__main__':
    main()
