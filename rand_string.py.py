from mimesis import Person
import pandas as pd
input_file = r'C:\Users\sethir919\Desktop\project\masking-input.xlsx'
data = pd.read_excel(input_file)
person = Person()
fake_names = [person.full_name() for i in range(10)]

data = pd.DataFrame({'Name': fake_names})
data.to_excel('output_file_random.xlsx', index=False)
print(data)




