import pandas as pd
import math
import random

def shuffle_column_numbers(file_path, column_name):
    """
    This function shuffles the integers within a given column of an excel file.

    Parameters:
    file_path (str): The file path of the input excel file.
    column_name (str): The name of the column to shuffle.

    Returns:
    A list of shuffled numbers.
    """

    df = pd.read_excel(file_path)
    column_values = df[column_name]
    rounded_numbers = [math.ceil(num) for num in column_values]
    indexes = list(range(len(column_values)))
    random.shuffle(indexes)
    shuffled_numbers = [rounded_numbers[index] for index in indexes]

    print("Original values:", column_values.tolist())
    print("Shuffled numbers:", shuffled_numbers)

    return shuffled_numbers
file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\data\masking-input.xlsx'
column_name = "Employee ID"
shuffled_numbers = shuffle_column_numbers(file_path, column_name)
