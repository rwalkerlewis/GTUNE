#!/usr/bin/env python

import pandas as pd
import numpy as np
from obspy import UTCDateTime

def month_code_to_number(month_code):
    """
    Convert a three-letter month abbreviation to a two-digit month number.

    Args:
    month_code (str): A three-letter abbreviation of a month (e.g., 'Jan', 'Feb', etc.).

    Returns:
    str: A two-digit string representing the month number ('01' for January, '02' for February, etc.),
         or 'Invalid' if the input is not a recognized month abbreviation.
    """
    # Dictionary mapping month abbreviations to their two-digit representations
    month_mapping = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
        'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
    }

    # Convert the month code to its two-digit representation
    return month_mapping.get(month_code.capitalize(), 'Invalid')



filename='Comprehensive_Catalog.csv'

df = pd.read_csv(filename)

#unix_time = df.UNIX_TIME.to_numpy()
unix_time = np.zeros(len(df))
gtuneid = [None] * len(unix_time)
mon_num = [None] * len(unix_time)
datetime_str = [None] * len(unix_time)


for i in np.arange(0, len(df)):
	mon_num[i] = month_code_to_number(df.MON[i])
	time = str(df.YEAR[i]) + '-' + mon_num[i] + '-' + f"{df.DAY[i]:02d}" + 'T' + df.TIME[i]
	datetime_str[i] = time

	gtuneid[i] = UTCDateTime(time).strftime("%Y") + \
							 UTCDateTime(time).strftime("%m") + \
							 UTCDateTime(time).strftime("%d") + \
							 UTCDateTime(time).strftime("%H") + \
							 UTCDateTime(time).strftime("%M")
	df.UNIX_TIME[i] = UTCDateTime(time).timestamp
df['GTUNE_ID'] = gtuneid
df.to_csv('Updated_Catalog.csv')



