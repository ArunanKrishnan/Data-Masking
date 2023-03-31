import pandas as pd
import random


df = pd.read_excel(r'C:\Users\akrish451\Desktop\datamaskingproject\Data-Obfuscation-1\input files\masking-input.xlsx')
col_name = 'Employee ID'


power_of_two = 2 ** random.randint(1, 10)


df[col_name] = df[col_name].apply(lambda x: x + power_of_two)

# Update the Excel file with the new values
#with pd.ExcelWriter('example.xlsx') as writer:
#    df.to_excel(writer, index=False)


print("Original values:", column_values.tolist())
print("Result values:", result_values)