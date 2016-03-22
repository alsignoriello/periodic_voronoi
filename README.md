# Periodic Voronoi

This simulates a voronoi diagram with periodic boundary conditions. In a voronoi diagram, the polygons on the boundaries are undefined. Adding periodic boundary conditions assures that every polygon in the voronoi diagram is well defined. This is accomplished by picking a set of points that you want to find the voronoi diagram of. Then, the same set of points is tiled around the current set such that there are 8 tiles that share at least one corner of with original tile. The voronoi algorithm is applied to the tiles points. Then, there will be duplicate polygons on the original boundaries of the set of points. The output is the 


<img src="https://github.com/alsignoriello/periodic_voronoi/blob/master/images/voronoi_periodic.jpg">


# Voronoi Diagram

A voronoi diagram partitions N points into convex polygons such that each polygon contains one point and the point is closer to its generating point than any other point. The delaunay triangulation is the dual to a voronoi diagram. The delaunay triangulation of a set of points is the triangulation that does not allow a point to be inside the circumcircle surrounding the triangle. This maximizes the minimum angle for every triangle in the triangulation. The voronoi diagram can be constructed from the delaunay triangulation by finding the perpendicular bisectors for every edge in the triangulation. 

http://mathworld.wolfram.com/DelaunayTriangulation.html

http://mathworld.wolfram.com/VoronoiDiagram.html


# Periodic Bounday Conditions 

Periodic boundary conditions assume that when you reach the maximum length of a box, you wrap back around to 0. 



# Running the Simulation

| Parameter | Definition | Range |
|-----------|------------|-------|
| N | number of generating points | any positive int |



sh run.sh [N]


vertices.txt
(x,y) coordinates for every vertex in the voronoi diagram

edges.txt
(index1, index2) indices for every edge between two vertices in the voronoi diagram

polygons.txt
(index0, index1, ... indexN) indices in counter-clockwise order that form every polygon in the voronoi diagram


# Requirements

numpy (1.8.1)

matplotlib (1.3.1)

scipy (0.14.0)
