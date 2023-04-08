import pandas as pd

# Load the input Excel file
input_file = r'C:\Users\sethir919\Desktop\project\masking-input.xlsx'
data = pd.read_excel(input_file)

# Define a function to mask a single name
def mask_name(name):
    first_letter = name[0]
    last_letter = name[-1]
    masked_name = (len(name)-2)*'*'
    return  masked_name 

# Mask the names in the 'Name' column
data['Name'] = data['Name'].apply(mask_name)
data.to_excel('output_file_mask.xlsx', index=False)

