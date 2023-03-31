import pandas as pd
path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data-Obfuscation-1\input files\masking-input.xlsx'
df = pd.read_excel(path)

def fixedint():
    integer_value = df['Employee ID']
    fixed_value = 1111
    result = integer_value + fixed_value
    return result
#df['Employee ID']=df['Employee ID'].apply()
print(df)
#column_name = 'Employee ID' 

#numbers = df['Employee ID'].tolist()
#added_numbers = fixedint(numbers)
#added_df = pd.DataFrame({'added Numbers': added_numbers})
#data['Employee ID']=data['Employee ID'].apply(swapped_df)

#added_df.to_excel('op_fixedint.xlsx', index=False)

#print("Original values:", column_values.tolist())
#print("Result values:", result_values)
#added_df.to_excel('op_addwithFV.xlsx', index=False)