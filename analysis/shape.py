#!/usr/bin/python
import numpy as np 
import sys
from geometry import *
from numpy import pi

vertexfile = sys.argv[1]
polyfile = sys.argv[2]


vertices = np.loadtxt(vertexfile)

polys = []

f = open(polyfile)
for line in f:
	linesplit = line.strip().split()
	n = len(linesplit)
	poly = np.zeros((n,2))
	for i,x in enumerate(linesplit):
		poly[i,:] = vertices[int(x),:]
	polys.append(poly)
f.close()


for poly in polys:
	n = len(poly)
	a = abs(get_area(n,poly))
	p = get_perimeter(n,poly)
	print a, p, p**2 / (4.*pi*a)


