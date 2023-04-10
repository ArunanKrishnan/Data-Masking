import pandas as pd

def add_fixed_value(data_file_path, column_name, fixed_value):
    """
    Adds a fixed value to each value in a specified column of a given Excel file using pandas.
    
    Parameters:
    - data_file_path (str): The file path of the Excel file to read.
    - column_name (str): The name of the column to perform the operation on.
    - fixed_value (int or float): The value to add to each value in the column.
    
    Returns:
    - df (pandas.DataFrame): The updated DataFrame with the new column added.
    """
    df = pd.read_excel(data_file_path)
    data_column = df[column_name]
    df['Updated Data'] = data_column + fixed_value
    return df
updated_df = add_fixed_value('C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\data\masking-input.xlsx', 'Employee ID', 1111)
