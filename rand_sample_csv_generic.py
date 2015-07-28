import pandas as pd
import numpy as np 
import csv 

input_filename = "in.csv" # must be in the same dir as script. 
output_filename = "out.csv" 
random_sample_size = 10000 #Desired number of lines for the sample

# Open the desired file
f = open(input_filename) 
# Gets the number of lines in the file. 
### NOTE: If the total number of lines is known, it's preferable to plug that number in, as 
###       it would cut script runtime by a lot. 
num_lines = sum(1 for line in f) 
print num_lines
# Numpy magic
lines2skip = (np.random.choice(np.arange(1,num_lines+1), (num_lines - random_sample_size), replace=False))
# Read in, while skipping lines. 
df = pd.read_csv(input_filename, skiprows=lines2skip)  
# Save to disk
df.to_csv(output_filename, quoting=csv.QUOTE_ALL, index=False)
  
