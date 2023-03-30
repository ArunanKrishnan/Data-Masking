import pandas as pd
data = pd.read_excel(r'C:\Users\akrish451\Desktop\datamaskingproject\Data-Obfuscation-1\masking-input.xlsx')

def divide_and_swap(numbers):   
    length = len(numbers)  
    if length % 2 == 0:     
        half = length // 2
        first_half = numbers[:half]
        second_half = numbers[half:]   
        numbers = second_half + first_half 
        return numbers
    else:
        return "Error: List length must be even"
column_name = 'Employee ID' 

numbers = data['Employee ID'].tolist()
swapped_numbers = divide_and_swap(numbers)
swapped_df = pd.DataFrame({'Swapped Numbers': swapped_numbers})
#swapped_df.to_excel('output_file_emp.xlsx', index=False)
# Print the original values and the results

