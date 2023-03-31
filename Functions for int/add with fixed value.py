
# This method is about adding the fixed value with the data in that column
import pandas as pd

df = pd.read_excel(r'C:\Users\akrish451\Desktop\datamaskingproject\Data-Obfuscation-1\input files\masking-input.xlsx')
data_column = df['Employee ID']
# add a value or subtract a value with the value in the data
fixed_value = 1111
df['Updated Data'] = data_column + fixed_value

# save the updated DataFrame to a new excel file
#df.to_excel('filename_with_updated_data.xlsx', index=False)
print(df['Updated Data'])