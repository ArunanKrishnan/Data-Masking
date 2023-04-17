import pandas as pd
import random
import math

def add_fixed_value(df: pd.DataFrame, column_name: str, fixed_value: int) -> pd.DataFrame:
    data_column = df[column_name]
    df['Updated Data'] = data_column + fixed_value
    return df

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

# Chain the three functions together
file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\DM 2.0\Data-Masking\data\masking-input.xlsx'
column_name = "Employee ID"

df = pd.read_excel(file_path)
updated_df = add_fixed_value(df, column_name, 1111)
result_column = multiply_and_subtract(updated_df, 'Updated Data')
result_column = shuffle_digits(updated_df, 'Updated Data')

print("Original values:", df[column_name].tolist())
print("Updated values:", updated_df['Updated Data'].tolist())
print("Result values:", result_column.tolist())