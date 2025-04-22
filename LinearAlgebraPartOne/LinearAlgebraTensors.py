#  Copyright (c) 2025.
#  Scaler    0
#  Vector    1
#  Matrix    2
#  Tensor   3 or n
import numpy as np
class LinearAlgTensor:
    def __init__(self, scalar_value, vector_value, matrix_value, tensor3d_value):
        self.scalar = scalar_value
        self.vector = np.array(vector_value)
        self.matrix = np.array(matrix_value)
        self.tensor3d = np.array(tensor3d_value)
def main():
       _tensor_types= tensors()
def tensors():
    _scalar = LinearAlgTensor(25,([2,25,28]),([2,25,28],[3,26,29]),([2,25,28],[3,26,29],[4,27,30]))
    print(f'Scalar : {_scalar.scalar} \nVector : {_scalar.vector} \nMatrix : {_scalar.matrix} \nTensor3D : {_scalar.tensor3d}')
    return _scalar.scalar,_scalar.vector,_scalar.matrix,_scalar.tensor3d
if __name__ == '__main__':
    main()