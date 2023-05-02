import pandas as pd
import random


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


def mask_employee_ids(input_file):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Generate a random power of 2
    power_of_two = 2 ** random.randint(1, 10)

    # Apply the mask to the specified column
    df['Employee ID'] = df['Employee ID'].apply(lambda x: x + power_of_two)

    # Return the masked list of employee IDs as a Python list
    return df['Employee ID'].tolist()
# Example usage of xor_with_random_and function
xor_results = xor_with_random_and(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx')
print(xor_results)

# Example usage of mask_employee_ids function
masked_ids = mask_employee_ids(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx')
print(masked_ids)
import pandas as pd

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
result = modify_list_values(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx', 'Column1')
print(result)
import pandas as pd

def add_fixed_value(file_path, column_name, fixed_value):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Add the fixed value to the specified column
    df[f'Updated {column_name}'] = df[column_name] + fixed_value

    # Return the updated DataFrame
    return df
result = add_fixed_value('C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx', 'Column1', 10)
print(result)
import pandas as pd

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
result = divide_and_swap_column(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx', 'Column1')
print(result)
import pandas as pd
import random

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
file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx'
column_name = 'YourColumnName'
result = multiply_and_subtract(file_path, column_name)
print(result)
import random
import math

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
result = sub_fixed_value(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx', 'Column1', 100)
print(result)