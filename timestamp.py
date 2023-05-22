import pandas as pd
from datetime import datetime, timedelta
from datetime import datetime
import random

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
    return pd.Timestamp(random_date)

# Define the fuzzing function
def random_date(date):
    """
    Adds a random offset of up to 3 days to the given date.

    Parameters:
        date (pd.Timestamp, datetime.datetime, or str): The date to be masked.

    Returns:
        pd.Timestamp or pd.Series: The masked date with a random offset of up to 3 days.
    """
    if isinstance(date, pd.Timestamp):
        date = date.to_pydatetime()
    elif isinstance(date, str):
        date = pd.to_datetime(date).to_pydatetime()
    elif isinstance(date, pd.Series):
        return date.apply(random_date)
    elif not isinstance(date, datetime):
        raise ValueError("Input should be a pd.Timestamp, datetime.datetime, or str object.")

    fuzz = timedelta(days=random.randint(-3, 3))
    var = date + fuzz
    return pd.Timestamp(var)

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
    return pd.Timestamp(mask)


def shift_hours(timestamp, hours=3):
    """
    Shifts the timestamp by the specified number of hours.

    Parameters:
        timestamp (str or pd.Timestamp): The timestamp to be shifted.
        hours (int): The number of hours to shift the timestamp by. Default is 3.

    Returns:
        pd.Timestamp: The shifted timestamp.
    """
    if isinstance(timestamp, str):
        # If timestamp is a string, convert it to a pd.Timestamp object
        timestamp = pd.to_datetime(timestamp)
    shifted_time = timestamp + timedelta(hours=hours)
    return shifted_time


# Apply the substitution function to the date column
#df['Time Stamp'] = df['Time Stamp'].apply(substitute_date)
#print(df['Time Stamp'])
