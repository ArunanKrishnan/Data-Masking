import pandas as pd
input_file = r'C:\Users\sethir919\Desktop\project\masking-input.xlsx'
data = pd.read_excel(input_file)
import random
import string


def generate_random_string(length):
    x = ''.join(random.choice(string.digits) for _ in range(2))
    y = ''.join(random.choice(string.digits) for _ in range(2))
    
    return (x +'.'+ y)

data['Weight'] = data['Weight'].apply(lambda x: generate_random_string(x))
data.to_excel('output_file_generate.xlsx', index=False)
                                      
print(data['Weight'])