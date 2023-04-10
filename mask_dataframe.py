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
    df = df.sample(frac=1).reset_index(drop=True)

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

