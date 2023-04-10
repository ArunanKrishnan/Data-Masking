
import pandas as pd
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
