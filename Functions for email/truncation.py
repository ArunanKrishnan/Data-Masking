import pandas as pd
def mask_email(email):
    username, domain = email.split('@')
    truncated_username = username[:3] + '...'
    masked_email = truncated_username + '@' + domain
    return masked_email
df = pd.read_excel(r'C:\Users\kramal361\Downloads\maskinginput.xlsx')
df['Email address'] = df['Email address'].apply(mask_email)
print(df)
df.to_excel('outputfle.xlsx', index=False)
