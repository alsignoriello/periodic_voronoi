#!/usr/bin/python
import numpy as np


# Assumes points are between 0 and 1 
def tile_points(points, N):

	# 9 tiles surrounding individual coordinates
	point_tile = np.zeros((9 * N, 2)) 

	# original coordinates
	point_tile[:N] = points

	# upper left 
	point_tile[N:2*N, 0] = points[:,0] - 1
	point_tile[N:2*N, 1] = points[:,1] + 1

	# directly above
	point_tile[2*N:3*N, 0] = points[:,0]
	point_tile[2*N:3*N, 1] = points[:,1] + 1

	# upper right
	point_tile[3*N:4*N, 0] = points[:,0] + 1
	point_tile[3*N:4*N, 1] = points[:,1] + 1

	# right
	point_tile[4*N:5*N, 0] = points[:,0] + 1
	point_tile[4*N:5*N, 1] = points[:,1]

	# lower right
	point_tile[5*N:6*N, 0] = points[:,0] + 1
	point_tile[5*N:6*N, 1] = points[:,1] - 1

	# under
	point_tile[6*N:7*N, 0] = points[:,0]  
	point_tile[6*N:7*N, 1] = points[:,1] - 1

	# lower left
	point_tile[7*N:8*N,0] = points[:,0] - 1
	point_tile[7*N:8*N,1] = points[:,1] - 1

	# left 
	point_tile[8*N:,0] = points[:,0] - 1
	point_tile[8*N:,1] = points[:,1]

	return point_tile
