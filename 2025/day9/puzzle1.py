
import os.path as osp

import numpy as np
from scipy.spatial import distance
import math

def condensed_index_to_ij_pairs(N):
    """
    Generates the (i, j) pairs for all k in the condensed distance matrix.
    N: The number of observations/points.
    """

    # Get the indices from the upper triangle (i < j)
    # The mask is N x N, where True corresponds to the upper triangle elements.
    mask = np.triu(np.ones(N, dtype=bool), k=1)

    # Get the i, j coordinates where the mask is True
    i_indices, j_indices = np.where(mask)

    return np.column_stack((i_indices, j_indices))

def solve(input):
    points = np.array(list(map(lambda x: np.array(x.split(','), dtype=int), input)))
    # compute the point-point distances
    distance_matrix = distance.pdist(points, 'euclidean')
    # compute all pdist-index to i,j mappings
    ij_indices = condensed_index_to_ij_pairs(points.shape[0])
    # sort the distances
    k_smallest_indices = np.argsort(distance_matrix)

    max_area = 0
    for idx in reversed(k_smallest_indices):
        i,j = map(int,ij_indices[idx])
        x_width = max(points[i][0], points[j][0]) - min(points[i][0], points[j][0]) +1
        y_width = max(points[i][1], points[j][1]) - min(points[i][1], points[j][1]) +1
        area = x_width * y_width
        if area > max_area:
            max_area = area

    return max_area

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().splitlines()

    print(solve(lines))