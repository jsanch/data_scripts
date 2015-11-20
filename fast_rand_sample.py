# fast_rand_sample.py

import random as rand

input_filename = "grants.csv" # must be in the same dir as script. 
output_filename = "out.csv" 
random_sample_size = 10000 #Desired number of lines for the sample


f = open(input_filename)

count = 0

for i, line in enumerate(f):
	RANDNUM= rand.randint(1, 10)
	if (i % RANDNUM) == 0 :
		print line
		count = count + 1

print 'COUNT' , count