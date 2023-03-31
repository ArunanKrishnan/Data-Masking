import pandas as pd
# This method is about dividing the column into two halves swapping the two halves
data = pd.read_excel(r'C:\Users\akrish451\Desktop\datamaskingproject\Data-Obfuscation-1\input files\masking-input.xlsx')

# diving the columns into two halves

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

# swapping the two halves which we added

numbers = data['Employee ID'].tolist()
swapped_numbers = divide_and_swap(numbers)
swapped_df = pd.DataFrame({'Swapped Numbers': swapped_numbers})
#data['Employee ID']=data['Employee ID'].apply(swapped_df)

swapped_df.to_excel('op_divide&swap.xlsx', index=False)
#Print the original values and the results

