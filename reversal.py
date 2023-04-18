import pandas as pd
import random
import numpy
df = pd.read_excel(r'C:\Users\kramal361\Downloads\maskinginput.xlsx')
# Define function to perform reversal masking on a phone number
def mask_reversal(phone_number):
    # Reverse the phone number
    reversed_number = str(phone_number)[::-1]
    # Determine the number of digits to mask
    num_masked_digits = random.randint(1, len(reversed_number) - 1)
    # Determine the positions of the masked digits
    masked_positions = random.sample(range(len(reversed_number)), num_masked_digits)
    # Mask the digits at the chosen positions with X's or *'s
    masked_number = ''.join(['X' if i in masked_positions else digit for i, digit in enumerate(reversed_number)])
    # Reverse the masked number and return it
    return masked_number[::-1]
df['Phone Number'] = df['Phone Number'].apply(mask_reversal)

# Write the new Excel file with masked phone numbers
df.to_excel('reversaloutput.xlsx', index=False)
print(df['Phone Number'])
