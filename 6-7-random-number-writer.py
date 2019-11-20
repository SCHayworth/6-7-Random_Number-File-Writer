# 6-7 Random Number File Writer
# Shaun Hayworth
# CIS 2
# 11-19-2019
# Source code and revision history are available at
# https://github.com/SCHayworth/6-7-Random-Number-File-Writer

# Generates a text file with a user-supplied amount of random integers between
# 1 and 500.

# Import the random module
import random


def main():
    '''Mainline program logic
    '''
    # Open or create a file called random.txt in write mode.
    file_name = open('random.txt', 'w')

    # Prompt user for the amount of random numbers to write to the file.
    number_quantity = int(input('How many numbers would you like to generate? '))

    # Generate the supplied amount of random integers between 1 and 500 and
    # write them to random.txt.
    for number in range(1, number_quantity +1):
        # Generate a random integer from 1-500 and convert it to a string.
        random_int = random.randint(1, 500)
        new_num = f'{random_int}\n'

        # Append the random number to the random.txt file.
        file_name.write(new_num)

    # Close the random.txt file
    file_name.close()

    # TESTING - Call the count_numbers() function.
    count_numbers()


def count_numbers():
    '''Counts the number of lines in a text file. Use for testing the main()
    function.
    '''
    # Open the random.txt file in read mode.
    test_file = open('random.txt', 'r')

    # Initialize an accumulator to count the number of items in the file.
    test_items = 0

    # Read the first item in the file.
    current_item = test_file.readline()

    # Read each line until the end of the file.
    while current_item != '':
        # increment the accumulator and read the next line in the file.
        test_items += 1
        current_item = test_file.readline()


    # Close the random.txt file.
    test_file.close()

    # Display the value of the accumulator.
    print(f'There are {test_items} numbers in this file.')

# Call the main() function
main()
