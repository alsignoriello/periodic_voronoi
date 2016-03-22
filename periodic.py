#!/usr/bin/python
import numpy as np


# get vertices inside original bounds
# assumes box length is 1
def get_vertices(tile_vertices):
	vertices = []
	index_map = {}

	for i,(x,y) in enumerate(tile_vertices):
		if x >= 0 and x <= 1.:
			if y >= 0 and y <= 1.:
				curr_indx = len(vertices)
				index_map[i] = curr_indx
				vertices.append((x,y))
	return np.array(vertices), index_map




# get edges with respect to periodic boundaries
# vertices and edges are from voronoi with tiled coordinates
def get_edges(vertices, edges, index_map):
	e = []
	for edge in edges:
		i1 = edge[0]
		i2 = edge[1]

		# Case 1: i1 and i2 in index map
		# Append indices for vertex list wrt periodic bounds
		if i1 in index_map and i2 in index_map:
			e.append((index_map[i1],index_map[i2]))
			e.append((index_map[i2],index_map[i1]))

		# Case 2: neither in index map
		# Do nothing

		# Case 3: i1 or i2 in index map
		# 		  but not both 
		# Because of periodicity, this edge needs to have a 
		# connecting edge that wraps around
		if i1 in index_map and i2 not in index_map:
			# find the vertex that it "wraps around" to
			# v = vertex in plane
			v = np.array(vertices[i1])
			# v1 = vertex out of plane
			v1 = np.array(vertices[i2])

			# print v1
			if v1[0] < 0:
				v1[0] = 1 + v1[0]

			if v1[0] > 1:
				v1[0] = v1[0] - 1

			if v1[1] < 0:
				v1[1] = 1 + v1[1]

			if v1[1] > 1:
				v1[1] = v1[1] - 1

			# # # find index of this vertex 
			for key in index_map:
				if abs(vertices[key][0] - v1[0]) < 10**-6:
					e.append((index_map[i1], index_map[key]))


		# include this IF you want duplicate edges...
		if i1 not in index_map and i2 in index_map:
			# find the vertex that it "wraps around" to
			# v = vertex in plane
			v = np.array(vertices[i2])
			# v1 = vertex out of plane
			v1 = np.array(vertices[i1])

			# print v1
			if v1[0] < 0:
				v1[0] = 1 + v1[0]

			if v1[0] > 1:
				v1[0] = v1[0] - 1

			if v1[1] < 0:
				v1[1] = 1 + v1[1]

			if v1[1] > 1:
				v1[1] = v1[1] - 1

			# # find index of this vertex 
			for key in index_map:
				if abs(vertices[key][0] - v1[0]) < 10**-6:
					e.append((index_map[i2], index_map[key]))

	return e




# add indices mapping to new vertices outside of bounds
def get_new_index_map(vertices, v, index_map):

	for i,(x,y) in enumerate(vertices):
		x1 = x
		y1 = y

		if x < 0 and x > -1.:
			x1 = x + 1.

		if x > 1 and x < 2.:
			x1 = x - 1.

		if y < 0 and y > -1.:
			y1 = y + 1.

		if y > 1 and y < 2.:
			y1 = y - 1.


		# look up new x,y in list
		for j,(x2,y2) in enumerate(v):
			if abs(x1 - x2) < 10**-6:
				if abs(y1 - y2) < 10**-6:
					index_map[i] = j

	return index_map


# get polygons
def get_polygons(regions, index_map, vertices):

	polygons = []

	for region in regions:
		count = 0
		poly = []
		for index in region:
			if index in index_map:
				count += 1
				poly.append(index_map[index])
		if count == len(region) and count != 0:
			polygons.append(cell)


	# remove duplicates
	new_polygons = []
	for poly in polygons:
		add = True
		for poly2 in new_polygons:
			if sorted(poly) == sorted(poly2):
				add = False
		if add == True:
			new_polygons.append(poly)


	return new_polygons