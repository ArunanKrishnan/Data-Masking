import pandas as pd
# Load the input Excel file
input_file = r'C:\Users\sethir919\Desktop\project\masking-input.xlsx'
data = pd.read_excel(input_file)
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
