from mimesis import Person

import pandas as pd

# Load the input Excel file
input_file = r'C:\Users\sethir919\Desktop\project\masking-input.xlsx'
data = pd.read_excel(input_file)

person = Person()

fake_names = [person.full_name() for i in range(10)]

data = pd.DataFrame({'Name': fake_names})

print(data)




