import numpy as np
class LinearAlgebraTensorTransposition:
    tensor_trans=np.array([[25,2],[5,26],[3,7]])
    def __init__(self,tensor_trans):
        tensorTrans = self.tensor_trans
def tensor_transposition():
    return LinearAlgebraTensorTransposition.tensor_trans
def main():
    _tensor_transposition = tensor_transposition()
    print(f'Reverse Matrices: {_tensor_transposition.T}')
    print(f'Shape Matrices: {_tensor_transposition.shape}')
    print(f'Multiply Matrices: {_tensor_transposition*2}')
    print(f'Add Matrices: {_tensor_transposition+2}')
    print(f'Add Matrices: {_tensor_transposition*2+2}')
    print(f'Power Matrices: {_tensor_transposition**2}')
if __name__ == "__main__":
    main()
