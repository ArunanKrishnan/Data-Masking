import pandas as pd
import hashlib
import random
import string

class ExcelMasker:
    def __init__(self, input_file):
        self.df = pd.read_excel(input_file)

    def substitute_numbers(self, column_name, num_to_str_dict, str_to_num_dict):
        self.df[column_name] = self.df[column_name].apply(lambda x: str(x) if isinstance(x, int) else x)
        self.df[column_name] = self.df[column_name].replace(num_to_str_dict)
        self.df[column_name] = self.df[column_name].replace(str_to_num_dict)
        return self
    
    def hide_data(self, column_name):
        self.df[column_name] = ""
        return self

    def hash_data(self, column_name):
        self.df[column_name] = self.df[column_name].apply(lambda x: hashlib.sha256(str(x).encode('utf-8')).hexdigest())
        return self
    
    def modify_integers(self, column_name):
        random_str = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
        prime = 1000000007
        self.df[column_name] = self.df[column_name].apply(lambda x: (x + int(random_str)) % prime)
        return self
    
    def threshold_values(self, column_name):
        self.df['Half_Value'] = self.df[column_name].apply(lambda x: (sum(1 for c in str(x) if c.isdigit())/2) + 
                                                                (sum(1 for c in str(x) if c.isalpha())/2))
        self.df['Opposite_Value'] = self.df[column_name].apply(lambda x: ''.join(random.choices(string.ascii_letters + string.digits, k=10)))
        self.df.loc[self.df['Half_Value'] > 0.5, 'Opposite_Value'] = self.df[column_name]
        return self
    
    def mask_values(self, column_name):
        self.df[column_name] = self.df[column_name].apply(lambda x: ''.join(['0' if c.isalpha() else str(int(c)*2) for c in x]))
        return self
    
    def fisher_yates_shuffle(self, column_name):
        values = self.df[column_name].values.tolist()
        n = len(values)
        for i in range(n-1, 0, -1):
            j = random.randint(0, i)
            values[i], values[j] = values[j], values[i]
        self.df[column_name] = values
        return self
    
    def to_excel(self, output_file):
        self.df.to_excel(output_file, index=False)


em = ExcelMasker(r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\DM 2.0\Data-Masking\data\masking-input.xlsx')
em.substitute_numbers('Passport Number', {1: 'one'}, {'one': 1})
em.hash_data('Passport Number')
em.mask_values('Passport Number')
em.to_excel('output_file.xlsx')
