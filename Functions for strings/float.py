import pandas as pd
# Load the input Excel file
input_file = r'C:\Users\sethir919\Desktop\project\masking-input.xlsx'
data = pd.read_excel(input_file)

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
print(masked_value)
