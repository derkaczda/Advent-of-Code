
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

def solve(input, num_pairs=1000):
    points = np.array(list(map(lambda x: np.array(x.split(','), dtype=int), input)))
    # compute the point-point distances
    distance_matrix = distance.pdist(points, 'euclidean')
    # compute all pdist-index to i,j mappings
    ij_indices = condensed_index_to_ij_pairs(points.shape[0])
    # only consider the num_pairs smallest distances
    k_smallest_indices = np.argsort(distance_matrix)[:num_pairs]
    circuits = {}
    circuit_counter = 0
    for idx in k_smallest_indices:
        i,j = map(int,ij_indices[idx])
        if i in circuits.keys() and j in circuits.keys():
            # if both indices are already part of
            # a circuit, we need to merge both circuits together
            circ_num = circuits[i]
            for k in circuits.keys():
                if circuits[k] == circ_num:
                    circuits[k] = circuits[j]
        elif j in circuits.keys() and not i in circuits.keys():
            # include new point to circuit
            circuits[i] = circuits[j]
        elif i in circuits.keys() and not j in circuits.keys():
            circuits[j] = circuits[i]
        else:
            # create a new circuit if both points
            # are currently not part of a circuit
            circuits[i] = circuits[j] = circuit_counter
            circuit_counter += 1
    # count the points in each circuit and take
    # the largest three
    counts = np.bincount(list(circuits.values()), minlength=circuit_counter)
    max_vals = counts[np.argpartition(counts, -3)[-3:]]
    return int(math.prod(max_vals))

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().splitlines()

    print(solve(lines))
