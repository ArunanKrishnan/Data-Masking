import pandas as pd
import random
#Define the function to mask email addresses
def obfuscate_email(email):
    # Split email into username and domain
    username, domain = email.split('@')
    obfuscated_username = ''
    for char in username:
        if char.lower() in ['a', 'e', 'i', 'o', 'u','b','c','d']:
            obfuscated_username += str(random.randint(0, 9))
        else:
            obfuscated_username += char
    # Construct obfuscated email
    obfuscated_email = obfuscated_username + '@' + domain
    return obfuscated_email
# Load the input Excel file
df = pd.read_excel(r'C:\Users\kramal361\Desktop\datamaskingproject\Data-Obfuscation-2\masking-input.xlsx')
df['Email address'] = df['Email address'].apply(obfuscate_email)
print(df)
print(df['Email address'])
#load masked data into output excel file
df.to_excel('outputfles_obfus.xlsx', index=False)
