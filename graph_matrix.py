import random

def generate_adj_matrix(n, seed):
    random.seed(seed)
    matrix = [[random.uniform(0, 2) for _ in range(n)] for _ in range(n)]
    n3 = 0
    n4 = 8
    k = 1.0 - n3 * 0.02 - n4 * 0.005 - 0.25
    for i in range(n):
        for j in range(n):
            matrix[i][j] *= k
            matrix[i][j] = 1 if matrix[i][j] >= 1.0 else 0
    return matrix

def make_undirected(dir_matrix):
    n = len(dir_matrix)
    undir = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dir_matrix[i][j] == 1:
                undir[i][j] = 1
                undir[j][i] = 1
    return undir