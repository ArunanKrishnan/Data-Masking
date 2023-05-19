import pandas as pd
from datetime import datetime, timedelta
import random
df = pd.read_excel(r'C:\\Users\\sethir919\\Desktop\\masking project\\Data-Obfuscation\\data\\masking-input.xlsx')

# Define the substitution function
def substitute_date(date):
    mask = []
    start_date = datetime(1900, 1, 1)
    end_date = datetime(2050, 12, 31)
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    mask.append(random_date)
    return mask
# Define the fuzzing function
def radin_date(date):
    mask = []
    fuzz = timedelta(days=random.randint(-3,3))
    var = date + fuzz
    mask.append(var)
    return mask

# Define the bucketing function
def add_date(date):
    masked = []
    year = date.year
    mask = datetime(year=year, month=1, day=1)
    masked.append(mask)
    return masked

def shift_hours(timestamp, hours=3):
    shifted_time = pd.to_datetime(timestamp) + timedelta(hours=hours)
    return [shifted_time]

# Apply the substitution function to the date column
#df['Time Stamp'] = df['Time Stamp'].apply(add_date)
#print(df['Time Stamp'])
