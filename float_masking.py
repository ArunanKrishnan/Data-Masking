import pandas as pd

# Load the input Excel file
input_file = r'C:\Users\sethir919\Desktop\project\masking-input.xlsx'
data = pd.read_excel(input_file)

# Define a function to mask a single name
def mask_name(weight):
    samp=str(weight)
    one = samp[0]
    two=samp[1]
    three=samp[-2]
    four= samp[-1]
    masked_name = three+four+"."+one+two
    return  masked_name 

# Mask the names in the 'Name' column
data['Weight'] = data['Weight'].apply(lambda x: mask_name(x))
data.to_excel('output_file_shuffle.xlsx', index=False)
print(data['Weight'])

import random
import string


def generate_random_string(length):
    x = ''.join(random.choice(string.digits) for _ in range(2))
    y = ''.join(random.choice(string.digits) for _ in range(2))
    
    return (x +'.'+ y)

data['Weight'] = data['Weight'].apply(lambda x: generate_random_string(x))
data.to_excel('output_file_ranint.xlsx', index=False)
          
print(data['Weight'])

def mask_float_values(input_list, mask_char='*', mask_start=0, mask_end=None):
    """
    Mask float values in input_list with mask_char from mask_start to mask_end indices.
    If mask_end is not provided, it defaults to the end of the input_list.
    """
    if mask_end is None:
        mask_end = len(input_list)
    masked_list = input_list.copy()
    for i in range(mask_start, mask_end):
        if isinstance(masked_list[i], float):
            masked_list[i] = mask_char
    return masked_list
masked_list = data["Weight"].apply(mask_float_values)
secmasked=masked_list.apply()
data.to_excel('output_file_param.xlsx', index=False)
print(masked_list)

def mask_float(value):#3,.5
    """
    Mask a float value by replacing the last `precision` digits with `mask_value`.
    :param value: the float value to be masked
    :param mask_value: the value to replace the masked digits
    :param precision: the number of digits to be masked
    :return: the masked float value
    """
    precision=8
    factor = 10 * precision #20 
    mask_value=7*int(value * factor)
    masked_value = int(value * factor) # get the integer part before the decimal
    rand=str(mask_value) * precision
    masked_value = round(float(str(masked_value) + '.' + rand),2) # append the mask_value
    return masked_value%100
masked_value = data["Weight"].apply(mask_float)
secmasked=masked_value.apply()
data.to_excel('output_file_float.xlsx', index=False)
print(masked_value)

