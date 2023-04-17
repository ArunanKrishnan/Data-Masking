import pandas as pd
import random
import math

def add_fixed_value(data_file_path, column_name, fixed_value):
    df = pd.read_excel(data_file_path)
    data_column = df[column_name]
    df['Updated Data'] = data_column + fixed_value
    return df['Updated Data']

def multiply_and_subtract(df: pd.DataFrame, column_name: str) -> pd.Series:
    column_values = df[column_name]
    result_values = []
    for value in column_values:
        random_number = random.uniform(0, 1)
        result = round(value - (value * random_number))
        result_values.append(result)
    return pd.Series(result_values)

def shuffle_digits(df: pd.DataFrame, column_name: str) -> pd.Series:
    column_values = df[column_name]
    result_values = []
    for value in column_values:
        digits_list = [int(digit) for digit in str(value)]
        random.shuffle(digits_list)
        result_value = int("".join(map(str, digits_list)))
        result_values.append(result_value)
    return pd.Series(result_values)

def divide_and_swap(numbers):
    length = len(numbers)
    if length % 2 == 0:
        half = length // 2
        first_half = numbers[:half]
        second_half = numbers[half:]
        swapped_numbers = second_half + first_half
        return swapped_numbers
    else:
        return "Error: List length must be even"

def shuffle_column_numbers(df: pd.DataFrame, column_name: str) -> pd.Series:
    column_values = df[column_name]
    rounded_numbers = [math.ceil(num) for num in column_values]
    indexes = list(range(len(column_values)))
    random.shuffle(indexes)
    shuffled_numbers = [rounded_numbers[index] for index in indexes]
    return pd.Series(shuffled_numbers)

# Example usage:
file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\DM 2.0\Data-Masking\data\masking-input.xlsx'
column_name = "Employee ID"

df = pd.read_excel(file_path)
print("Original values:", df[column_name].tolist())

result_column = add_fixed_value(file_path, column_name, 1111)
print("Result of add_fixed_value:", result_column.tolist())

result_column = multiply_and_subtract(df, column_name)
print("Result of multiply_and_subtract:", result_column.tolist())

result_column = shuffle_digits(df, column_name)
print("Result of shuffle_digits:", result_column.tolist())

result_column = shuffle_column_numbers(df, column_name)
print("Result of shuffle_column_numbers:", result_column.tolist())

result_column = divide_and_swap(result_column.tolist())
print("Result of divide_and_swap:", result_column)

# create new DataFrame with swapped column values and save to Excel file
#swapped_df = pd.DataFrame({f'Swapped {column_name}': result_column})
#swapped_df.to_excel('op_divide&swap.xlsx', index=False)