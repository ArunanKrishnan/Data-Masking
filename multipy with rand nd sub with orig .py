import pandas as pd
import random

# This method is about multiply the column data with the random number and subracting it with the original value

file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data-Obfuscation-1\input files\masking-input.xlsx'
df = pd.read_excel(file_path)
column_name = "Employee ID" 
column_values = df[column_name]
result_values = []

# multipling the value with random numbers
for value in column_values:
    
    random_number = random.uniform(0, 1)
    
    # rounding off the value which we get

    result = round(value - (value * random_number))
    
    
    result_values.append(result)
print("Original values:", column_values.tolist())
print("Result values:", result_values)