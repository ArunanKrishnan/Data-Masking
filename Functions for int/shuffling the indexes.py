import pandas as pd
import random
# This method shuffles the the indexes of the paticular data in that column

file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data-Obfuscation-1\input files\masking-input.xlsx'
df = pd.read_excel(file_path)
column_name = "Employee ID"  
column_values = df[column_name]
result_values = []
for value in column_values:
    
    digits_list = [int(digit) for digit in str(value)]
    
    
    random.shuffle(digits_list)
    
    
    result_value = int("".join(map(str, digits_list)))
    
    
    result_values.append(result_value)


print("Original values:", column_values.tolist())
print("Result values:", result_values)