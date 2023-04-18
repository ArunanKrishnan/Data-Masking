import pandas as pd
import math
import random

class DataMasker:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)
        
    def add_fixed_value(self, column_name, fixed_value):
        data_column = self.df[column_name]
        self.df[f'Updated {column_name}'] = data_column + fixed_value
        print(self.df)
        
    def divide_and_swap_column(self, column_name):
        numbers = self.df[column_name].tolist()
        length = len(numbers)
        if length % 2 == 0:
            half = length // 2
            first_half = numbers[:half]
            second_half = numbers[half:]
            swapped_numbers = second_half + first_half
            swapped_df = pd.DataFrame({f'Swapped {column_name}': swapped_numbers})
            self.df[f'Swapped {column_name}'] = swapped_numbers
            print(swapped_df)
        else:
            print("Error: List length must be even")

    def multiply_and_subtract(self, column_name):
        column_values = self.df[column_name]
        result_values = []
        for value in column_values:
            random_number = random.uniform(0, 1)
            result = round(value - (value * random_number))
            result_values.append(result)
        self.df[f'Multiplied and Subtracted {column_name}'] = pd.Series(result_values)
        print(self.df[f'Multiplied and Subtracted {column_name}'].tolist())

    def shuffle_column_numbers(self, column_name):
        column_values = self.df[column_name]
        rounded_numbers = [math.ceil(num) for num in column_values]
        indexes = list(range(len(column_values)))
        random.shuffle(indexes)
        shuffled_numbers = [rounded_numbers[index] for index in indexes]
        self.df[f'Shuffled {column_name}'] = shuffled_numbers
        print(shuffled_numbers)

    def shuffle_digits(self, column_name):
        column_values = self.df[column_name]
        result_values = []
        for value in column_values:
            digits_list = [int(digit) for digit in str(value)]
            random.shuffle(digits_list)
            result_value = int("".join(map(str, digits_list)))
            result_values.append(result_value)
        self.df[f'Shuffled Digits {column_name}'] = pd.Series(result_values)
        print(self.df[f'Shuffled Digits {column_name}'].tolist())

    def xor_with_random_and(self):
        xor_results = []
        for number in self.df['Employee ID']:
            random_value = random.randint(1, 1000)
            and_result = number & random_value
            xor_result = number ^ and_result
            xor_results.append({'Number': number, 'XOR': xor_result})
        result = pd.DataFrame(xor_results)
        print(result)
        
    def xor_with_random(self):
        xor_results = []
        for number in self.df['Employee ID']:
            random_value = random.randint(1, 1000)
            or_result = number | random_value
            xor_result = number ^ or_result
            xor_results.append({'Number': number, 'XOR': xor_result})
        result = pd.DataFrame(xor_results)
        print(result)

# Example usage
file_path = r'C:\Users\akrish451\Desktop\datamaskingproject\Data masking\Data-Masking\DM 2.0\Data-Masking\data\masking-input.xlsx'
data_masker = DataMasker(file_path)

data_masker.add_fixed_value('Employee ID', 1111)
data_masker.divide_and_swap_column('Employee ID')
data_masker.multiply_and_subtract('Employee ID')
data_masker.shuffle_column_numbers('Employee ID')
data_masker.shuffle_digits('Employee ID')
data_masker.xor_with_random_and()
data_masker.xor_with_random()

