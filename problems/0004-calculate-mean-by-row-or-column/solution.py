def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    import numpy as np
    arr = np.array(matrix)
    return arr.mean(axis = 1*(mode == 'row'))
