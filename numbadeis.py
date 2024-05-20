from numba import jit
from math import ceil, log2
from random import random

@jit(nopython=True)
def cmv_numba(A, thresh=None, epsilon=0.99, delta=0.9):
    p = 1.0
    X = set()
    if thresh is None:
        thresh = ceil((12 / (epsilon**2)) * log2((8 / delta)))

    for a in A:
        X.discard(a)

        if random() < p and len(X) < thresh:
            X.add(a)

        if len(X) >= thresh:
            X = {x for x in X if random() < 0.5}
            p /= 2

    return len(X) / p

# Example usage
A = [1, 2, 3, 4, 1, 2, 3, 4, 5]
result = cmv_numba(A)
print(result)
