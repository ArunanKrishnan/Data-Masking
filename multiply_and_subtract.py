import pandas as pd
import random

def multiply_and_subtract(df: pd.DataFrame, column_name: str) -> pd.Series:
    """
    Multiply the values in the specified column of a DataFrame with a random number
    between 0 and 1, and subtract the result from the original value.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be obfuscated.
        column_name (str): The name of the column containing the data to be obfuscated.

    Returns:
        pd.Series: A new pandas Series object containing the obfuscated data.
    """
    column_values = df[column_name]
    result_values = []
    for value in column_values:
        random_number = random.uniform(0, 1)
        result = round(value - (value * random_number))
        result_values.append(result)
    return pd.Series(result_values)

# Example usage:
file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\data\masking-input.xlsx'
df = pd.read_excel(file_path)
column_name = "Employee ID"
result_column = multiply_and_subtract(df, column_name)
print("Original values:", df[column_name].tolist())
print("Result values:", result_column.tolist())
