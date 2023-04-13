import pandas as pd
import hashlib
import os
import random

#import input data
data = pd.read_excel(r'C:\Users\kramal361\Desktop\datamaskingproject\Data-Obfuscation-2\masking-input.xlsx')
def shuffle_email(email):
    '''Shuffles the local-part of an email address using a random shuffling algorithm.
    Args:
        email (str): The email address to be shuffled.
    Returns:
        str: The shuffled email address.
    Raises:
        ValueError: If the input email address is not valid.'''

    email_parts = email.split('@')
    username = email_parts[0]
    domain = email_parts[1]
    shuffled_username = ''.join(random.sample(username, len(username)))
    shuffled_email = shuffled_username + '@' + domain
    return shuffled_email

# Define the truncation function to mask email addresses
def mask_email(email):
    """Mask the username part of an email address by replacing all but the first 3 characters with an ellipsis.
    Parameters:
        email (str): A string representing an email address in the standard format with a single '@' character separating the username and domain parts.
    Returns:
        str: A masked email address with the same domain part as the input, but with the username part truncated and replaced with an ellipsis.
    Example:
        >>> mask_email('john.doe@example.com')
        'joh...@example.com' """
    username, domain = email.split('@')
     # maksing the username part to the first 3 characters and add
    truncated_username = username[:3] + '...'
    # Combine the masked username and domain parts to form the masked email address
    masked_email = truncated_username + '@' + domain
    return masked_email


# Define the padding function to mask email addresses
def pad_email(email):
    """
    Obfuscate the username part of an email address by replacing vowels and consonants with random digits.
    Parameters:
        email (str): A string representing an email address in the standard format with a single '@' character separating the username and domain parts.
    Returns:
        str: An obfuscated email address with the same domain part as the input, but with the username part replaced with random digits for each vowel or consonant character.
    Example:
        >>> obfuscate_email('jane.doe@example.com')
        'j8n6.d48@ex1mpl5.com'
    """
    # Define a list of characters to choose
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
     # Add random characters to the email address
    char=''
    for i in range(5):
        char += random.choice(chars)
        #it chooses from the second character and do masking
    pad_email = email[:1] + '....' + char+ email[-10:]
    return pad_email

#Define the function to mask email addresses
def obfuscate_email(email):
    """
    Obfuscate the username part of an email address by replacing vowels and consonants with random digits.
    Parameters:
        email (str): A string representing an email address in the standard format with a single '@' character separating the username and domain parts.
    Returns:
        str: An obfuscated email address with the same domain part as the input, but with the username part replaced with random digits for each vowel or consonant character.
    Example:
        >>> obfuscate_email('jane.doe@example.com')
        'j8n6.d48@ex1mpl5.com'
    """
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

# Define the cryptography function to mask email addresses

'''
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)
def encrypt_email(email):
    """Encrypts the input email using Fernet encryption method.
Args:
    email (str): The email address to be encrypted.
Returns:
    bytes: The encrypted email address as bytes."""
    encrypted_email = fernet.encrypt(email.encode())
    return encrypted_email

df['Email address'] = df['Email address'].apply(obfuscate_email)
print(df['Email address'])'''

# Define a function to mask a single name
def mask_name(name):
    first_letter = name[0]
    last_letter = name[-1]
    masked_name = (len(name)-2)*'*'
    return  masked_name 

def knuth_shuffle(s):
    chars = list(s)
    for i in range(len(chars)-1, 0, -1):
        j = random.randint(0, i)
        chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)

# Apply the knuth_shuffle function to the 'String Column' column
#data['Name'] = data['Name'].apply(knuth_shuffle)
def durstenfeld_shuffle(s):
    chars = list(s)
    for i in range(len(chars)-1, 0, -1):
        j = random.randint(0, i)
        chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)

# Convert the string column to a list and shuffle it using the durstenfeld_shuffle function
#shuffled_column = data['Name'].apply(lambda x: list(x)).apply(durstenfeld_shuffle)

# Replace the original string column with the shuffled list
#data['Name'] = shuffled_column.apply(lambda x: ''.join(x))


# Define a list of replacement names
replacement_names = ['John Doe', 'Jane Doe', 'Bob Smith', 'Alice Johnson', 'Michael Brown']

# Define a function to mask names in a string
def masking_name(name):
    if name in replacement_names:
        return random.choice(replacement_names)
    else:
        return name

def caesar_cipher(plaintext, key):
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
#data['Name'] = data['Name'].apply(lambda x: caesar_cipher(x, key) if isinstance(x, str) else x)

import pandas as pd


def salt_and_hash(plaintext):
    """Encrypt a string using salt and hash."""
    salt = os.urandom(4)
    salted_plaintext = salt + plaintext.encode()
    hashed_plaintext = hashlib.sha256(salted_plaintext).hexdigest()
    return hashed_plaintext

# Apply the salt and hash algorithm to the 'Name' column
#data['Name'] = data['Name'].apply(lambda x: salt_and_hash(x) if isinstance(x, str) else x)

def reverse_string(plaintext):
    """Reverse a string."""
    return plaintext[::-1]

# Apply the reversal algorithm to the 'Name' column
#data['Name'] = data['Name'].apply(lambda x: reverse_string(x) if isinstance(x, str) else x)

def substitute_chars(plaintext):
    """Replace each character in a string with a corresponding character from a mapping."""
    mapping = {'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T',
               'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P',
               'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G',
               'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z',
               'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N', 'Z': 'M'}
    return ''.join([mapping.get(c.upper(), c) for c in plaintext])

# Apply the substitution cipher algorithm to the 'Name' column
#data['Name'] = data['Name'].apply(lambda x: substitute_chars(x) if isinstance(x, str) else x)

def replace_random_chars(plaintext):
    """Replace each character in a string with a randomly selected character from a set."""
    char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join([random.choice(char_set) if c.isalpha() else c for c in plaintext])

# Apply the random replacement algorithm to the 'Name' column
#data['Name'] = data['Name'].apply(lambda x: replace_random_chars(x) if isinstance(x, str) else x)

# Define a fixed key value for XOR operation
key = 2

def xor_chars(plaintext):
    """Perform a bitwise XOR operation between each character in a string and a fixed key value."""
    return ''.join([chr(ord(c) ^ key) for c in plaintext])

# Apply the Bitwise XOR algorithm to the 'Name' column
data['Name'] = data['Name'].apply(lambda x: xor_chars(x) if isinstance(x, str) else x)
print(data['Name'])


