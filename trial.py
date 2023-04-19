'''import json

# Load JSON file into dictionary
with open('cc_sky_data_masking.json', 'r') as f:
    data = json.load(f)
    print(data) '''

import json
import pandas as pd
#from float import mask_float_by_str
input_file = r'C:\Users\sethir919\Desktop\masking project\Data-Obfuscation\data\masking-input.xlsx'
data = pd.read_excel(input_file)

# Read the JSON input from a file or from a string
json_input = '''{
  "function": "mask_float_by_str",
  "column_info": [
    {
      "name": "Weight",
      "type": "float",
      "mode": "REQUIRED",
      "col_type": {
        "ApplyMasking": "mask_float_by_str"
      } 
    }
  ]
}'''

input_data = json.loads(r'C:\\Users\\sethir919\\Desktop\\masking project\\cc_sky_data_masking.json')

with open('C:\Users\sethir919\Desktop\masking project\Data-Obfuscation\trial.json', 'r') as f:
    data = json.load(f)

# Get the function name and column information from the input data
function_name = input_data['mask_float_by_str']
input_data = data['input_file']
column_info = input_data['Weight']

# Apply the function to the specified columns
for column in column_info:
    if 'ApplyMasking' in column['Weight']:
        column_data = {data['Weight']}  # Get your data for the column here
        masked_data = mask_float_by_str(column_data)
        print(f"Masked data for {column['Weight']}: {masked_data}")
output_data = globals()[function_name](input_data)
print(output_data)

'''
        with open('C:\Users\sethir919\Desktop\masking project\Data-Obfuscation\trial.json', 'r') as f:
    data = json.load(f)

function_name = data['Weight']
input_data = data['input_file']
output_data = globals()[function_name](input_data)
print(output_data) '''
