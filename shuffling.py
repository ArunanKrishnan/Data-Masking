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
