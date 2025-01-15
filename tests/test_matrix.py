"""
Tests pour le module matrix.py
"""

import pytest
import numpy as np
from src.module.matrix import mult_mat


def test_mult_mat_valid():
    # Test avec des listes de listes
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    result = mult_mat(mat1, mat2)
    expected = np.array([[19, 22], [43, 50]])
    assert np.array_equal(result, expected)


def test_mult_mat_numpy_arrays():
    # Test avec des numpy arrays
    mat1 = np.array([[1, 0], [0, 1]])
    mat2 = np.array([[4, 1], [2, 3]])
    result = mult_mat(mat1, mat2)
    expected = np.array([[4, 1], [2, 3]])
    assert np.array_equal(result, expected)


def test_mult_mat_invalid_dimensions():
    # Test avec des dimensions incompatibles
    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[1, 2], [3, 4]]
    with pytest.raises(ValueError):
        mult_mat(mat1, mat2)


def test_mult_mat_invalid_input():
    # Test avec des entrées invalides
    mat1 = "not a matrix"
    mat2 = [[1, 2], [3, 4]]
    with pytest.raises(TypeError):
        mult_mat(mat1, mat2)  # type: ignore
