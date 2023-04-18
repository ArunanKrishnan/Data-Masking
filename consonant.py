import pandas as pd

# Read the Excel file
df = pd.read_excel(r'C:\Users\kramal361\Downloads\maskinginput.xlsx', dtype={'Phone Number': str})

# Define function to mask all digits in the phone number column
def mask_consonants(phone_number):
    return ''.join(['X' if c.isdigit() else c for c in str(phone_number)])

# Apply mask_consonants function to phone number column

df['Phone Number'] = df['Phone Number'].apply(mask_consonants)

# Write the new Excel file with masked phone numbers
df.to_excel('binaryoutput.xlsx', index=False)
print(df['Phone Number'])
