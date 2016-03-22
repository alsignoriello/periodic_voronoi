#!/usr/bin/bash


HOME=/Users/Lexi/Documents/Ohern_2016/periodic_voronoi

N=$1
echo "N = "$N

folder="test"
# mkdir $folder
cd $folder

# run voronoi diagram without periodic boundaries
# python $HOME/voronoi.py $N

# plot voronoi diagram
# python $HOME/plot.py "voronoi.jpg"


# run voronoi diagram with periodic boundaries
python $HOME/periodic_voronoi.py $N

# plot voronoi diagram




