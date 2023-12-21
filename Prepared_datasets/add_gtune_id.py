#!/usr/bin/env python

import pandas as pd
import numpy as np
from obspy import UTCDateTime

filename='Comprehensive_Catalog.csv'

df = pd.read_csv(filename)

unix_time = df.UNIX_TIME.to_numpy()

gtuneid = np.zeros(len(unix_time))


for i, time in enumerate(unix_time):
	gtuneid[i] = UTCDateTime(time).strftime("%YY") + \
							 UTCDateTime(time).strftime("%m") + \
							 UTCDateTime(time).strftime("%d") + \
							 UTCDateTime(time).strftime("%H") + \
							 UTCDateTime(time).strftime("%M")

	
