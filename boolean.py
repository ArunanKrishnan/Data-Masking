import pandas as pd
data = pd.read_excel(r'C:\Users\kramal361\Downloads\masking-input (2).xlsx')
def mask_by_consonant(value):
    if value:
        return 'X'
    else:
        return 'O'
#data['Boolean'] = data['Boolean'].apply(mask_by_consonant)

def mask_by_word(value):
    if value:
        return 'Enabled'
    else:
        return 'Disabled'
#data['Boolean'] = data['Boolean'].apply(mask_by_word)    
def mask_by_value(value):
    if value:
        return 'T'
    else:
        return 'F'

data['Boolean'] = data['Boolean'].apply(mask_by_value) 

def mask_boolean_with_gates(value, gate):
    if gate == 'NOT':
        result = not value
    else:
        raise ValueError('Invalid gate type')
    
    if result:
        return '1'
    else:
        return '0'
data['Boolean'] = data['Boolean'].apply(lambda value: mask_boolean_with_gates(value, 'NOT'))


def mask_boolean_complex(value):
    mask = ['@', '#', '$', '%', '&', '*', '+', '-', '/', '=']
    if value:
        return mask
    else:
        return mask[F]
#data['Boolean'] = data['Boolean'].apply(mask_boolean_complex)
data.to_excel('masked_file.xlsx', index=False)
print(data['Boolean'])