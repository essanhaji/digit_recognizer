__author__ = 'Sanhoj'

import numpy as np

def compute_correlation_similarity_score(x, y):
    """
        sorensen Similarity J (A,B) = | Intersection (A,B) | / | Union (A,B) |
    """
    return np.corrcoef(x, y)[0][1]


if __name__ == "__main__":

    score = compute_correlation_similarity_score(np.array([0, 1, 2, 5, 6]), np.array([0, 2, 3, 5, 7]))
    print("correlation Similarity Score : %s" %score)
    pass