import pandas as pd
import random
import string
import struct
import numpy as np
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

# define two floating-point numbers
def mask_val(val):
    a =76.89
    b =val
    # convert the numbers to their IEEE 754 binary representation
    a_bin = struct.pack('!f', a)
    b_bin = struct.pack('!f', b)
    # perform a bitwise AND operation on the binary strings

    result_bin = bytearray([x & y for x, y in zip(a_bin, b_bin)])
# convert the result back to a floating-point number
    result = struct.unpack('!f', result_bin)[0]
    return result


def mask_or(val):
    a =150
    b = 200
    # convert the numbers to their IEEE 754 binary representation
    a_bin = struct.pack('!f', a)
    b_bin = struct.pack('!f', b)
    # perform a bitwise AND operation on the binary strings

    result_bin = bytearray([x | y for x, y in zip(a_bin, b_bin)])
# convert the result back to a floating-point number
    result = struct.unpack('!f', result_bin)[0]
    return result

def float_bit_shift_and_mask(x, shift_amount, mask):
    # Convert the floating-point number to its IEEE 754 binary representation
    x_bin = bytearray(struct.pack('!f', x))

    # Shift the bits of the binary representation by the specified amount
    x_bin[0] <<= shift_amount

    # Mask the bits of the binary representation using the specified mask
    x_bin[1] &= mask

    # Convert the resulting binary string back to a floating-point number
    result = struct.unpack('!f', bytes(x_bin))[0]

    # Return the resulting floating-point number
    return result

# Define the shift amount and mask
shift_amount = 1
mask = 1111000011000

#data['Weight'] = data['Weight'].apply(float_bit_shift_and_mask, shift_amount=shift_amount, mask=mask)
#print(data['Weight'])

def float_rotate(x):
    r=150
    # Convert float to binary string
    bits = bin(struct.unpack('!I', struct.pack('!f', x))[0])
    # Remove '0b' prefix and pad with zeros
    bits = bits[2:].zfill(32)
    # Perform rotation using bitwise operations
    bits = bits[-r:] + bits[:-r]
    # Convert binary string back to float
    x_rotated = struct.unpack('!f', struct.pack('!I', int(bits, 2)))[0]
    return round(x_rotated,2)
#data['Weight']=data['Weight'].apply(float_rotate)
#print(data['Weight'])

def swap_floats_one(a,b):
    """
    Swaps the integer parts of two float values and returns them as a tuple.
    """
    a_int, a_dec = divmod(a, 9)
    b_int, b_dec = divmod(b, 2)
    return b_int + a_dec
# Apply the swap_floats() function to the 'Weight' column
# data['Weight'] = data['Weight'].apply(swap_floats_one,b=77)


def swap_floats(a):
    """
    Swaps the integer parts of two float values and returns them as a tuple.
    """
    a_int, a_dec = divmod(a, 2)
    return a_dec +a_int
# Apply the swap_floats() function to the 'Weight' column
#data['Weight'] = data['Weight'].apply(swap_floats)


def shuffle_column(weight):
    shuffled = np.random.permutation(weight)
    return shuffled
data['Weight'] = data['Weight'].apply(shuffle_column)
print(data['Weight'])







