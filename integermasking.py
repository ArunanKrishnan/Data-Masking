import pandas as pd
import numpy as np
import random
import soundex
df = pd.read_excel(r'C:\Users\kramal361\Downloads\maskinginput.xlsx', dtype={'Phone Number': str})
# Define function to convert a phone number to binary format
def binary_to_phone(binary_number):
    binary_number = str(binary_number) 
    binary_number = binary_number.replace('X', '0')
    phone_number = ''
    for i in range(0, len(binary_number), 4):
        binary_digit = binary_number[i:i+4]
        if all(d in '01' for d in binary_digit):
            digit = str(int(binary_digit, 2))
            phone_number += digit
        else:
            phone_number += 'X'
        if i == 3:
            phone_number += '-'
        elif i == 7:
            phone_number += '-'
    return phone_number
fun1=df['Phone Number'].apply(binary_to_phone)

# Define function to mask all digits in the phone number column
def mask_consonants(phone_number):
    return ''.join(['X' if c.isdigit() else c for c in str(phone_number)])
fun2=df['Phone Number'].apply(mask_consonants)

# Define function to perform reversal masking on a phone number
def mask_reversal(phone_number):
    # Reverse the phone number
    reversed_number = str(phone_number)[::-1]
    # Determine the number of digits to mask
    num_masked_digits = random.randint(1, len(reversed_number) - 1)
    # Determine the positions of the masked digits
    masked_positions = random.sample(range(len(reversed_number)), num_masked_digits)
    # Mask the digits at the chosen positions with X's or *'s
    masked_number = ''.join(['X' if i in masked_positions else digit for i, digit in enumerate(reversed_number)])
    # Reverse the masked number and return it
    return masked_number[::-1]
fun3=df['Phone Number'].apply(mask_reversal)

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
fun4=df['Phone Number'].apply(mask_soundex)

# Define function to apply randomized offset masking to a phone number
def randomized_offset_masking(phone_number):
    phone_number = str(phone_number)  # Convert phone number to string
    length = len(phone_number)
    offset = random.randint(0, length - 1)  # Choose random offset
    num_digits_to_mask = random.randint(1, length - offset)  # Choose random number of digits to mask
    masked_number = list(phone_number)
    for i in range(offset, offset + num_digits_to_mask):
        masked_number[i] = 'X'  # Mask selected digits with X's
    masked_number = ''.join(masked_number)
    return masked_number
fun5=df['Phone Number'].apply(randomized_offset_masking)
print(fun5)






