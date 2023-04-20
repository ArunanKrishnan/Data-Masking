import json
import pandas as pd
import struct
import numpy as np

# Load the JSON configuration file
with open('cc_sky_data_masking.json', 'r') as f:
    config = json.load(f)

# Load the input data from an Excel file
input_file = config["input_file"]
data = pd.read_excel(input_file) 

# Define a function to mask a single name
def mask_float_by_str(weight): #56.64
    samp=str(weight)
    one = samp[0]
    two=samp[1]
    three=samp[-2]
    four= samp[-1]
    result = three+four+"."+one+two
    return  result
fun1=data['Weight'].apply(mask_float_by_str)

def mask_float_by_precision(weight):
    """
    Mask a float value by replacing the last `precision` digits with `mask_value`.
    :param value: the float value to be masked
    :param mask_value: the value to replace the masked digits
    :param precision: the number of digits to be masked
    :return: the masked float value
    """
    precision=3
    factor = 2 * precision #20 
    mask_value=7*int(weight * factor)
    masked_value = int(weight * factor) # get the integer part before the decimal
    rand=str(mask_value) * precision
    masked_value = round(float(str(masked_value) + '.' + rand),2) # append the mask_value
    result=masked_value%100
    return result
fun2=data['Weight'].apply(mask_float_by_precision)
#print(data['Weight'])

# define two floating-point numbers
def mask_float_by_add(weight):
    a =weight
    b =45.67
    # convert the numbers to their IEEE 754 binary representation
    a_bin = struct.pack('!f', a)
    b_bin = struct.pack('!f', b)
    # perform a bitwise AND operation on the binary strings
    result_bin = bytearray([x & y for x, y in zip(a_bin, b_bin)])
# convert the result back to a floating-point number
    result = struct.unpack('!f', result_bin)[0]
    return result
fun3=data['Weight'].apply(mask_float_by_add)
#print(data['Weight'])

def mask_float_by_or(weight):
    a =150
    b =weight
    # convert the numbers to their IEEE 754 binary representation
    a_bin = struct.pack('!f', a)
    b_bin = struct.pack('!f', b)
    # perform a bitwise OR operation on the binary strings
    result_bin = bytearray([x | y for x, y in zip(a_bin, b_bin)])
# convert the result back to a floating-point number
    result = struct.unpack('!f', result_bin)[0]
    return result
fun4=data['Weight'].apply(mask_float_by_or)
#print(data['Weight'])

def mask_float_by_shift(x):
    # Define the shift amount and mask
    shift_amount = 1
    mask = 1111000011000
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
fun5=data['Weight'].apply(mask_float_by_shift)

def mask_float_by_rotate(x):
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
fun6=data['Weight'].apply(mask_float_by_rotate)
#print(data['Weight'])

def mask_float_by_swap1(a):
    b=77
    """
    Swaps the integer parts of two float values and returns them as a tuple.
    """
    a_int, a_dec = divmod(a, 9)
    b_int, b_dec = divmod(b, 2)
    return b_int + a_dec
# Apply the swap_floats() function to the 'Weight' column
fun7= data['Weight'].apply(mask_float_by_swap1)

def mask_float_by_swap2(weight):
    """
    Swaps the integer parts of two float values and returns them as a tuple.
    """
    a_int, a_dec = divmod(weight, 2)
    return a_dec +a_int
fun8=data['Weight'].apply(mask_float_by_swap2)

def mask_float(function_name):
    if function_name == 'mask_float_by_str':
# Apply mask_float_by_str function
        return data['Weight'].apply(mask_float_by_str)
    elif function_name == 'mask_float_by_precision':
# Apply mask_float_by_swap1 function
        return data['Weight'].apply(mask_float_by_precision)
    elif function_name == 'mask_float_by_add':
# Apply mask_float_by_swap1 function
        return data['Weight'].apply(mask_float_by_add)
    elif function_name == 'mask_float_by_or':
# Apply mask_float_by_swap1 function
        return data['Weight'].apply(mask_float_by_or)
    elif function_name == 'mask_float_by_shift':
# Apply mask_float_by_swap1 function
        return data['Weight'].apply(mask_float_by_shift)
    elif function_name == 'mask_float_by_rotate':
# Apply mask_float_by_swap1 function
        return data['Weight'].apply(mask_float_by_rotate)
    elif function_name == 'mask_float_by_swap1':
# Apply mask_float_by_swap1 function
        return data['Weight'].apply(mask_float_by_swap1)
    elif function_name == 'mask_float_by_swap2':
# Apply mask_float_by_swap1 function
        return data['Weight'].apply(mask_float_by_swap2)
    else:
# Invalid function name
        print(f"Invalid function name: {function_name}")

# Apply masking to the specified columns
for col_config in config['column_info']:
    if 'ApplyMasking' in col_config['col_type']:
        col_name = col_config['name']
        col_type = col_config['type']
        col_data = data[col_name]
        functions_to_apply = col_config['col_type']['ApplyMasking']

        for function_name in functions_to_apply:
            col_data = mask_float(function_name)

        data[col_name] = col_data

# Write the masked data to a new Excel file
output_file = config['output_file']
data.to_excel(output_file, index=False)

