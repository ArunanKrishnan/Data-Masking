import pandas as pd
import numpy as np
from numpy import random
# Load the input Excel file

data = pd.read_excel(r'C:\Users\sethir919\Desktop\project\masking-input.xlsx')
def some(weight):
    i=1
    l=[]
    while i==1:
        r=(random.randint(10))
        if r not in l:
            l.append(r)
            return weight+r
        break

data["Weight"]=data["Weight"].apply(some)
data.to_excel('output_file_add.xlsx', index=False)
print(data['Weight'])