#!/usr/bin/python
import numpy as np
from scipy.spatial import Voronoi
import sys



np.random.seed([1938420])


N = int(sys.argv[1])

# generate random points
points = np.random.uniform(0, 1, size=(N,2))

# generate voronoi diagram
vor = Voronoi(points)


# write vertices
np.savetxt("vertices.txt", vor.vertices)

# write edges
f = open("edges.txt", "w+")
for edge in vor.ridge_vertices:
	f.write("%d \t %d\n" % (edge[0], edge[1]))
f.close()

# write polygons
f = open("polygons.txt", "w+")
for region in vor.regions:
	if len(region) != 0:
		for index in region:
			f.write("%d\t" % index)
		f.write("\n")
f.close()

