import pandas as pd
import random
import hashlib
import numpy as np

# Read the Excel file into a DataFrame
df = pd.read_excel(r'C:\Users\kramal361\Downloads\masking-input (2).xlsx')
# Define a function to apply the algorithm to each pin code
import random

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
    else:
        # If the number has less than three digits, return an error message
        return ["Error: Number should have at least three digits"]
    return updated_numbers

# Apply the function to the 'Pin code' column in the DataFrame
#df['Updated Number'] = df['Pin code'].apply(multiply_random_middle)

# Define a function to apply the algorithm to each pin code
def extract_first_digit(number):
    # Convert the number to a string
    number_str = str(number)
    # Check if the number has at least four digits
    if len(number_str) >= 4:
        # Extract the first digit of the original number
        first_digit = number_str[0]
        # Extract the next three digits of the original number
        next_three_digits = number_str[1:4]
        # Create a list containing the extracted first digit and next three digits
        extracted_digits = [int(first_digit), int(next_three_digits)]
        # Return the list
        return extracted_digits
    else:
        # If the number has less than four digits, return an error message as a list
        return ["Error: Number should have at least four digits"]

# Apply the function to the 'Pin code' column in the DataFrame
#df[['First Digit', 'Next Three Digits']] = df['Pin code'].apply(extract_first_digit).apply(pd.Series)
#print(['Pin code'])
def mask_pincode(pincode):
    # Convert the pincode to a string
    pincode_str = str(pincode)

    # Mask the pincode using bitwise XOR operation
    masked_chars = []
    for char in pincode_str:
        masked_char = chr(ord(char) ^ 255)
        masked_chars.append(masked_char)

    return masked_chars


# Apply the masking function to the 'Pin code' column in the DataFrame
#df['Pin code']= df['Pin code'].apply(mask_pincode)

def mask_pincode(pincode):
    # Convert the pincode to a string
    pincode_str = str(pincode)

    # Mask the pincode using bitwise XOR operation
    masked_chars = []
    for char in pincode_str:
        masked_char = chr(ord(char) ^ 255)
        masked_chars.append(masked_char)

    return masked_chars

#df['Pin code']=df['Pin code'].apply(mask_pincode)



'''
# Test the function with an example pincode
example_pincode = "123456"
masked_pincode = mask_pincode(example_pincode)
print("Original PIN Code: ", example_pincode)
print("Masked PIN Code: ", masked_pincode) '''

# Define a function to apply the algorithm to each pin code
def remind_first_last_swap_between(number):
    # Convert the number to a string
    number_str = str(number)
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
        # Return the list
        return swapped_list
    else:
        # If the number has less than two digits, return an error message as a list
        return ["Error: Number should have at least two digits"]

# Apply the function to the 'Pin code' column in the DataFrame
#df['Pin code'] = df['Pin code'].apply(remind_first_last_swap_between)

# Define a function to apply the complex algorithm to each pin code
def complex_mask_pincode(pincode):
    # Convert the pincode to a string
    pincode_str = str(pincode)
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
        return [masked_pincode]  # wrap the masked pincode in a list
    else:
        # If the pincode has less than five digits, return an error message
        return ["Error: Pincode should have at least five digits"]

# Apply the function to the 'Pin code' column in the DataFrame
#df['Pin code'] = df['Pin code'].apply(complex_mask_pincode)

# Define a function to apply tokenization to each pin code
# def tokenization_mask_pincode(pincode):
#     # Convert the pin code to a string
#     pincode_str = str(pincode)
#     # Use a hash function (e.g., SHA-256) to generate a token from the pin code
#     token = hashlib.sha256(pincode_str.encode()).hexdigest()
#     return token
# Apply the function to the 'Pin code' column in the DataFrame
#df['Pin code'] = df['Pin code'].apply(tokenization_mask_pincode)

import numpy as np

def mask_pincode(pincode):
    # Convert PIN code to matrix
    pin_matrix = np.array([[int(d) for d in str(pincode)]])
    # Generate masking matrix with random values
    masking_matrix = np.random.randint(0, 10, size=pin_matrix.shape)
    # Perform matrix multiplication
    masked_matrix = np.dot(pin_matrix, masking_matrix)
    # Flatten masked matrix to get masked PIN code
    masked_pincode = ''.join(str(d) for d in masked_matrix.flatten())
    return [int(d) for d in masked_pincode]


# Apply masking function to each PIN code in the DataFrame
# df['Pin code'] = df['Pin code'].apply(mask_pincode)
# print(df['Pin code'])


