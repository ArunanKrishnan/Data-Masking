import pandas as pd

def divide_and_swap_column(data_file_path, column_name):
    """
    Divides a column into two halves, swaps the two halves, and saves the resulting DataFrame to an Excel file.
    
    Parameters:
    - data_file_path (str): The file path of the Excel file to read.
    - column_name (str): The name of the column to perform the operation on.
    
    Returns:
    - swapped_df (pandas.DataFrame): The DataFrame with the swapped column values.
    """
    # read data from Excel file
    data = pd.read_excel(data_file_path)

    # define function to divide and swap column values
    def divide_and_swap(numbers):
        """
        Divides a list of numbers into two halves, swaps the two halves, and returns the resulting list.
        
        Parameters:
        - numbers (list of int or float): The list of numbers to divide and swap.
        
        Returns:
        - swapped_numbers (list of int or float): The list of numbers with the swapped halves.
        """
        length = len(numbers)
        if length % 2 == 0:
            half = length // 2
            first_half = numbers[:half]
            second_half = numbers[half:]
            swapped_numbers = second_half + first_half
            return swapped_numbers
        else:
            return "Error: List length must be even"

    # convert column to list of numbers and apply divide_and_swap function
    numbers = data[column_name].tolist()
    swapped_numbers = divide_and_swap(numbers)

    # create new DataFrame with swapped column values and save to Excel file
    swapped_df = pd.DataFrame({f'Swapped {column_name}': swapped_numbers})
    swapped_df.to_excel('op_divide&swap.xlsx', index=False)

    return swapped_df
swapped_df = divide_and_swap_column('C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\data\masking-input.xlsx', 'Employee ID')

