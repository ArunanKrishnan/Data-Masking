import pandas as pd
import math
import random


file_path =r'C:\Users\akrish451\Desktop\datamaskingproject\Data-Obfuscation-1\input files\masking-input.xlsx'
df = pd.read_excel(file_path)


column_name = 'Employee ID' 
column_values = df[column_name]


rounded_numbers = [math.ceil(num) for num in column_values]


indexes = list(range(len(column_values)))
random.shuffle(indexes)


shuffled_numbers = [rounded_numbers[index] for index in indexes]
print(df)