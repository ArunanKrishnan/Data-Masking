
import pandas as pd
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
def encrypt_email(email):
    encrypted_email = fernet.encrypt(email.encode())
    return encrypted_email
df = pd.read_excel(r'C:\Users\kramal361\Downloads\maskinginput.xlsx')
df['Email address'] = df['Email address'].apply(encrypt_email)
df.to_excel('encrypted_emails.xlsx', index=False)
print('Original Email Addresses:')
print(df['Email address'])
print('\nEncrypted Email Addresses:')
