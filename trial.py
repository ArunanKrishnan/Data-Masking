'''import pandas as pd
import numpy as np

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(r'C:\Users\sethir919\Desktop\project\masking-input.xlsx')

# Shuffle the names in the 'Name' column
df['Name'] = np.random.permutation(df['Name'])

# Save the shuffled DataFrame to a new Excel file
df.to_excel('output_file.xlsx', index=False)'''

'''------------------
import numpy as np

def shuffle(user):
    data['User ID'] = np.random.permutation(data['User ID'])
    return user
data["User ID"]=data["User ID"].apply(shuffle)

print(data)
------------
def some(name):
    last_names = data['Name']
    fake_second_name = random.choice(last_names)
    return name
data["Name"]=data["Name"].apply(some)
print(data)'''

'''import pandas as pd
from faker import Faker

# Load the input Excel file
input_file = r'C:\Users\sethir919\Desktop\project\masking-input.xlsx'
data = pd.read_excel(input_file)

# Define a function to generate fake names
def generate_fake_name():
    fake = Faker()
    return fake.name()

# Replace the original names with fake names
data['Name'] = data['Name'].apply(lambda x: generate_fake_name())
print(data)'''
'''# Create a Faker instance
def some(name):
    fake = Faker()
    num_names = 10 
    fake_names = [(fake.first_name(), fake.last_name()) for _ in range(num_names)]
    df = pd.DataFrame(fake_names, columns=['First Name', 'Last Name'])
    data["Name"]=data["Name"].apply(name)
print(data)
'''
