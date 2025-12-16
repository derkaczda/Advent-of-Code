
import os.path as osp

import numpy as np
from scipy.spatial import distance
import math
from functools import reduce

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
    def is_part_of_convex_hull(point):
        # mask_x_upper = np.logical_or(convex_hull[:,0] >= point[0], convex_hull[:,1] == point[1])
        # mask_x_lower = np.logical_and(convex_hull[:,0] <= point[0], convex_hull[:,1] == point[1])
        # mask_y_upper = np.logical_or(convex_hull[:,1] >= point[1], convex_hull[:,0] == point[0])
        # mask_y_lower = np.logical_and(convex_hull[:,1] <= point[1], convex_hull[:,0] == point[0])
        # return mask_x_lower.any() and mask_x_upper.any() and mask_y_lower.any() and mask_y_upper.any()

        # check if between two vertical edges
        # i.e. there needs to be two edges such that e1.x <= point.x <= e2.x
        mask_vertical = np.logical_and(np.logical_and(convex_hull[:,0] == 1, convex_hull[:,1] <= point[0]),  convex_hull[:,2] >= point[0])
        mask_vertical = np.logical_and(np.logical_and(mask_vertical, convex_hull[:,3] >= point[1]), convex_hull[:,3] <= point[1])
        # furthermore, the point needs to be enclosed by
        # two horizontal edges
        mask_horizontal = np.logical_and(np.logical_and(convex_hull[:,0] == 0, convex_hull[:,2] <= point[1]), convex_hull[:,3] >= point[1])
        mask_horizontal = np.logical_and(np.logical_and(mask_horizontal, convex_hull[:,1] >= point[0]), convex_hull[:,1] <= point[0])
        # both statements need to be true
        return mask_horizontal.any() and mask_vertical.any()



    points = np.array(list(map(lambda x: np.array(x.split(','), dtype=int), input)))
    # compute the point-point distances
    distance_matrix = distance.pdist(points, 'euclidean')
    # compute all pdist-index to i,j mappings
    ij_indices = condensed_index_to_ij_pairs(points.shape[0])
    # sort the distances
    # k_smallest_indices = np.argsort(distance_matrix)

    convex_hull = []
    for i, p in enumerate(points):
        next_idx = (i+1) % points.shape[0]
        neighbor = points[next_idx]
        is_vertical_edge = True if p[1] == neighbor[1] else False
        if is_vertical_edge:
            x1, x2 = min(p[0], neighbor[0]), max(p[0], neighbor[0])
            y = p[1]
            convex_hull.append([int(is_vertical_edge), x1,x2,y])
        else:
            x = p[0]
            y1, y2 = min(p[1], neighbor[1]), max(p[1], neighbor[1])
            convex_hull.append([int(is_vertical_edge), x, y1, y2])
            # target_min = min(n[0], p[0]) if p[1] == n[1] else min(n[1], p[1])
            # target_max = max(n[0], p[0]) if p[1] == n[1] else max(n[1], p[1])
            # constant = int(n[1]) if p[1] == n[1] else int(n[0])
            # const_list = [constant]*(target_max-target_min+1)
            # other_list = list(range(target_min, target_max+1, 1))
            # if p[1] == n[1]:
            #     convex_hull.extend(list(zip(other_list, const_list)))
            # else:
            #     convex_hull.extend(list(zip(const_list, other_list)))


    convex_hull = np.array(convex_hull)
    max_area = 0
    def compute_area(max_area, idx):
        i,j = map(int,ij_indices[idx])
        p1, p2 = points[i], points[j]
        other_corners = [[points[i][0], points[j][1]], [points[j][0], points[i][1]]]
        in_convex_hull = all(list(map(is_part_of_convex_hull, other_corners)))

        if in_convex_hull:
            x_width = max(points[i][0], points[j][0]) - min(points[i][0], points[j][0]) +1
            y_width = max(points[i][1], points[j][1]) - min(points[i][1], points[j][1]) +1

            if x_width * y_width == 50:
                tmp = 1
            max_area = max(x_width * y_width, max_area)

        return max_area
    # for idx in range(len(distance_matrix)):
    max_area = reduce(compute_area, range(len(distance_matrix)), max_area)

    return int(max_area)

if __name__ == "__main__":
    script_dir = osp.dirname(osp.abspath(__file__))
    input_path = osp.join(script_dir,'input', "input.txt")

    with open(input_path, "r") as f:
        lines = f.read().splitlines()

    print(solve(lines))