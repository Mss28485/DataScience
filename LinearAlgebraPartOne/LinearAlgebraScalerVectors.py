import numpy as np
import torch as tor
class LinearAlgebraOne:
    vector = np.array([[25,2,5]])
    vectorSQ = np.array([25,2,5])
    vectorY = np.array([[25,2,5]])
    orthogonalVectorI = np.array([1,0])
    orthogonalVectorJ = np.array([0,1])
    scalar = tor.tensor(25)
    def __init__(self,vector):
        self.vector = vector
#main function
def main():
#Scalar Value
    value_scalar = scalar()
    print(f'Value of Scalar : {value_scalar}')
    print(f'Size of Scalar : {value_scalar.shape}')

# Vectors
    vectorsList = vectors()
    print(f'Vectors List : {vectorsList}')
    print(f'Size of Vector length : {len(vectorsList)}')
    print(f'Size of Vector Type : {type(vectorsList)}')
    print(f'Size of Vector @ 0 : {vectorsList[0]}')
    print(f'Size of Vector @ 0 Type : {type(vectorsList[0])}')
# Vectors Transportation
    vectorTransprot = vector_transportation()
    print(f'Vector Transport 1-d : {vectorTransprot.T}')
    print(f'Vector Transport shape : {vectorTransprot.shape}')
    print(f'Vector Transport Y : {LinearAlgebraOne.vectorY}')
    print(f'Transposing a regular 1-D array : {LinearAlgebraOne.vectorY.T}')
# Zero Vector
    z_vector = zero_vector()
    print(f'Vector Zero: {z_vector}')

# L2 Norm
    l2Norm = l2norm()
    print(f'L2 Norm: {l2Norm}')
# L1 Norm
    l1Norm = l1norm()
    print(f'L1 Norm: {l1Norm}')
# L2 Norm Square
    l2NormSquare = l2square()
    print(f'L2 Norm Square: {l2NormSquare}')
# Max Norm
    _maxNorm = max_norm()
    print(f'Max Norm: {_maxNorm}')
# Orthogonal Vector
    _orthogonalVector = orthogonal_vector()
    print(f'Orthogonal Vector: {_orthogonalVector}')
# scalar is constant numeric value (single or complex)
def scalar():
    return LinearAlgebraOne.scalar
# Vector is more like Array in most programming languages
def vectors():
    return LinearAlgebraOne.vector
# Vector Transportation
def vector_transportation():
    return LinearAlgebraOne.vector
# Vector Zero
def zero_vector():
    return np.zeros(3)
#  L2 Norm
def l2norm():
    return np.linalg.norm(LinearAlgebraOne.vector)
#  L1 Norm
def l1norm():
    l1NormInput = LinearAlgebraOne.vector[0]
    return np.abs(l1NormInput[0] + l1NormInput[1] + l1NormInput[2])
#  L1 Norm Square
def l2square():
    return np.dot(LinearAlgebraOne.vectorSQ, LinearAlgebraOne.vectorSQ)
def max_norm():
    maxNormInput=LinearAlgebraOne.vector[0]
    return np.max([np.abs(maxNormInput[0]),np.abs(maxNormInput[1]),np.abs(maxNormInput[2])])
def orthogonal_vector():
    return np.dot(LinearAlgebraOne.orthogonalVectorI, LinearAlgebraOne.orthogonalVectorJ)
if __name__=="__main__":
    main()
