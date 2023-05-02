import pandas as pd
import random

def mask_dataframe(file_path):
    """
    This function shuffles and masks the data in an Excel file using Pandas and print the output file.
    
    Args:
    file_path (str): The file path of the input Excel file.
    
    Returns:
    pandas.DataFrame: The shuffled and masked DataFrame.
    """
    
    # Load data from Excel file into a Pandas DataFrame
    df = pd.read_excel(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\data\masking-input.xlsx')

    # Shuffle the index of the DataFrame
i
    # Shuffle the rows across different columns
    num_cols = len(df.columns)
    for i in range(num_cols):
        df.iloc[:, i] = df.iloc[:, i].sample(frac=1).reset_index(drop=True)

    # creating a list to store the masked employee IDs
    result_values = []

    # Shuffle the index of the DataFrame
    df = df.sample(frac=1).reset_index(drop=True)

    # Shuffle the rows across different columns
    num_cols = len(df.columns)
    for i in range(num_cols):
        df.iloc[:, i] = df.iloc[:, i].sample(frac=1).reset_index(drop=True)

    # Shuffle the phone number and bank account number columns
    num_cols = ["Phone Number", "Bank Account Number"]
    for column_name in num_cols:
        column_values = df[column_name]

        for i, value in enumerate(column_values):
            digits_list = [int(digit) for digit in str(value)]
            random.shuffle(digits_list)
            result_value = int("".join(map(str, digits_list)))
            df.at[i, column_name] = result_value

    # Mask the email addresses
    column_name = "Email address"  
    column_values = df[column_name]

    for i, value in enumerate(column_values):
        # Split the email address into username and domain parts
        username, domain = value.split('@')

        # Shuffle the characters in the username part
        username_list = list(username)
        random.shuffle(username_list)
        shuffled_username = ''.join(username_list)

        # Combine the shuffled username and original domain
        masked_email = f"{shuffled_username}@{domain}"

        # Update the email address column with the masked value
        df.at[i, column_name] = masked_email

    # Save the shuffled and masked DataFrame to the same Excel file
    #df.to_excel(file_path, index=False)
    
        return df
df = mask_dataframe(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking project\Data\masking-input.xlsx')
print(df)

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
updated_df = add_fixed_value(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\data\masking-input.xlsx', 'Employee ID', 1111)


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
swapped_df = divide_and_swap_column(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\data\masking-input.xlsx', 'Employee ID')


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
result = xor_with_random_and(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\DM 2.0\Data-Masking\data\masking-input.xlsx')
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
result = xor_with_random(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\DM 2.0\Data-Masking\data\masking-input.xlsx')
print(result)




