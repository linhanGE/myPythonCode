print("# vtk DataFile Version 2.0")
from math import *
import sys

print("Generated by convert.py")
print("ASCII")
print("DATASET POLYDATA")

lines = open(sys.argv[1],'r').readlines()
lines = lines[9:]

print("POINTS", 2*len(lines), "float")
for line in lines:
    v = line.split(' ')
    print('{} {} {}'.format(v[0],v[1],v[2]))
    print('{} {} {}'.format(v[3],v[4],v[5]))

print("LINES", len(lines), 3*len(lines))
l = 0
for line in lines:
    v = line.split(' ')
    print('2 {} {}'.format(l, l+1))
    l = l + 2
    
print("POINT_DATA", 2*len(lines))
print("SCALARS ContactForce float 1")
print("LOOKUP_TABLE default")
for line in lines:
    v = line.split(' ')
    x = float(v[9])
    y = float(v[10])
    z = float(v[11])
    mag = sqrt(x*x+y*y+z*z)
    print('{}'.format(mag))
    print('{}'.format(mag))


