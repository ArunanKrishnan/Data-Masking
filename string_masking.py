import pandas as pd

# Load the input Excel file
input_file = r'C:\Users\sethir919\Desktop\project\masking-input.xlsx'
data = pd.read_excel(input_file)

# Define a function to mask a single name
def mask_name(name):
    first_letter = name[0]
    last_letter = name[-1]
    masked_name = (len(name)-2)*'*'
    return  masked_name 

# Mask the names in the 'Name' column
data['Name'] = data['Name'].apply(mask_name)
data.to_excel('output_file_mask.xlsx', index=False)

# Define a function to mask a single name
def mask_name(Name):
    if Name[0]=='A':
        return("Emily")
    elif Name[0]=='B':
        return("Elena")
    elif Name[0]=='C':
        return("Komal")
    elif Name[0]=='D':
        return("Gilbert")
    elif Name[0]=='E':
        return("Ram")
    elif Name[0]=='F':
        return("Helina")
    elif Name[0]=='G':
        return("Reshkanth")
    elif Name[0]=='H':
        return("Pughal")
    elif Name[0]=='I':
        return("Yalighar")
    elif Name[0]=='J':
        return("Vanmathi")
    elif Name[0]=='K':
        return("Jeswanth")
    elif Name[0]=='L':
        return("kirthok")
    elif Name[0]=='M':
        return("Vikki")
    elif Name[0]=='N':
        return("Kousal")
    elif Name[0]=='O':
        return("Arthik")
    elif Name[0]=='P':
        return("Manoj")
    elif Name[0]=='Q':
        return("Relin")
    elif Name[0]=='R':
        return("Anishk")
    elif Name[0]=='S':
        return("Rajesh")
    elif Name[0]=='T':
        return("Elena")
    elif Name[0]=='U':
        return("Elena")
    elif Name[0]=='V':
        return("Elena")
    elif Name[0]=='W':
        return("Elena")
    elif Name[0]=='X':
        return("Elena")
    elif Name[0]=='Y':
        return("Elena")
    elif Name[0]=='Z':
        return("Elena")


# Mask the names in the 'Name' column
data['Name'] = data['Name'].apply(mask_name)
data.to_excel('output_file_char.xlsx', index=False)
print(data['Name'])

from mimesis import Person
import pandas as pd
input_file = r'C:\Users\sethir919\Desktop\project\masking-input.xlsx'
data = pd.read_excel(input_file)
person = Person()
fake_names = [person.full_name() for i in range(10)]

data = pd.DataFrame({'Name': fake_names})
data.to_excel('output_file_random.xlsx', index=False)
print(data)
