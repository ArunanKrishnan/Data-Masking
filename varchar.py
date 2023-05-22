import pandas as pd
import numpy as np
import string
import random

df = pd.read_excel(r'C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx')

def shuffle_string(s):
    """
    Shuffles the characters in a string randomly to create a new string with the same length.

    Args:
        s (str or pd.Series): The string or series of strings to shuffle.

    Returns:
        pd.Series: The shuffled strings.
    """
    if isinstance(s, str):
        # If s is a single string, convert it to a list of characters
        lst = list(s)
        # Shuffle the list randomly
        random.shuffle(lst)
        # Convert the shuffled list back to a string
        return ''.join(lst)
    elif isinstance(s, pd.Series):
        # If s is a series, apply the shuffling operation to each element
        return s.apply(lambda x: shuffle_string(x))
    else:
        raise ValueError("Input should be either a string or a pd.Series.")


# df['User ID'] = df['User ID'].apply(shuffle_string)
# print(df['User ID'])
def random_replace_and_shuffle(s, p=0.5):
    """
    Randomly replaces some characters in the string with other random characters,
    and then shuffles the resulting string.

    Args:
        s (str or pd.Series): The input string or series of strings to mask.
        p (float): The probability of replacing each character.

    Returns:
        str or pd.Series: The masked string or series of masked strings.
    """
    if isinstance(s, str):
        # If s is a single string, convert it to a list of characters
        chars = list(s)
        # Iterate over the characters and randomly replace some of them
        for i in range(len(chars)):
            if random.random() < p:
                chars[i] = random.choice(string.printable)
        # Convert the list of characters back to a string and shuffle it
        masked = ''.join(chars)
        masked = ''.join(random.sample(masked, len(masked)))
        return masked
    elif isinstance(s, pd.Series):
        # If s is a series, apply the masking operation to each element
        return s.apply(lambda x: random_replace_and_shuffle(x, p))
    else:
        raise ValueError("Input should be either a string or a pd.Series.")



def swap_pairs(s, swap_prob=0.5):
    """
    Randomly swap pairs of adjacent characters in a string or series of strings.

    Parameters:
        s (str or pd.Series): The string or series of strings to be modified.
        swap_prob (float): The probability of swapping each pair of adjacent characters. Default is 0.5.

    Returns:
        str or pd.Series: The modified string or series of modified strings with pairs of adjacent characters swapped randomly.
    """
    if isinstance(s, str):
        # If s is a single string, convert it to a list of characters
        chars = list(s)
        # Iterate over the characters and randomly swap adjacent pairs
        for i in range(0, len(chars) - 1, 2):
            if np.random.binomial(1, swap_prob) == 1:
                chars[i], chars[i + 1] = chars[i + 1], chars[i]
        return ''.join(chars)
    elif isinstance(s, pd.Series):
        # If s is a series, apply the swapping operation to each element
        return s.apply(lambda x: swap_pairs(x, swap_prob))
    else:
        raise ValueError("Input should be either a string or a pd.Series.")



def truncate_string(s, truncate_prob=0.5):
    """
    Truncates a random portion of the string from the beginning, end, or middle.

    Parameters:
        s (str or pd.Series): The string or series of strings to be modified.
        truncate_prob (float): Probability of truncating the string.

    Returns:
        str or pd.Series: The modified string or series of modified strings with a random portion truncated.
    """
    if isinstance(s, str):
        # If s is a single string, perform the truncation operation
        if random.random() < truncate_prob:
            n = len(s)
            start_idx = random.randint(0, n - 1)
            end_idx = random.randint(start_idx, n - 1)
            return s[:start_idx] + s[end_idx + 1:]
        else:
            return s
    elif isinstance(s, pd.Series):
        # If s is a series, apply the truncation operation to each element
        return s.apply(lambda x: truncate_string(x, truncate_prob))
    else:
        raise ValueError("Input should be either a string or a pd.Series.")
#df['User ID'] = df['User ID'].apply(truncate_string)
#print(df['User ID'])
