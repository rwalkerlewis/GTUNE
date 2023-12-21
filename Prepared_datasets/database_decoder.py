 #!/usr/bin/env python


import pickle

filename = 'final_llnl_uncut_data.pkl'

with open(filename, 'rb') as file:
	data = pickle.load(file)
