import numpy as np
import torch as tor

class LinearAlgebraMatrices:
    matrices=np.array([[25,2],[5,26],[3,7]])
    matrices_torch=tor.tensor([[25,2],[5,26],[3,7]])

    def __init__(self,matrices):
        self.matrices=matrices
def main():
    # Numpy import
    _matrices_array = matrices_array()
    print(f'Matrices Array : {_matrices_array}')
    print(f'Matrices Shape : {_matrices_array.shape}')
    print(f'Matrices Size : {_matrices_array.size}')
    print(f'Matrices left colum : {_matrices_array[:,0]}')
    print(f'Matrices right colum : {_matrices_array[:,-1]}')
    print(f'Matrices Middle row : {_matrices_array[1,:]}')
    print(f'Matrices Index by 2 and 2 : {_matrices_array[0:2,0:2]}')
    print(f'---------Torch------------------')
    # Torch import
    _matrices_torch = matrices_torch()
    print(f'Matrices Torch Array: {_matrices_torch}')
    print(f'Matrices Torch Shape: {_matrices_torch.shape}')
    print(f'Matrices Torch zero-indexed: {_matrices_torch[1,:]}')
    print(f'Matrices Torch zero-indexed: {_matrices_torch}')
def matrices_array():
    return LinearAlgebraMatrices.matrices
def matrices_torch():
    return LinearAlgebraMatrices.matrices_torch
if __name__ == "__main__":
    main()