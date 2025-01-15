"""
Ce module fournit des fonctions pour les opérations matricielles.
"""

import numpy as np
from collections.abc import Sequence

print(Sequence[Sequence[float | int]])


def mult_mat(
    mat1: Sequence[Sequence[float | int]] | np.ndarray,
    mat2: Sequence[Sequence[float | int]] | np.ndarray,
) -> np.ndarray:
    """
    Multiplie deux matrices en utilisant numpy.

    Args:
        mat1: Première matrice (liste de listes ou numpy array)
        mat2: Deuxième matrice (liste de listes ou numpy array)

    Returns:
        np.ndarray: Résultat de la multiplication matricielle

    Raises:
        ValueError: Si les dimensions des matrices ne sont pas compatibles
        TypeError: Si les entrées ne sont pas des matrices valides
    """
    try:
        # Conversion en numpy arrays si nécessaire
        mat1_arr = np.array(mat1, dtype=float)
        mat2_arr = np.array(mat2, dtype=float)
    except (ValueError, TypeError) as e:
        raise TypeError("Les entrées doivent être des matrices valides") from e

    # Vérification des dimensions
    if mat1_arr.shape[1] != mat2_arr.shape[0]:
        raise ValueError(
            "Les dimensions des matrices ne sont pas compatibles pour la multiplication"
        )

    return np.matmul(mat1_arr, mat2_arr)
