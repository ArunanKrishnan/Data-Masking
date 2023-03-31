import pandas as pd
# Define the truncation function to mask email addresses
def mask_email(email):
    username, domain = email.split('@')
     # maksing the username part to the first 3 characters and add
    truncated_username = username[:3] + '...'
    # Combine the masked username and domain parts to form the masked email address
    masked_email = truncated_username + '@' + domain
    return masked_email
#load the excel file as input
df = pd.read_excel(r'C:\Users\kramal361\Downloads\maskinginput.xlsx')
df['Email address'] = df['Email address'].apply(mask_email)
print(df)
print(df['Email address'])
#load the output in excel file
df.to_excel('outputfle.xlsx', index=False)
