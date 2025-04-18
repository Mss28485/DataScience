#  Copyright (c) 2025.

import numpy as np
import torch as tor
class LinearAlgHadamardPoint:
    hadamard_array = np.array([[25, 2], [5, 26], [3, 7]])
    hadamard_array_torch = tor.tensor([[25, 2], [5, 26], [3, 7]])
    def __init__(self, _hadamard_array):
        _hadamard_array = self.hadamard_array
def main():
    _hadamard_product = hadamard_product_addition()
    print(f'From NumPay--------------------------------------------')
    print(f'Hadamard Array: {_hadamard_product}')
    print(f'Hadamard Array Plus Two: {_hadamard_product+2}')
    _xarray_plus = _hadamard_product+2
    print(f'Hadamard Array plus Two: {_hadamard_product+_xarray_plus}')
    print(f'Hadamard Multiple 2: {_hadamard_product*_xarray_plus}')
    _hadamard_product_torch = hadamard_product_torch()
    print(f'From torch----------------------------------------------')
    print(f'Hadamard Array: {_hadamard_product_torch}')
    print(f'Hadamard Array Plus Two: {_hadamard_product_torch+2}')
    _xarray_plus = _hadamard_product_torch+2
    print(f'Hadamard Array plus Two: {_hadamard_product_torch+_hadamard_product_torch}')
    print(f'Hadamard Multiple 2: {_hadamard_product_torch*_hadamard_product_torch}')

def hadamard_product_addition():
    _xarray = LinearAlgHadamardPoint.hadamard_array
    return _xarray
def hadamard_product_torch():
    _xarray_torch = LinearAlgHadamardPoint.hadamard_array_torch
    return _xarray_torch

if __name__ == "__main__":
    main()