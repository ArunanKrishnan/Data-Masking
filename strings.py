import pandas as pd
import hashlib
import os
import random

data=pd.read_excel(r'C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx')

# Define a function to mask a single name
def mask_string_by_asterisk(lst):
    masked_lst = []
    for name in lst:
        if isinstance(name, str):
            if len(name) > 2:
                masked_name = name[0] + (len(name)-2)*'*' + name[-1]
            else:
                masked_name = name
            masked_lst.append(masked_name)
        else:
            masked_lst.append(name)
    return masked_lst

def mask_string_by_knuth_shuffle(lst):
    masked_lst = [] 
    for s in lst:
        if isinstance(s, str):
            chars = list(s)
            for i in range(len(chars)-1, 0, -1):
                j = random.randint(0, i)
                chars[i], chars[j] = chars[j], chars[i]
            masked_lst.append(''.join(chars))
        else:
            masked_lst.append(s)
    return masked_lst

# Apply the knuth_shuffle function to the 'String Column' column
#data['Name']=data['Name'] = data['Name'].apply(mask_string_by_knuth_shuffle)

def mask_string_by_durstenfeld_shuffle(lst):
    masked_lst = []
    for s in lst:
        if isinstance(s, str):
            chars = list(s)
            for i in range(len(chars)-1, 0, -1):
                j = random.randint(0, i)
                chars[i], chars[j] = chars[j], chars[i]
            masked_lst.append(''.join(chars))
        else:
            masked_lst.append(s)
    return masked_lst

# Replace the original string column with the shuffled list
#data['Name']=data['Name'] = shuffled_column.apply(lambda x: ''.join(x))
replacement_names = ['John Doe', 'Jane Doe', 'Bob Smith', 'Alice Johnson', 'Michael Brown']
def mask_string_by_replacement(lst):
    masked_lst = []
    for name in lst:
        if name in replacement_names:
            masked_lst.append(random.choice(replacement_names))
        else:
            masked_lst.append(name)
    return masked_lst
#data['Name']=data['Name'].apply(mask_string_by_replacement)

def mask_strings_by_salt_and_hash(lst):
    """Encrypt a list of strings using salt and hash."""
    masked_lst = []
    for plaintext in lst:
        salt = os.urandom(4)
        salted_plaintext = salt + plaintext.encode()
        hashed_plaintext = hashlib.sha256(salted_plaintext).hexdigest()
        masked_lst.append(hashed_plaintext)
    return masked_lst

# Apply the salt and hash algorithm to the 'Name' column
#data['Name']= data['Name'].apply(lambda x: mask_string_by_salt_and_hash(x) if isinstance(x, str) else x)

def mask_strings_by_reverse_string(lst):
    """Reverse a list of strings."""
    masked_lst = []
    for plaintext in lst:
        reversed_plaintext = plaintext[::-1]
        masked_lst.append(reversed_plaintext)
    return masked_lst

# Apply the reversal algorithm to the 'Name' column
#data['Name']= data['Name'].apply(lambda x: mask_string_by_reverse_string(x) if isinstance(x, str) else x)

def mask_string_by_substitute_chars(plaintext_list):
    """Replace each character in a list of strings with a corresponding character from a mapping."""
    mapping = {'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T',
               'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P',
               'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G',
               'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z',
               'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N', 'Z': 'M'}
    return [''.join([mapping.get(c.upper(), c) for c in plaintext]) for plaintext in plaintext_list]

# Apply the substitution cipher algorithm to the 'Name' column
#data['Name']= data['Name'].apply(lambda x: mask_string_by_substitute_chars(x) if isinstance(x, str) else x)

def mask_string_by_replace_random_chars(plaintext_list):
    """Replace each character in a list of strings with a randomly selected character from a set."""
    char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    masked_list = []
    for plaintext in plaintext_list:
        masked_list.append(''.join([random.choice(char_set) if c.isalpha() else c for c in plaintext]))
    return masked_list

# Apply the random replacement algorithm to the 'Name' column
#data['Name']= data['Name'].apply(lambda x: mask_string_by_replace_random_chars(x) if isinstance(x, str) else x)
# Define a fixed key value for XOR operation
key = 2
def mask_string_by_xor_chars(plaintext):
    """Perform a bitwise XOR operation between each character in a string and a fixed key value."""
    return ''.join([chr(ord(c) ^ key) for c in plaintext])
# Apply the Bitwise XOR algorithm to the 'Name' column
data['Name'] = data['Name'].apply(lambda x: mask_string_by_xor_chars(x) if isinstance(x, str) else x)


