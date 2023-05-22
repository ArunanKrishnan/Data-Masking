import pandas as pd
import numpy as np
import random
import math
import soundex
df=pd.read_excel(r"C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx")


# Define function to mask all digits in the phone number columndef mask_consonants(phone_number):
def mask_consonants(phone_number):
    if not isinstance(phone_number, str):
        phone_number = str(phone_number)
    
    masked_number = ''
    for c in phone_number:
        if c.isalpha() and c.lower() not in 'aeiou':
            masked_number += 'X'
        else:
            masked_number += c
    
    return masked_number

    
    
#df['Employee ID'] = df['Employee ID'].apply(mask_consonants)
#print(df['Employee ID'])
def mask_reversal(phone_number):
    # Reverse the phone number
    reversed_number = str(phone_number)[::-1]
    # Determine the number of digits to mask
    num_masked_digits = random.randint(1, len(reversed_number) - 1)
    # Determine the positions of the masked digits
    masked_positions = random.sample(range(len(reversed_number)), num_masked_digits)
    # Mask the digits at the chosen positions with X's or *'s
    masked_number = ''.join(['X' if i in masked_positions else digit for i, digit in enumerate(reversed_number)])
    return masked_number[::-1]
    # Reverse the masked number and return it
  
def mask_soundex(phone_number):
    soundex_codes = {
        '0': 'Z',
        '1': 'S',
        '2': 'T',
        '3': 'T',
        '4': 'F',
        '5': 'F',
        '6': 'S',
        '7': 'S',
        '8': 'A',
        '9': 'N'
    }
    soundex_number = ''.join(soundex_codes.get(digit, '') for digit in str(phone_number) if digit.isdigit())
    masked_soundex = soundex_number[:3] + 'X' * (len(soundex_number) - 3)
    return masked_soundex


# Define function to apply randomized offset masking to a phone number
def randomized_offset_masking(phone_numbers):
    if isinstance(phone_numbers, int):  # Convert to list if input is an integer
        phone_numbers = [phone_numbers]
    masked_numbers = []
    for phone_number in phone_numbers:
        phone_number = str(phone_number)  # Convert phone number to string
        length = len(phone_number)
        offset = random.randint(0, length - 1)  # Choose random offset
        num_digits_to_mask = random.randint(1, length - offset)  # Choose random number of digits to mask
        masked_number = list(phone_number)
        for i in range(offset, offset + num_digits_to_mask):
            masked_number[i] = 'X'  # Mask selected digits with X's
        masked_numbers.append(''.join(masked_number))
    return masked_numbers
def multiply_random_middle(number):
    # Convert the number to a string
    number_str = str(number)
    updated_numbers = [] # Create an empty list to store the updated numbers
    # Check if the number has at least three digits
    if len(number_str) >= 3:
        # Extract the middle portion of the original number
        middle_portion = number_str[1:-1]
        # Multiply a random value to the middle portion
        random_value = random.randint(1, 10)  # Generate a random integer between 1 and 10
        multiplied_middle = int(middle_portion) * random_value
        # Create the updated number by concatenating the first digit, multiplied middle portion, and last digit
        updated_number = int(number_str[0] + str(multiplied_middle) + number_str[-1])
        updated_numbers.append(updated_number) # Append the updated number to the list
    return updated_numbers

# Define a function to apply the algorithm to each pin code
def extract_first_digit(number):
    extracted_digit = []
    # Convert the number to a string
    number_str = str(number)
    # Check if the number has at least four digits
    if len(number_str) >= 4:
        # Extract the first digit of the original number
        first_digit = number_str[0]
        # Extract the next three digits of the original number
        next_three_digits = number_str[1:5]
        # Create a list containing the extracted first digit and next three digits
        extracted_digits = (int(first_digit)+ int(next_three_digits))
        extracted_digit.append(extracted_digits)
        # Return the list
        return extracted_digit

def mask_pincode(pincode):
    # Convert the pincode to a string
    pincode_str = str(pincode)
    # Mask the pincode using bitwise XOR operation
    masked_chars = []
    for char in pincode_str:
        masked_char = chr(ord(char) ^ 255)
        masked_chars.append(masked_char)
    return masked_chars

# Define a function to apply the algorithm to each pin code
def remind_first_last_swap_between(number):
    # Convert the number to a string
    number_str = str(number)
    number_strs = []
    # Check if the number has at least two digits
    if len(number_str) >= 2:
        # Extract the first digit of the original number
        first_digit = number_str[0]
        # Extract the last digit of the original number
        last_digit = number_str[-1]
        # Extract the digits between the first and last digits of the original number
        between_digits = number_str[1:-1]
        # Swap the digits between the first and last digits
        swapped_digits = last_digit + between_digits + first_digit
        # Create a list containing the swapped digits
        swapped_list = [int(digit) for digit in swapped_digits]
        a=''.join(str(digit) for digit in swapped_list)
        number_strs.append(a)
        # Use join() method to concatenate digits without comma
        return number_strs

# Define a function to apply the complex algorithm to each pin code
def complex_mask_pincode(pincode):
    # Convert the pincode to a string
    pincode_str = str(pincode)
    masked_pincodes = []
    # Check if the pincode has at least five digits
    if len(pincode_str) >= 5:
        # Randomly select a position to start the masking
        start_position = random.randint(0, len(pincode_str) - 3)
        # Randomly select a position to end the masking
        end_position = random.randint(start_position + 1, len(pincode_str) - 1)
        # Extract the portion of the pincode to be masked
        portion_to_mask = pincode_str[start_position:end_position + 1]
        # Generate a random mask of 'X' characters with the same length as the portion to be masked
        mask = 'X' * len(portion_to_mask)
        # Replace the portion to be masked with the generated mask
        masked_pincode = pincode_str[:start_position] + mask + pincode_str[end_position + 1:]
        masked_pincodes.append(masked_pincode)
        return masked_pincodes


'''
def xor_with_random_and(input_file):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Initialize an empty list to store the XOR results
    xor_results = []

    # Iterate over the integers in the DataFrame
    for number in df['Employee ID']:
        # Generate a random value and perform a bitwise AND operation with the number
        random_value = random.randint(1, 1000)
        and_result = number & random_value

        # Perform the XOR operation with the AND result
        xor_result = number ^ and_result

        # Add the XOR result to the list
        xor_results.append(xor_result)

    # Return the list of XOR results
    return xor_results
df['Employee ID'] = df['Employee ID'].apply(xor_with_random_and)
print(df['Employee ID'])

def mask_employee_ids(input_file):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Generate a random power of 2
    power_of_two = 2 ** random.randint(1, 10)

    # Apply the mask to the specified column
    df['Employee ID'] = df['Employee ID'].apply(lambda x: x + power_of_two)

    # Return the masked list of employee IDs as a Python list
    return df['Employee ID'].tolist()

def modify_list_values(file_path, column_name):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Extract the values from the specified column as a list
    input_list = df[column_name].tolist()

    # Modify the list
    result_list = []
    for value in input_list:
        multiplied_digits = []
        for digit in str(value):
            multiplied_digits.append(str(int(digit) * 2))

        final_digits = []
        for i, digit in enumerate(multiplied_digits):
            if int(digit) % 2 == 0:
                final_digits.append(str(int(digit) + 1))
            else:
                final_digits.append(str(int(digit) - 1))

        final_value = int("".join(final_digits))
        result_list.append(final_value)

    # Return the modified list
    return result_list

def add_fixed_value(file_path, column_name, fixed_value):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Add the fixed value to the specified column
    df[f'Updated {column_name}'] = df[column_name] + fixed_value

    # Return the updated DataFrame
    return df

def divide_and_swap_column(file_path, column_name):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Divide the column into two halves and swap them
    numbers = df[column_name].tolist()
    length = len(numbers)
    if length % 2 == 0:
        half = length // 2
        first_half = numbers[:half]
        second_half = numbers[half:]
        swapped_numbers = second_half + first_half

        # Add the swapped column to the DataFrame
        df[f'Swapped {column_name}'] = swapped_numbers

        # Return the updated DataFrame
        return df
    else:
        print("Error: List length must be even")

def multiply_and_subtract(file_path, column_name):
    # Read the Excel file
    df = pd.read_excel(file_path)

    column_values = df[column_name]
    result_values = []
    for value in column_values:
        random_number = random.uniform(0, 1)
        result = round(value - (value * random_number))
        result_values.append(result)

    # Add the modified column to the DataFrame
    df[f'Multiplied and Subtracted {column_name}'] = pd.Series(result_values)

    # Return the output list
    return df[f'Multiplied and Subtracted {column_name}'].tolist()


def shuffle_column_numbers(column_values):
    rounded_numbers = [math.ceil(num) for num in column_values]
    indexes = list(range(len(column_values)))
    random.shuffle(indexes)
    shuffled_numbers = [rounded_numbers[index] for index in indexes]
    return shuffled_numbers
def shuffle_digits(file_path, column_name):
    df = pd.read_excel(file_path)
    column_values = df[column_name]
    result_values = []
    for value in column_values:
        digits_list = [int(digit) for digit in str(value)]
        random.shuffle(digits_list)
        result_value = int("".join(map(str, digits_list)))
        result_values.append(result_value)
    df[f'Shuffled Digits {column_name}'] = pd.Series(result_values)
    return result_values
def sub_fixed_value(file_path, column_name, fixed_value):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Add the fixed value to the specified column
    df[f'Updated {column_name}'] = df[column_name] - fixed_value

    # Return the updated DataFrame
    return df
'''