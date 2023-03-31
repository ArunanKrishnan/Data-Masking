import pandas as pd
import random


file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data-Obfuscation-1\input files\masking-input.xlsx'
df = pd.read_excel(file_path)


column_name = "Employee ID" 
column_values = df[column_name]


result_values = []


for value in column_values:
    
    random_number = random.uniform(0, 1)
    
    
    result = round(value - (value * random_number))
    
    
    result_values.append(result)


print("Original values:", column_values.tolist())
print("Result values:", result_values)