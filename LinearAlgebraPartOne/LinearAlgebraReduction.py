#  Copyright (c) 2025.
#   ------- n
#   \         xi
#   /
#   ------- i = 1
import numpy as np
import torch as tor
class LinearAlgReduction:
    reduction_matrices = np.array([[25,2],[5,26],[3,7]])
    reduction_matrices_torch = tor.tensor([[25,2],[5,26],[3,7]])
    def __init__(self):
        pass
def main():
    _reduction_sum = reduction_sum()
    # From NumPy
    print(f'from NumPy-----------------------------------------------')
    print(f'Reduction Matrices: {_reduction_sum}')
    print(f'Reduction Total Matrices: {_reduction_sum.sum()}')
    print(f'Reduction Sum of Axis Matrices: {_reduction_sum.sum(axis=0)}')
    print(f'Reduction Sum of Axis Matrices: {_reduction_sum.sum(axis=1)}')
    # From torch
    _reduction_sum_torch = reduction_sum_torch()
    print(f'from Torch-----------------------------------------------')
    print(f'Reduction Matrices: {_reduction_sum_torch}')
    print(f'Reduction Total Matrices: {_reduction_sum_torch.sum()}')

def reduction_sum():
    return LinearAlgReduction.reduction_matrices
def reduction_sum_torch():
    return LinearAlgReduction.reduction_matrices_torch

if __name__ == "__main__":
    main()