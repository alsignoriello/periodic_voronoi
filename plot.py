#!/usr/bin/python
import numpy as np 
import matplotlib.pyplot as plt
import sys


def plot_points(vertices):
	for x,y in vertices:
		plt.scatter(x, y, color="c")
	return


def plot_edges(vertices, edges):
	for i1,i2 in edges:
		if i1 != -1 and i2 != -1:
			x1,y1 = vertices[i1]
			x2,y2 = vertices[i2]
			plt.plot([x1,x2], [y1,y2], color="m")
	return

def plot_polygons(vertices, polys):
	for poly in polys:
		for i,index in enumerate(poly):

			if index == poly[-1]:
				if index != -1 and poly[0] != -1:
					x1,y1 = vertices[index]
					x2,y2 = vertices[poly[0]]
					plt.plot([x1,x2], [y1,y2], color="r")
			else:
				if index != -1 and poly[i+1] != -1:
					x1,y1 = vertices[index]
					x2,y2 = vertices[poly[i+1]]
					plt.plot([x1,x2], [y1,y2], color="r")
	return

def save_plot(outfile):

	# remove tick marks
	frame = plt.gca()
	frame.axes.get_xaxis().set_ticks([])
	frame.axes.get_yaxis().set_ticks([])

	# save and close plot
	plt.savefig(outfile)
	plt.close()
	return



def read_poly(file):
	indices = []
	f = open(file)
	for line in f:
		cell_indices = []
		linesplit = line.strip().split("\t")
		for i in linesplit:
			cell_indices.append(int(i))
		indices.append(cell_indices)
	f.close()
	return indices



# filename for plot
outfile = sys.argv[1]


vertex_file = "vertices.txt"
edge_file = "edges.txt"
poly_file = "polygons.txt"


vertices = np.loadtxt(vertex_file)
edges = np.loadtxt(edge_file, dtype=int)
polys = read_poly(poly_file)


plot_points(vertices)
# plot_polygons(vertices, polys)
plot_edges(vertices, edges)

save_plot(outfile)




