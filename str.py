import pandas as pd
import random
#import input data
df = pd.read_excel(r'C:\Users\kramal361\Desktop\datamaskingproject\Data-Obfuscation-2\masking-input.xlsx')
def shuffle_email(email):
    email_parts = email.split('@')
    username = email_parts[0]
    domain = email_parts[1]
    shuffled_username = ''.join(random.sample(username, len(username)))
    shuffled_email = shuffled_username + '@' + domain
    return shuffled_email
df['Email address'] = df['Email address'].apply(shuffle_email)
print(df)
print(df['Email address'])
df.to_excel('output_shuffling.xlsx', index=False)


# Define the truncation function to mask email addresses
def mask_email(email):
    username, domain = email.split('@')
     # maksing the username part to the first 3 characters and add
    truncated_username = username[:3] + '...'
    # Combine the masked username and domain parts to form the masked email address
    masked_email = truncated_username + '@' + domain
    return masked_email
#load the excel file as input
df = pd.read_excel(r'C:\Users\kramal361\Desktop\datamaskingproject\Data-Obfuscation\masking-input.xlsx')
df['Email address'] = df['Email address'].apply(mask_email)
print(df)
print(df['Email address'])
#load the output in excel file
df.to_excel('outputfle_truncate.xlsx', index=False)


# Define the padding function to mask email addresses
def pad_email(email):
    # Define a list of characters to choose
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
     # Add random characters to the email address
    char=''
    for i in range(5):
        char += random.choice(chars)
        #it chooses from the second character and do masking
    pad_email = email[:1] + '....' + char+ email[-10:]
    return pad_email
import pandas as pd
import random
#load the excel file as the input
df = pd.read_excel(r'C:\Users\kramal361\Desktop\datamaskingproject\Data-Obfuscation-2\masking-input.xlsx')
if 'Email address' in df.columns:
    df['Email address'] = df['Email address'].apply(pad_email)
    print(df['Email address'])
    #load the masked output in the ouput excel file
    df.to_excel('outputfile_padding.xlsx', index=False)


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



# Define the cryptography function to mask email addresses
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
def encrypt_email(email):
    encrypted_email = fernet.encrypt(email.encode())
    return encrypted_email
#load the excel file as a input
df = pd.read_excel(r'C:\Users\kramal361\DownloadsC:\Users\kramal361\Desktop\datamaskingproject\Data-Obfuscation-2\maskinginput.xlsx')
df['Email address'] = df['Email address'].apply(encrypt_email)
#load the masked data in the output excel file 
df.to_excel('encrypted_emails.xlsx', index=False)
print('Original Email Addresses:')
print(df['Email address'])
print('\nEncrypted Email Addresses:')