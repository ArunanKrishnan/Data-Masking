import pandas as pd
import numpy as np
import random
import soundex
df=pd.read_excel(r"C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx")

def shuffle_email(email):
    if isinstance(email, pd.Series):
        return email.apply(shuffle_email)  # Apply the function to each element in the Series
    elif isinstance(email, str):
        email_parts = email.split('@')
        username = email_parts[0]
        domain = email_parts[1]
        shuffled_username = ''.join(random.sample(username, len(username)))
        shuffled_email = shuffled_username + '@' + domain
        return shuffled_email
    else:
        return email


# Define the truncation function to mask email addresses
def mask_email(email):
    if isinstance(email, pd.Series):
        return email.apply(mask_email)  # Apply the function to each element in the Series
    elif isinstance(email, str):
        username, domain = email.split('@')
        masked_username = ''.join('*' for _ in username)
        masked_domain = domain.split('.')[0] + 'masked.com'
        masked_email = masked_username + '@' + masked_domain
        return masked_email
    else:
        return email  # Return non-string values as is


# Define the padding function to mask email addresses
def pad_email(email):
    if isinstance(email, pd.Series):
        return email.apply(pad_email)  # Apply the function to each element in the Series
    elif isinstance(email, str):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        char = ''
        for _ in range(5):
            char += random.choice(chars)
        padded_email = email[:1] + '....' + char + email[-10:]
        return padded_email
    else:
        return email  # Return non-string values as is

#Define the function to mask email addresses
def obfuscate_email(email):
    if isinstance(email, pd.Series):
        return email.apply(obfuscate_email)  # Apply the function to each element in the Series
    elif isinstance(email, str):
        username, domain = email.split('@')
        obfuscated_username = ''
        for char in username:
            if char.lower() in ['a', 'e', 'i', 'o', 'u', 'b', 'c', 'd']:
                obfuscated_username += str(random.randint(0, 9))
            else:
                obfuscated_username += char
        obfuscated_email = obfuscated_username + '@' + domain
        return obfuscated_email
    else:
        return email  # Return non-string values as is
# df['Email address'] = df['Email address'].apply(obfuscate_email)
# print(df['Email address'])   