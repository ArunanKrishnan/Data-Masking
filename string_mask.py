import json
import pandas as pd
import hashlib
import os
import random

# Load the JSON configuration file
with open('check.json', 'r') as f:
    config = json.load(f)

#import input data
input_file = config["input_file"]
data = pd.read_excel(input_file)

# Define a function to mask a single name
def mask_string_by_asterick(name):
    first_letter = name[0]
    last_letter = name[-1]
    masked_name = (len(name)-2)*'*'
    return  masked_name 
fun1=data['Name'].apply(mask_string_by_asterick)

def mask_string_by_knuth_shuffle(s):
    chars = list(s)
    for i in range(len(chars)-1, 0, -1):
        j = random.randint(0, i)
        chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)
# Apply the knuth_shuffle function to the 'String Column' column
fun2=data['Name'] = data['Name'].apply(mask_string_by_knuth_shuffle)

def mask_string_by_durstenfeld_shuffle(s):
    chars = list(s)
    for i in range(len(chars)-1, 0, -1):
        j = random.randint(0, i)
        chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)
# Convert the string column to a list and shuffle it using the durstenfeld_shuffle function
shuffled_column = data['Name'].apply(lambda x: list(x)).apply(mask_string_by_durstenfeld_shuffle)
# Replace the original string column with the shuffled list
fun3=data['Name'] = shuffled_column.apply(lambda x: ''.join(x))


# Define a list of replacement names
replacement_names = ['John Doe', 'Jane Doe', 'Bob Smith', 'Alice Johnson', 'Michael Brown']

# Define a function to mask names in a string
def mask_string_by_replacement(name):
    if name in replacement_names:
        return random.choice(mask_string_by_replacement)
    else:
        return name
fun4=data['Name'].apply(mask_string_by_replacement)

def mask_string_by_caesar_cipher(plaintext, key):
    """Encrypt a string using the Caesar cipher algorithm."""
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + key) % 26 + 65)
        else:
            shifted_char = char
        ciphertext += shifted_char
    return ciphertext

# Define the key to use for the Caesar cipher
key = 3

# Apply the Caesar cipher to the 'Name' column
fun5= data['Name'].apply(lambda x: mask_string_by_caesar_cipher(x, key) if isinstance(x, str) else x)

def mask_string_by_salt_and_hash(plaintext):
    """Encrypt a string using salt and hash."""
    salt = os.urandom(4)
    salted_plaintext = salt + plaintext.encode()
    hashed_plaintext = hashlib.sha256(salted_plaintext).hexdigest()
    return hashed_plaintext

# Apply the salt and hash algorithm to the 'Name' column
fun6= data['Name'].apply(lambda x: mask_string_by_salt_and_hash(x) if isinstance(x, str) else x)

def mask_string_by_reverse_string(plaintext):
    """Reverse a string."""
    return plaintext[::-1]

# Apply the reversal algorithm to the 'Name' column
fun7= data['Name'].apply(lambda x: mask_string_by_reverse_string(x) if isinstance(x, str) else x)

def mask_string_by_substitute_chars(plaintext):
    """Replace each character in a string with a corresponding character from a mapping."""
    mapping = {'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T',
               'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P',
               'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G',
               'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z',
               'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N', 'Z': 'M'}
    return ''.join([mapping.get(c.upper(), c) for c in plaintext])

# Apply the substitution cipher algorithm to the 'Name' column
fun8= data['Name'].apply(lambda x: mask_string_by_substitute_chars(x) if isinstance(x, str) else x)

def mask_string_by_replace_random_chars(plaintext):
    """Replace each character in a string with a randomly selected character from a set."""
    char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join([random.choice(char_set) if c.isalpha() else c for c in plaintext])

# Apply the random replacement algorithm to the 'Name' column
fun9= data['Name'].apply(lambda x: mask_string_by_replace_random_chars(x) if isinstance(x, str) else x)

# Define a fixed key value for XOR operation
key = 2

def mask_string_by_xor_chars(plaintext):
    """Perform a bitwise XOR operation between each character in a string and a fixed key value."""
    return ''.join([chr(ord(c) ^ key) for c in plaintext])

# Apply the Bitwise XOR algorithm to the 'Name' column
fun10= data['Name'].apply(lambda x: mask_string_by_xor_chars(x) if isinstance(x, str) else x)

def mask_string(function_name):
    if function_name == 'mask_string_by_asterick':
#Apply mask_string_by_asterick
        return data['Name'].apply(mask_string_by_asterick)
    elif function_name == 'mask_string_by_knuth_shuffle':
#Apply mask_string_by_knuth_shuffle
        return data['Name'].apply(mask_string_by_knuth_shuffle)
    elif function_name == 'mask_string_by_durstenfeld_shuffle':
#Apply mask_string_by_durstenfeld_shuffle
        return data['Name'].apply(mask_string_by_durstenfeld_shuffle)
    elif function_name == 'mask_string_by_replacement':
#Apply mask_string_by_replacement
        return data['Name'].apply(mask_string_by_replacement)
    elif function_name == 'mask_string_by_caesar_cipher':
#Apply mask_string_by_caesar_cipher
        return data['Name'].apply(mask_string_by_caesar_cipher)
    elif function_name == 'mask_string_by_salt_and_hash':
#Apply mask_string_by_salt_and_hash
        return data['Name'].apply(mask_string_by_salt_and_hash)
    elif function_name == 'mask_string_by_reverse_string':
#Apply mask_string_by_reverse_string
        return data['Name'].apply(mask_string_by_reverse_string)
    elif function_name == 'mask_string_by_substitute_chars':
#Apply mask_string_by_substitute_chars
        return data['Name'].apply(mask_string_by_substitute_chars)
    elif function_name == 'mask_string_by_replace_random_chars':
#Apply mask_string_by_replace_random_chars
        return data['Name'].apply(mask_string_by_replace_random_chars)
    elif function_name == 'mask_string_by_xor_chars':
#Apply mask_string_by_xor_chars
        return data['Name'].apply(mask_string_by_xor_chars)
    else:
#Invalid function name
        print(f"Invalid function name: {function_name}")

# Apply masking to the specified columns
for col_config in config['column_info']:
    if 'ApplyMasking' in col_config['col_type']:
        col_name = col_config['name']
        col_type = col_config['type']
        col_data = data[col_name]
        functions_to_apply = col_config['col_type']['ApplyMasking']

        for function_name in functions_to_apply:
            col_data = mask_string(function_name)

        data[col_name] = col_data

# Write the masked data to a new Excel file
output_file = config['output_file']
data.to_excel(output_file, index=False)
