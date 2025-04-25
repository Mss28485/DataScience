#  Copyright (c) 2025.
import numpy as np
import torch as tor
class LinearAlgDotProduct:
    dot_product_vector1 = np.array([25,2,5])
    dot_product_vector2 = np.array([0,1,2])
    dot_product_vector1_torch = tor.tensor([25,2,5])
    dot_product_vector2_torch = tor.tensor([0,1,2])
    def __init__(self):
        pass
def dot_product_numpy_results():
    return LinearAlgDotProduct.dot_product_vector1
def dot_product_torch_results():
    return LinearAlgDotProduct.dot_product_vector1_torch
def main():
    _dot_product = dot_product_numpy_results()
    print(f'Dot Product NumPyy...............')
    print(f'Dot Product Vector1:{_dot_product}')
    _dot_product2=LinearAlgDotProduct.dot_product_vector2
    print(f'Dot Product Vector1:{_dot_product2}')
    print(f'Dot Product Vector Total:{np.dot(_dot_product,_dot_product2)}')

    _dot_product_torch = dot_product_torch_results()
    print(f'Dot Product torch...............')
    print(f'Dot Product Vector1:{_dot_product_torch}')
    _dot_product2_torch=LinearAlgDotProduct.dot_product_vector2_torch
    print(f'Dot Product Vector1:{_dot_product2_torch}')
    print(f'Dot Product Total Torch:{tor.dot(_dot_product_torch,_dot_product2_torch)}')


if __name__ == "__main__":
    main()