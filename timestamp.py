import pandas as pd
import numpy as np
df = pd.read_excel(r'C:\Users\kramal361\Downloads\masking-input (2).xlsx')
def random_shift(dfs, max_shift=7):

    """

Randomly shifts time stamp data in a list of pandas DataFrame columns by a random number of days up to a specified maximum shift value.

Parameters:

- dfs (list of pandas.DataFrame): a list of DataFrames containing the time stamp data to be masked
- max_shift (int): the maximum number of days by which to randomly shift each time stamp (default: 7)
Returns:
- list of pandas.DataFrame: a list of masked DataFrames with the time stamp data shifted by a random amount
"""
# Iterate through each DataFrame in the list
    masked_dfs = []
    for df in dfs:
# Convert the time stamp column to a pandas DateTime format
        df = df.apply(pd.to_datetime, errors='ignore')
# Generate random shifts for each time stamp
        shifts = pd.TimedeltaIndex(np.random.randint(-max_shift, max_shift+1, size=len(df)), unit='d')
# Shift the time stamp columns by the random shifts
    for column in df.select_dtypes(include='datetime'):
        df[column] = pd.to_datetime(df[column]) + shifts
# Add the masked DataFrame to the list
    masked_dfs.append(df)
# Return the list of masked DataFrames
    return masked_dfs
# Define the DataFrame to operate on
df = pd.DataFrame({'Time Stamp': pd.date_range('2022-01-01', periods=10, freq='D')})
# Apply the random shift function to the DataFrame
masked_dfs = random_shift([df])
# Print the shifted DataFrame
print(masked_dfs[0]['Time Stamp'])

def interval_mask(df, start_date=None, end_date=None):

    """

Masks rows in a pandas DataFrame column with time stamps that fall within a specified time interval.
Parameters:
- df (pandas.DataFrame): a DataFrame containing the time stamp data to be masked
- start_date (str): a string in the format 'YYYY-MM-DD' specifying the start date of the time interval (default: None)
- end_date (str): a string in the format 'YYYY-MM-DD' specifying the end date of the time interval (default: None)
Returns:
- pandas.DataFrame: a masked DataFrame with rows containing time stamps in the specified interval masked
"""

# Convert the time stamp column to a pandas DateTime format

    df = df.apply(pd.to_datetime, errors='ignore')
 # Mask the rows containing time stamps within the specified interval (if start and end dates are specified)
    if start_date is not None and end_date is not None:
        mask = (df['Time Stamp'] >= start_date) & (df['Time Stamp'] <= end_date)
    df.loc[mask, 'Time Stamp'] = pd.NaT
# Return the masked DataFrame
    return df
# Define the DataFrame to operate on
df = pd.DataFrame({'Time Stamp': pd.date_range('2022-01-01', periods=10, freq='D')})
# Apply the interval mask function to the DataFrame with a specified time interval
masked_df = interval_mask(df, '2022-01-03', '2022-01-06')
# Print the masked DataFrame
print(masked_df)