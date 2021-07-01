"""8. Write a program that allows the user to navigate through the lines of text in a file. The program prompts the user for a filename and inputs the lines of text into a list. The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits. Otherwise, the program prints the line associated with that number."""

def file_to_list():
    """Ask user for a filename and inputs the lines of text into a list which needs to be returned."""
    # Ask the user for the filename and open it.
    file = open(input('Enter the filename: '), 'r')
    
    return [line.strip() for line in file]

# print(file_to_list())

def return_line():
    """The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits. Otherwise, the program prints the line associated with that number."""
    file_lines = file_to_list() # Returns a list 
    total_lines = len(file_lines) - 1 # Returns the length of the list

    # Print the total line numbers for the user
    print(f'the total lines in this file is {total_lines}')
    
    while True:
        # Prompt the user for a line number and print it
        user_line = int(input('What line number do you want: '))
        
        if user_line in list(range(1, total_lines)):
            print(file_lines[user_line])
        
        # Prompt user to continue or break
        print_more = input('Continue to print more lines: ')
        if print_more not in ['y', 'yes', 'Y', 'YES']:
            break 

return_line()