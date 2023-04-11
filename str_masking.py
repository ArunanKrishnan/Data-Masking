import pandas as pd
import random
#import input data
df = pd.read_excel(r'C:\Users\kramal361\Desktop\datamaskingproject\Data-Obfuscation-2\masking-input.xlsx')
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
print(df['Email address'])
