__author__ = 'renienj'

import numpy as np

def compute_jaccard_similarity_score(x, y):
    """
        Jaccard Similarity J (A,B) = | Intersection (A,B) | / | Union (A,B) |
    """
    intersection_cardinality = len(set(x).intersection(set(y)))
    union_cardinality = len(set(x).union(set(y)))
    return intersection_cardinality / float(union_cardinality)


if __name__ == "__main__":

    score = compute_jaccard_similarity_score(np.array([0, 1, 2, 5, 6]), np.array([0, 2, 3, 5, 7, 9]))
    print("Jaccard Similarity Score : %s" %score)
    pass