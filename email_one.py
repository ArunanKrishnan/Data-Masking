import pandas as pd
import numpy as np
import random
import soundex
df = pd.read_excel(r'C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx')

def shuffle_email(email):
    mask = []
    email_parts = email.split('@')
    username = email_parts[0]
    domain = email_parts[1]
    shuffled_username = ''.join(random.sample(username, len(username)))
    shuffled_email = shuffled_username + '@' + domain
    mask.append(shuffled_email)
    return mask

# Define the truncation function to mask email addresses
def mask_email(email):
    l=[]
    username, domain = email.split('@') 
    truncated_username = username[:3] + '...'
    masked_email = truncated_username + '@' + domain
    l.append(masked_email)
    return l

# Define the padding function to mask email addresses
def pad_email(email):
    p=[]
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    char=''
    for i in range(5):
        char += random.choice(chars)  
    pad_email = email[:1] + '....' + char+ email[-10:]
    p.append(pad_email)
    return p

#Define the function to mask email addresses
def obfuscate_email(email):
        o=[]
        username, domain = email.split('@')
        obfuscated_username = ''
        for char in username:
            if char.lower() in ['a', 'e', 'i', 'o', 'u','b','c','d']:
                obfuscated_username += str(random.randint(0, 9))
        else:
            obfuscated_username += char
        obfuscated_email = obfuscated_username + '@' + domain
        o.append(obfuscated_email)
        return o
#df['Email address'] = df['Email address'].apply(obfuscate_email)
#print(df['Email address'])