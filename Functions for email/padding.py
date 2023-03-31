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
    df.to_excel('outputfile.xlsx', index=False)
