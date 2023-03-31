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

