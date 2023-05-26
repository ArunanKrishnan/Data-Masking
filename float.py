import pandas as pd
import struct
import numpy as np
import random
import math

data = pd.read_excel(r'C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx')

def mask_float_by_str(weight): #56.64
    result = []
    for i in range(len(weight)):
        samp = str(weight[i])
        one = samp[0] #5
        two = samp[1]
        three = samp[-2]
        four = samp[-1]
        x = three + four + "." + one + two
        result.append(x)
    return result

# data['Weight'] = data['Weight'].apply(mask_float_by_str)
# print(data['Weight'])
def mask_float_by_precision(lst):
    print("In function mask_float_by_precision")
    print(lst)
    masked_lst = []
    factor = 0.1
    for x in lst:
        if isinstance(x, (int, float)):
            var = round(random.uniform(1.0, 100.0), 2)
            mask_value = round(7 * var * factor, 2)
            masked_lst.append(round(x + mask_value, 2))
        else:
            masked_lst.append(x)
    print(masked_lst)
    return masked_lst

#data['Weight'] = data['Weight'].apply(mask_float_by_precision)
def mask_float_by_add(lst):
    masked_lst = []
    factor = 0.1
    for x in lst:
        if isinstance(x, (int, float)):
            a = x + (random.uniform(0, 1) * x * factor)
            masked_lst.append(round(a, 2))
        else:
            masked_lst.append(x)
    return masked_lst

#data['Weight'] = data['Weight'].apply(mask_float_by_add)


def mask_float_by_rotate(x):
    bin_size = 2.56
    if isinstance(x, (float, int)):
        bin_midpoint = bin_size * (np.round(x / bin_size) + 0.5)
        return round(bin_midpoint, 2)
    else:
        return x.apply(lambda val: round(bin_size * (np.round(val / bin_size) + 0.5), 2))


data['Weight'] = data['Weight'].apply(mask_float_by_rotate)
#print(data['Weight'])
