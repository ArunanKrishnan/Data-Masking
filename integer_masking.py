


import pandas as pd
import random

def xor_with_random_and(input_file):
    """
    Performs the XOR operation on each integer in a list of integers in an Excel file
    with the result of a bitwise AND operation with a random value.
    
    Args:
    - input_file: str, the path to the Excel file
    
    Returns:
    - A DataFrame with two columns: "Number" (the original integer) and "XOR" (the result of the XOR operation).
    """
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
        xor_results.append({'Number': number, 'XOR': xor_result})
    
    # Convert the list of XOR results to a DataFrame and return it
    return pd.DataFrame(xor_results)
result = xor_with_random_and(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx')
print(result)


import pandas as pd
import random

def xor_with_random(input_file):
    """
    Performs the XOR operation on each integer in a list of integers in an Excel file
    with the result of a bitwise OR operation with a random value.
    
    Args:
    - input_file: str, the path to the Excel file
    
    Returns:
    - A DataFrame with two columns: "Number" (the original integer) and "XOR" (the result of the XOR operation).
    """
    # Load the Excel file into a DataFrame
    df = pd.read_excel(input_file)
    
    # Initialize an empty list to store the XOR results
    xor_results = []
    
    # Iterate over the integers in the DataFrame
    for number in df['Employee ID']:
        # Generate a random value and perform a bitwise OR operation with the number
        random_value = random.randint(1, 1000)
        or_result = number | random_value
        
        # Perform the XOR operation with the OR result
        xor_result = number ^ or_result
        
        # Add the XOR result to the list
        xor_results.append({'Number': number, 'XOR': xor_result})
    
    # Convert the list of XOR results to a DataFrame and return it
    return pd.DataFrame(xor_results)
result = xor_with_random(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx')
print(result)

import pandas as pd
import random


def mask_employee_ids(file_path, column_name):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Generate a random power of 2
    power_of_two = 2 ** random.randint(1, 10)

    # Apply the mask to the specified column
    df[column_name] = df[column_name].apply(lambda x: x + power_of_two)

    # Save the modified data to the Excel file
    with pd.ExcelWriter(file_path) as writer:
        df.to_excel(writer, index=False)

    # Print the original and modified values for verification
    print("Original values:", df[column_name].tolist())
    print("Masked values:", df[column_name].apply(lambda x: x - power_of_two).tolist())


def modify_column_values(file_path, column_name):
    df = pd.read_excel(file_path)
    column_values = df[column_name]

    result_values = []
    for value in column_values:
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
        result_values.append(final_value)

    return result_values


def generate_binary_codes(file_path, column_name):
    df = pd.read_excel(file_path)
    column_values = df[column_name]

    result_values = []

    for value in column_values:

        first_two_digits = str(value)[:2]
        binary_code = bin(int(first_two_digits))[2:].zfill(8)

        rest_of_digits = str(value)[2:]
        binary_code += bin(int(rest_of_digits))[2:].zfill(len(rest_of_digits) * 4)

        result_values.append(binary_code)

    return result_values


# Call the functions and print the output
file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx'
column_name = "Employee ID"

print("Mask employee IDs:")
mask_employee_ids(file_path, column_name)
print("\nModify column values:")
print(modify_column_values(file_path, column_name))
print("\nGenerate binary codes:")
print(generate_binary_codes(file_path, column_name))

