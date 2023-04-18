import pandas as pd
import soundex
df = pd.read_excel(r'C:\Users\kramal361\Downloads\maskinginput.xlsx')
def mask_soundex(phone_number):
    soundex_codes = {
        '0': 'Z',
        '1': 'S',
        '2': 'T',
        '3': 'T',
        '4': 'F',
        '5': 'F',
        '6': 'S',
        '7': 'S',
        '8': 'A',
        '9': 'N'
    }
    soundex_number = ''
    for digit in str(phone_number):
        if digit.isdigit():
            soundex_number += soundex_codes[digit]
    masked_soundex = soundex_number[:3] + 'X' * (len(soundex_number) - 3)
    return masked_soundex
df['Phone Number'] = df['Phone Number'].apply(mask_soundex)

# Write the new Excel file with masked phone numbers
df.to_excel('consonantoutput.xlsx', index=False)
print(df['Phone Number'])
