import numpy as np

from py_hello_world_keatincf.operations import sum

def test_sum_provides_2x2_ones_matrix():
    assert np.array_equal(sum.sum(), np.ones(shape=[2,2]))