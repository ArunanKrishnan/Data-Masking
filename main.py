import json
import float
import strings
import varchar_one
import integer_one
import pandas as pd

def main():
    #Load the JSON file specified by the end user
    with open('end_user.json', 'r') as f:
        user_input = json.load(f)

    #Load the Excel file using Pandas
    data=pd.read_excel(r"C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx")

    #Loop through each column in the JSON file
    for column in user_input:
        col_name = column['name']
        col_type = column['type']
        apply_masking = column['col_type']['ApplyMasking']
        #print(col_name)
        #Select the appropriate masking function based on the column type
        if col_type == 'FLOAT':
            if 'mask_float_by_str' in apply_masking:
                data[col_name] = float.mask_float_by_str(data[col_name])
            if 'mask_float_by_precision' in apply_masking:
                data[col_name] = float.mask_float_by_precision(data[col_name])
            if 'mask_float_by_add' in apply_masking:
                data[col_name] = float.mask_float_by_add(data[col_name])
            if 'mask_float_by_rotate' in apply_masking:
                data[col_name] = float.mask_float_by_rotate(data[col_name])

        elif col_type == 'STRING':
            if 'mask_string_by_asterisk' in apply_masking:
                data[col_name] = strings.mask_string_by_asterisk(data[col_name])
            if 'mask_string_by_knuth_shuffle' in apply_masking:
                data[col_name] = strings.mask_string_by_knuth_shuffle(data[col_name])
            if 'mask_string_by_durstenfeld_shuffle' in apply_masking:
               data[col_name] = strings.mask_string_by_durstenfeld_shuffle(data[col_name])
            if 'mask_string_by_replacement' in apply_masking:
                data[col_name] = strings.mask_string_by_replacement(data[col_name])
            if 'mask_strings_by_salt_and_hash' in apply_masking:
                data[col_name] = strings.mask_strings_by_salt_and_hash(data[col_name])
            if 'mask_strings_by_reverse_string' in apply_masking:
                data[col_name] = strings.mask_strings_by_reverse_string(data[col_name])
            if 'mask_string_by_substitute_chars' in apply_masking:
                data[col_name] = strings.mask_string_by_substitute_chars(data[col_name])
            if 'mask_string_by_replace_random_chars' in apply_masking:
                data[col_name] = strings.mask_string_by_replace_random_chars(data[col_name])
            if 'mask_string_by_xor_chars' in apply_masking:
                data[col_name] = strings.mask_string_by_xor_chars(data[col_name])    

        elif col_type == 'INT':
            if 'mask_consonants' in apply_masking:
                data[col_name] = integer_one.mask_consonants(data[col_name])
            if 'mask_reversal' in apply_masking:
                data[col_name] = integer_one.mask_reversal(data[col_name])
            if 'mask_soundex' in apply_masking:
                data[col_name] = integer_one.mask_soundex(data[col_name])
            if 'randomized_offset_masking' in apply_masking:
                data[col_name] = integer_one.randomized_offset_masking(data[col_name])
                '''
            if 'extract_first_digit' in apply_masking:
                data[col_name] = integer_one.extract_first_digit(data[col_name])
            if 'mask_pincode' in apply_masking:
                data[col_name] = integer_one.mask_pincode(data[col_name])
            if 'remind_first_last_swap_between' in apply_masking:
                data[col_name] = integer_one.remind_first_last_swap_between(data[col_name])
            if 'complex_mask_pincode' in apply_masking:
                data[col_name] = integer_one.complex_mask_pincode(data[col_name])
            if 'mask_integer' in apply_masking:
                data[col_name] = integer_one.mask_integer(data[col_name])
                '''

        elif col_type == 'VARCHAR':
            if 'shuffle_email' in apply_masking:
                data[col_name] = varchar_one.shuffle_email(data[col_name])
            if 'mask_email' in apply_masking:
                data[col_name] = varchar_one.mask_email(data[col_name])
            if 'pad_email' in apply_masking:
                data[col_name] = varchar_one.pad_email(data[col_name])
            if 'obfuscate_email' in apply_masking:
                data[col_name] = varchar_one.obfuscate_email(data[col_name])

    #Save the masked Excel file
    data.to_excel('output.xlsx', index=False)
    
if __name__ == '__main__':
    main()

