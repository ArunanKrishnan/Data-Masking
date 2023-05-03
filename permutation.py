import pandas as pd
import random

def mask_dataframe(file_path):
    """
    This function shuffles and masks the data in an Excel file using Pandas and prints the output DataFrame.
    
    Args:
    file_path (str): The file path of the input Excel file.
    
    Returns:
    pandas.DataFrame: The shuffled and masked DataFrame.
    """
    
    # Load data from Excel file into a Pandas DataFrame
    df = pd.read_excel(file_path)

    # Shuffle the index of the DataFrame
    df = df.sample(frac=1).reset_index(drop=True)

    # Shuffle the rows across different columns
    num_cols = len(df.columns)
    for i in range(num_cols):
        df[df.columns[i]] = df[df.columns[i]].sample(frac=1).reset_index(drop=True)

    # Shuffle the phone number and bank account number columns
    num_cols = ["Pin code", "Employee ID"]
    for column_name in num_cols:
        column_values = df[column_name]

        for i, value in enumerate(column_values):
            digits_list = [int(digit) for digit in str(value)]
            random.shuffle(digits_list)
            result_value = int("".join(map(str, digits_list)))
            df.at[i, column_name] = result_value

    # Shuffle the email domains
    column_name = "Email address"  
    column_values = df[column_name]

    domains_list = []
    for value in column_values:
        # Split the email address into username and domain parts
        username, domain = value.split('@')
        domains_list.append(domain)

    # Shuffle the list of domains
    random.shuffle(domains_list)

    # Update the email address column with the shuffled domains
    for i, value in enumerate(column_values):
        # Split the email address into username and domain parts
        username, domain = value.split('@')
        shuffled_domain = domains_list[i]

        # Combine the username and shuffled domain to form the masked email
        masked_email = f"{username}@{shuffled_domain}"

        # Update the email address column with the masked value
        df.at[i, column_name] = masked_email



     # Shuffle the names in the Name column
    column_name = "Name"
    column_values = df[column_name]

# Split the names into first and last name lists
    first_list = []
    last_list = []
    for name in column_values:
       first, last = name.split(" ")
       first_list.append(first)
       last_list.append(last)

# Shuffle the first and last name lists
    random.shuffle(first_list)
    random.shuffle(last_list)

# Combine the shuffled first and last names to form the shuffled names list
    shuffled_names = []
    for i in range(len(column_values)):
        shuffled_name = f"{first_list[i]} {last_list[i]}"
        shuffled_names.append(shuffled_name)

# Update the Name column with the shuffled names
    df[column_name] = shuffled_names

# Print the shuffled and masked DataFrame
    print(df)

    return df



# Test the function
mask_dataframe(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\dm\Data-Masking\data\masking-input.xlsx')