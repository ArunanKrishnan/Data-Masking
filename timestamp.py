import pandas as pd
from datetime import datetime, timedelta
from datetime import datetime
import random
import numpy as np

df = pd.read_excel(r'C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx')

# Define the substitution function
def substitute_date(date):
    """
    Generates a random date between January 1, 1900 and December 31, 2050 to substitute the given date.

    Parameters:
        date (pd.Timestamp, datetime.datetime, or str): The date to be substituted.

    Returns:
        pd.Timestamp or pd.Series: The substituted random date between January 1, 1900 and December 31, 2050.
    """
    start_date = datetime(1900, 1, 1)
    end_date = datetime(2050, 12, 31)

    if isinstance(date, pd.Timestamp):
        date = date.to_pydatetime()
    elif isinstance(date, str):
        date = pd.to_datetime(date).to_pydatetime()
    elif isinstance(date, pd.Series):
        return date.apply(substitute_date)
    elif not isinstance(date, datetime):
        raise ValueError("Input should be a pd.Timestamp, datetime.datetime, or str object.")

    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    timestamp = pd.Timestamp(random_date, unit='D')
    formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_timestamp

def radin_date(date):
    """
    Adds a random offset of up to 3 days to the given date.

    Parameters:
        date (pd.Timestamp, datetime.datetime, or str): The date to be masked.

    Returns:
        str or pd.Series: The masked date with a random offset of up to 3 days.
    """
    if isinstance(date, pd.Timestamp):
        date = date.to_pydatetime()
    elif isinstance(date, str):
        date = pd.to_datetime(date).to_pydatetime()
    elif isinstance(date, pd.Series):
        return date.apply(radin_date)
    elif not isinstance(date, datetime):
        raise ValueError("Input should be a pd.Timestamp, datetime.datetime, or str object.")

    fuzz = timedelta(days=random.randint(-3, 3))
    var = date + fuzz
    formatted_timestamp = var.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_timestamp
# df['Time Stamp'] = df['Time Stamp'].apply(random_date)
# print(df['Time Stamp'])


def add_date(date):
    """
    Adds the first day of the year as a mask to the given date.

    Parameters:
        date (pd.Timestamp, datetime.datetime, or str): The date to be masked.

    Returns:
        pd.Timestamp or pd.Series: The masked date with the year set to the first day of the year.
    """
    if isinstance(date, pd.Timestamp):
        date = date.to_pydatetime()
    elif isinstance(date, str):
        date = pd.to_datetime(date).to_pydatetime()
    elif isinstance(date, pd.Series):
        return date.apply(add_date)
    elif not isinstance(date, datetime):
        raise ValueError("Input should be a pd.Timestamp, datetime.datetime, or str object.")

    year = date.year
    mask = datetime(year=year, month=1, day=1)
    timestamp = pd.Timestamp(mask, unit='D')
    formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_timestamp


def shift_hours(timestamp, hours=3):
    if isinstance(timestamp, str):
        timestamp = pd.to_datetime(timestamp)
    elif isinstance(timestamp, pd.Series):
        return timestamp.apply(lambda x: shift_hours(x, hours=3))
    
    shifted_timestamp = timestamp + pd.DateOffset(hours=3)
    formatted_timestamp = shifted_timestamp.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_timestamp


def random_shift(df):
    if isinstance(df, pd.Series):
        return df.apply(random_shift)
    elif isinstance(df, pd.DataFrame):
        df = df.apply(pd.to_datetime, errors='ignore')
        mask = ~df.isnull()
        random_shifts = np.random.randint(-30, 31, size=df.shape)
        df_shifted = df + pd.to_timedelta(random_shifts, unit='D') * mask
        df_shifted = df_shifted.applymap(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(x) else None)
        return df_shifted
    else:
        return df


def interval_mask(df):
    if isinstance(df, pd.Series):
        return df.apply(interval_mask)
    elif isinstance(df, pd.DataFrame):
        mask = df['Time Stamp'] > pd.Timestamp('2022-01-01')
        df.loc[mask, 'Time Stamp'] = df.loc[mask, 'Time Stamp'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
        return df
    else:
        return df