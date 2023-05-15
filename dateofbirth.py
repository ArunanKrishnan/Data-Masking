import pandas as pd
import numpy as np
from datetime import datetime, timedelta
df= pd.read_excel(r'C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx')

def date_encoding(date_column, encoding_type="days_since_reference", reference_date=pd.to_datetime("1970-01-01")):
    """
    Encodes the date in a given pandas column as a numerical value based on a specified encoding type.

    Parameters:
    date_column (pandas Series): The column of dates to be encoded.
    encoding_type (str): The type of encoding to use. Options are "days_since_reference" (default), "weeks_since_year_start",
                         and "months_since_year_start".
    reference_date (pandas Timestamp): The reference date to use for the encoding. Default is January 1st, 1970.

    Returns:
    pandas Series: A new column of encoded date values.
    """
    if encoding_type == "days_since_reference":
        encoded_dates = (date_column - reference_date) / pd.Timedelta(days=1)
    elif encoding_type == "weeks_since_year_start":
        start_of_year = date_column.dt.year.apply(str) + "-01-01"
        days_since_year_start = (date_column - pd.to_datetime(start_of_year)).dt.days
        encoded_dates = (days_since_year_start / 7).astype(int)
    elif encoding_type == "months_since_year_start":
        start_of_year = date_column.dt.year.apply(str) + "-01-01"
        months_since_year_start = (date_column.dt.to_period('M') - pd.to_datetime(start_of_year).dt.to_period('M')).astype(int)
        encoded_dates = months_since_year_start
    else:
        raise ValueError("Invalid encoding type specified. Options are 'days_since_reference', 'weeks_since_year_start', or 'months_since_year_start'.")
    
    return encoded_dates
df['Date of Birth']=df['Date of Birth'].apply(date_encoding)
print(df['Date of Birth'])