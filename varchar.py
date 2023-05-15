import pandas as pd
import numpy as np
import string
import random

df = pd.read_excel(r'C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx')

    # Define a function to shuffle a single string
def shuffle_string(s):
        """Shuffles the characters in a string randomly to create a new string with the same length.
    
    Args:
    column_name: The name of the column to shuffle.
    df: The DataFrame containing the column to shuffle.
    
    Returns:
    A new DataFrame with the shuffled column.
    """
        # Convert the string to a list of characters
        lst = list(s)
        # Shuffle the list randomly
        random.shuffle(lst)
        # Convert the shuffled list back to a string
        return ''.join(lst)

def random_replace_and_shuffle(s, p=0.5):
    mask = []
    """
    Randomly replaces some characters in the string with other random characters,
    and then shuffles the resulting string.

    Args:
        s (str): The input string to mask.
        p (float): The probability of replacing each character.

    Returns:
        str: The masked string.
    """
    # Convert s to a list of characters
    chars = list(s)

    # Iterate over the characters and randomly replace some of them
    for i in range(len(chars)):
        if random.random() < p:
            chars[i] = random.choice(string.printable)

    # Convert the list of characters back to a string and shuffle it
    masked = ''.join(chars)
    masked = ''.join(random.sample(masked, len(masked)))
    mask.append(masked)

    return mask   

def swap_pairs(s, swap_prob=0.5):
    """
    Randomly swap pairs of adjacent characters in a string.

    Parameters:
    s (str): The string to be modified.
    swap_prob (float): The probability of swapping each pair of adjacent characters. Default is 0.5.

    Returns:
    str: The modified string with pairs of adjacent characters swapped randomly.
    """
    chars = list(s)
    for i in range(0, len(chars) - 1, 2):
        if np.random.binomial(1, swap_prob) == 1:
            chars[i], chars[i+1] = chars[i+1], chars[i]
    return ''.join(chars)

def truncate_string(s, truncate_prob = 0.5):
    """
    Truncates a random portion of the string from the beginning, end, or middle.

    Parameters:
    s (str): The string to be modified.
    truncate_prob (float): Probability of truncating the string.

    Returns:
    str: The modified string with a random portion truncated.
    """
    if random.random() < truncate_prob:
        n = len(s)
        start_idx = random.randint(0, n-1)
        end_idx = random.randint(start_idx, n-1)
        return s[:start_idx] + s[end_idx+1:]
    else:
        return s
