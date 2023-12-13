import numpy as np

def sum() -> np.ndarray:
    """
    Calculates the sum of two 2x2 matrices with one matrix being a ones diagnol matrix
    and the other a ones anti-diagonal matrix.

    Returns:
        np.ndarray: 2x2 matrix of all ones
    """
    a = np.ndarray(shape=(2,2), buffer=np.array([[1,0],[0,1]]), dtype=int)
    b = np.ndarray(shape=(2,2), buffer=np.array([[0,1],[1,0]]), dtype=int)

    return a + b