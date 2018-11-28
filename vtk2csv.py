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
	id=[]
	vx=[]
	vy=[]
	vz=[]
	fx=[]
	fy=[]
	fz=[]
	f_dragx=[]
	f_dragy=[]
	f_dragz=[]

	state = 0 # 1=coords 2=vertices 3=average velocities 4=volumefraction 5=radius 6=pressure

	i = 0
	with open(filename) as f:
		for line in f:
			s = line.strip('\n').split(' ')

			if s[0] == 'POINTS':
				state = 1
				n = int(s[1])
				i = 0
				continue
				
			if s[0] == 'VERTICES' or s[0] == 'POINT_DATA' or s[0] = 'FIELD':
				state = 0
				i = 0
				continue
				
			if s[0] == 'id' :
				f.readline() # just ignore the lookup_table line
				state = 2
				i = 0
				continue	

			if s[0] == 'v':
				f.readline() # just ignore the lookup_table line
				state = 3
				i = 0
				continue
				
			if s[0] == 'f':
				f.readline() # just ignore the lookup_table line
				state = 4
				i = 0
				continue
				
			if s[0] == 'f_dragforce[1-3]':
				f.readline() # just ignore the lookup_table line
				state = 5
				i = 0
				continue

			if state == 1:
				x.append(float(s[0]))
				y.append(float(s[1]))
				z.append(float(s[2]))
				if i == n:
					state = 0
				i = i + 1
					
			if state == 2:
				id.append(float(s[0]))
				if i == n:
					state = 0
				i = i + 1
						
			if state == 3:
				vx.append(float(s[0]))
				vy.append(float(s[1]))
				vz.append(float(s[2]))
				if i == n:
					state = 0
				i = i + 1
						
			if state == 4:
				fx.append(float(s[0]))
				fy.append(float(s[1]))
				fz.append(float(s[2]))
				if i == n:
					state = 0
				i = i + 1
			
			if state == 5:
				f_dragx.append(float(s[0]))
				f_dragy.append(float(s[1]))
				f_dragz.append(float(s[2]))
				if i == n:
					state = 0
				i = i + 1
			

	return x,y,z,id,vx,vy,vz,fx,fy,fz,f_dragx,f_dragy,f_dragz

filename = glob.glob('*.vtk')
# filename = os.path.splitext(filename)[0]
def natural_sort(l): 
	convert = lambda text: int(text) if text.isdigit() else text.lower() 
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
	return sorted(l, key = alphanum_key)
filename = natural_sort(filename)

for i in filename:
	x,y,z,vx,vy,vz,vol,r,p = convertFile(i)
	k = os.path.splitext(i)[0] 
	with open("%s.txt"%(k),'a') as f:
		for j in range(len(x)):
			f.write("%s %s %s %s %s %s %s %s %s %s %s %s %s\n"%(str(x[j]),str(y[j]),str(z[j]),str(vx[j]),str(vy[j]),str(vz[j]),str(id[j]),str(fx[j]),str(fy[j]),str(fz[j]),str(f_dragx[j]),str(f_dragy[j]),str(f_dragz[j])))


