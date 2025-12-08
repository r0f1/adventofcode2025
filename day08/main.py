from math import prod
from operator import itemgetter

import numpy as np
from scipy.cluster.hierarchy import DisjointSet
from scipy.spatial.distance import pdist, squareform

with open("input.txt") as f:
    coords = [[int(i) for i in x.split(",")] for x in f]

n_nodes = len(coords)
distances = sorted(np.ndenumerate(squareform(pdist(coords))), key=itemgetter(1))[n_nodes::2]

clustering = DisjointSet(list(range(n_nodes)))
for idx, ((n1, n2), _) in enumerate(distances):
    clustering.merge(n1, n2)
    if idx == 1000:
        print(prod(sorted([len(c) for c in clustering.subsets()])[-3:]))

    if clustering.n_subsets == 1:
        print(coords[n1][0] * coords[n2][0])
        break
