import pandas as pd
import random

def shuffle_digits(df: pd.DataFrame, column_name: str) -> pd.Series:
    """
    Shuffle the digits of each value in the specified column of a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be obfuscated.
        column_name (str): The name of the column containing the data to be obfuscated.

    Returns:
        pd.Series: A new pandas Series object containing the obfuscated data.
    """
    column_values = df[column_name]
    result_values = []
    for value in column_values:
        digits_list = [int(digit) for digit in str(value)]
        random.shuffle(digits_list)
        result_value = int("".join(map(str, digits_list)))
        result_values.append(result_value)
    return pd.Series(result_values)

# Example usage:
file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\data\masking-input.xlsx'
df = pd.read_excel(file_path)
column_name = "Employee ID"
result_column = shuffle_digits(df, column_name)
print("Original values:", df[column_name].tolist())
print("Result values:", result_column.tolist())
