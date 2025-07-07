#the task has screenshot task_1_19.png or something related

import numpy as np

def minkowski_distance(p, x, y):
    assert isinstance(x, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert x.size == y.size, "Arrays must be of the same shape"
    assert p > 0 and isinstance(p, int), "p must be a positive integer"

    return np.sum(np.abs(x - y) ** p) ** (1/p)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(minkowski_distance(3, x, y))