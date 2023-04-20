import pandas as pd
import random

def phone_to_ascii(phone_num):
    """
    Converts phone number to ASCII format and masks random characters with X's.
    """
    phone_str = str(phone_num)
    ascii_num = ''.join([str(ord(digit)).zfill(2) for digit in phone_num])
    ascii_list = list(ascii_num)
    
    # Randomly mask 10% of characters
    num_chars_to_mask = int(len(ascii_list) * 0.1)
    masked_chars_indices = random.sample(range(len(ascii_list)), num_chars_to_mask)
    
    # Replace masked characters with X's
    for i in masked_chars_indices:
        ascii_list[i] = 'X' 
    # Convert back to phone number format
    masked_ascii_num = ''.join(ascii_list)
    phone_number = ''
    for i in range(0, len(masked_ascii_num), 2):
        phone_number += chr(int(masked_ascii_num[i:i+2]))
    return phone_number

# Read data from excel file
df = pd.read_excel(r'C:\Users\kramal361\Downloads\maskinginput.xlsx')

# Apply ASCII masking to phone numbers
df['Phone Number'] = df['Phone Number'].apply(phone_to_ascii)

# Write the new Excel file with masked phone numbers
df.to_excel('binaryoutput.xlsx', index=False)

print(df['Phone Number'])
