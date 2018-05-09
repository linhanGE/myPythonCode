import sys, math
import glob
import numpy as np, pandas as pd
import re
import os

def convertFile(filename):
    # Read the file line by line

	x=[]
	y=[]
	z=[]
	r=[]

	state = 0 # 1=coords 2=radius 3=id 0=ignore

	i = 0
	with open(filename) as f:
		for line in f:
			s = line.strip('\n').split(' ')

			if s[0] == 'POINTS':
				state = 1
				n = int(s[1])
				i = 0
				continue

			if s[0] == 'SCALARS' and s[1] == 'radius':
				f.readline() # just ignore the lookup_table line
				state = 2
				i = 0
				continue

			#print(state, s)

			if state == 1:
				x.append(float(s[0]))
				y.append(float(s[1]))
				z.append(float(s[2]))
				i=i+1
				if i == n:
					state = 0
					
			if state == 2:
				r.append(float(s[0]))
				i = i + 1
				if i == n:
					state = 0
	return x,y,z,r



filename = glob.glob('*.vtk')
# filename = os.path.splitext(filename)[0]
def natural_sort(l): 
	convert = lambda text: int(text) if text.isdigit() else text.lower() 
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
	return sorted(l, key = alphanum_key)
filename = natural_sort(filename)

for i in filename:
	x,y,z,r = convertFile(i)
	k = os.path.splitext(i)[0] 
	with open("%s.csv"%(k),'a') as f:
		for j in range(len(x)):
			f.write("%s %s %s %s \n"%(str(x[j]),str(y[j]),str(z[j]),str(r[j])))


