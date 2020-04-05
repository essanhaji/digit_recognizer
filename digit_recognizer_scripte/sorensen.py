__author__ = 'Sanhoj'

import numpy as np

def compute_sorensen_similarity_score(x, y):
    """
        sorensen Similarity J (A,B) = | Intersection (A,B) | / | Union (A,B) |
    """
    intersection_cardinality = len(set(x).intersection(set(y))) * 2
    sum_cardinality = len(set(x)) + len(set(y))
    return (intersection_cardinality / float(sum_cardinality))


if __name__ == "__main__":

    score = compute_sorensen_similarity_score(np.array([0, 1, 2, 5, 6]), np.array([0, 2, 3, 5, 7, 9]))
    print("Sorensen Similarity Score : %s" %score)
    pass