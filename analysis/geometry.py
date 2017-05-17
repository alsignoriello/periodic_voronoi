#!/usr/bin/python
import numpy as np 
from numpy import pi, sqrt, cos, sin

# Area of a polygon
def get_area(Nv,vertices):

	cross = 0.
	for i in range(0,Nv):
		x1,y1 = vertices[i,:]
		if i != Nv - 1:
			x2,y2 = vertices[i+1,:]
		if i == Nv - 1:
			x2,y2 = vertices[0,:]
		cross += ((x1 * y2) - (x2 * y1))
	return 0.5 * cross

# Perimeter of a polygon
def get_perimeter(Nv,vertices):

	lengths = np.zeros(Nv)

	for i in range(0,Nv):

		x1,y1 = vertices[i,:]
		if i !=  Nv - 1:
			x2,y2 = vertices[i+1,:]
		if i == Nv - 1:
			x2,y2 = vertices[0,:]

		d = sqrt((x2-x1)**2 + (y2-y1)**2)
		lengths[i] = d
	return np.sum(lengths)