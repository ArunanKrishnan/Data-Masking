import pandas as pd
import numpy as np
from datetime import datetime, timedelta
df= pd.read_excel(r'C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx')


def date_truncation(date_column, portion):
     
    """
    Removes a random portion of the date (day, month, or year).
    :param date_column: Pandas series object containing date values.
    :param portion: Portion to remove from the date. Choose from 'day', 'month', or 'year'.
    :return: Pandas series object with truncated date values.
    """
    if portion not in ['day', 'month', 'year']:
        raise ValueError("Portion must be 'day', 'month', or 'year'.")
    
    # Extract year, month, and day from the date
    year = date_column.dt.year
    month = date_column.dt.month
    day = date_column.dt.day
    
    # Replace the specified portion with NaN
    if portion == 'day':
        day = np.nan
    elif portion == 'month':
        month = np.nan
    else:
        year = np.nan
    
    # Combine the year, month, and day components back into a date
    truncated_date = pd.to_datetime(pd.DataFrame({'year': year, 'month': month, 'day': day}))
    
    return truncated_date

df['Date of Birth']=df['Date of Birth'].apply(date_truncation)
print(df['Date of Birth'])
   
