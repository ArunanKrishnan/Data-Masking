import pandas as pd
import numpy as np
import random
import math
import soundex
df=pd.read_excel(r"C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx")


# Define function to mask all digits in the phone number columndef mask_consonants(phone_number):
def remind_first_last_swap_between(data):
    swapped_digits = []
    for value in data:
        str_value = str(value)
        first_digit = str_value[0]
        last_digit = str_value[-1]
        swapped_digits.append(last_digit + str_value[1:-1] + first_digit)
    
    # Remove spaces from swapped digits
    swapped_digits = [digit.replace(' ', '') for digit in swapped_digits]
    
    swapped_list = [int(digit) for digit in swapped_digits]
    return swapped_list

def masked_pincode(data):
    masked_values = []
    for value in data:
        str_value = str(value)
        if len(str_value) <= 2:
            # If the pincode has 2 or fewer digits, mask all digits
            masked_values.append('XX')
        else:
            # Mask all digits except the first and last two digits
            masked_values.append(str_value[:-2] + 'XX')
    
    return masked_values

def complex_mask_pincode(data):
    masked_values = []
    for value in data:
        str_value = str(value)
        if len(str_value) <= 2:
            # If the pincode has 2 or fewer digits, mask all digits
            masked_values.append('XX')
        else:
            # Mask the middle digits, leaving the first two and last two digits intact
            first_two_digits = str_value[:2]
            last_two_digits = str_value[-2:]
            masked_digits = 'X' * (len(str_value) - 4)
            masked_values.append(first_two_digits + masked_digits + last_two_digits)
    
    return masked_values

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
    soundex_number = ''
    for digit in str(phone_number):
        if digit.isdigit():
            soundex_number += soundex_codes[digit]
    masked_soundex = soundex_number[:3] + 'X' * (len(soundex_number) - 3)
    return masked_soundex

def shuffle_column_numbers(column_values):
    rounded_numbers = [math.ceil(num) for num in column_values]
    indexes = list(range(len(column_values)))
    random.shuffle(indexes)
    shuffled_numbers = [rounded_numbers[index] for index in indexes]
    return shuffled_numbers

def shuffle_digits(column_values):
    result_values = []
    for value in column_values:
        digits_list = [int(digit) for digit in str(value)]
        random.shuffle(digits_list)
        result_value = int("".join(map(str, digits_list)))
        result_values.append(result_value)
    return result_values

def add_fixed_value(fix):
    fixed_value = 100
    # Add the fixed value to the specified column
    final = fix+ fixed_value
    # Return the updated DataFrame
    return final

def sub_fixed_value(fix):
    fixed_value = 100
    # Add the fixed value to the specified column
    final = fix- fixed_value
    # Return the updated DataFrame
    return final

def modify_list_values(input_list):
    # Modify the list
    result_list = []
    for value in input_list:
        multiplied_digits = [str(int(digit) * 2) for digit in str(value)]
        final_digits = [str(int(digit) + 1) if int(digit) % 2 == 0 else str(int(digit) - 1) for digit in multiplied_digits]
        final_value = int("".join(final_digits))
        result_list.append(final_value)

    # Return the modified list
    return result_list

def mask_employee_ids(x):

    # Generate a random power of 2
    power_of_two = 2 ** random.randint(1, 10)

    # Apply the mask to the specified column
    return x + power_of_two

def multiply_random_middle(number):
    # Check if the number has at least three digits
    if isinstance(number, int) and number >= 100:
        # Convert the number to a string
        number_str = str(number)
        
        # Generate a random replacement string
        replacement = ''.join(str(random.randint(0, 9)) for _ in range(len(number_str)))
        
        # Return the masked number
        return int(replacement)
    
    return number