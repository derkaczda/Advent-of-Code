
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

    def all_in_same_circuit():
        # if we only have one unique circuit id then
        # we are done
        return len(np.unique(list(circuits.values()))) == 1

    points = np.array(list(map(lambda x: np.array(x.split(','), dtype=int), input)))
    # compute the point-point distances
    distance_matrix = distance.pdist(points, 'euclidean')
    # compute all pdist-index to i,j mappings
    ij_indices = condensed_index_to_ij_pairs(points.shape[0])
    # only consider the num_pairs smallest distances
    k_smallest_indices = np.argsort(distance_matrix)
    circuits = {}
    for i in range(points.shape[0]):
        circuits[i] = i
    for idx in k_smallest_indices:
        i,j = map(int,ij_indices[idx])
        if i in circuits.keys() and j in circuits.keys():
            # merge both circuits together
            circ_num = circuits[i]
            for k in circuits.keys():
                if circuits[k] == circ_num:
                    circuits[k] = circuits[j]

        if all_in_same_circuit():
            return int(points[i][0] * points[j][0])
    return 0

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().splitlines()

    print(solve(lines))
