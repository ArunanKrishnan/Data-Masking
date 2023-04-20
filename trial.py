import json
import pandas as pd
import random

# Load the JSON configuration file
with open('cc_sky_data_masking.json', 'r') as f:
    config = json.load(f)

#import input data
input_file = config["input_file"]
df = pd.read_excel(input_file)

#import input data
#df = pd.read_excel(r'C:\Users\kramal361\Desktop\datamaskingproject\Data-Obfuscation-2\masking-input.xlsx')
def shuffle_email(email):
    email_parts = email.split('@')
    username = email_parts[0]
    domain = email_parts[1]
    shuffled_username = ''.join(random.sample(username, len(username)))
    shuffled_email = shuffled_username + '@' + domain
    return shuffled_email
fun1= df['Email address'].apply(shuffle_email)



# Define the truncation function to mask email addresses
def mask_email(email):
    username, domain = email.split('@')
     # maksing the username part to the first 3 characters and add
    truncated_username = username[:3] + '...'
    # Combine the masked username and domain parts to form the masked email address
    masked_email = truncated_username + '@' + domain
    return masked_email
fun2= df['Email address'].apply(mask_email)

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
if 'Email address' in df.columns:
    fun3= df['Email address'].apply(pad_email)

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
fun4= df['Email address'].apply(obfuscate_email)

def mask_email(function_name):
    if function_name == 'shuffle_email':
        return df['Email address'].apply(shuffle_email)
    elif function_name == 'mask_email':
        return df['Email address'].apply(mask_email)
    elif function_name == 'pad_email':
        return df['Email address'].apply(pad_email)
    elif function_name == 'obfuscate_email':
        return df['Email address'].apply(obfuscate_email)
    else:
        print(f"Invalid function name: {function_name}")


# Apply masking to the specified columns
for col_config in config['column_info']:
    if 'ApplyMasking' in col_config['col_type']:
        col_name = col_config['name']
        col_type = col_config['type']
        col_data = df[col_name]
        functions_to_apply = col_config['col_type']['ApplyMasking']

        for function_name in functions_to_apply:
            col_data = mask_email(function_name)

        df[col_name] = col_data

# Write the masked data to a new Excel file
output_file = config['output_file']
df.to_excel(output_file, index=False)