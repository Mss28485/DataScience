#  Copyright (c) 2025.
import numpy as np

class LinearAlgOrthogonalVector:
    def __init__(self,orthogonal_vector_x,orthogonal_vector_y):
        self.orthogonal_vector_x = np.array(orthogonal_vector_x)
        self.orthogonal_vector_y = np.array(orthogonal_vector_y)
    def orthogonal_vector(self):
        # Formula : V = i,j ==> i+j & U = i + J ==> [vi1*ui1] + [vi2*ui2] or 90 degree.
        print(f'Values of x and y :: {self.orthogonal_vector_x,self.orthogonal_vector_y}')
        print(f'Value of dot product :: {np.dot(self.orthogonal_vector_x,self.orthogonal_vector_y)}')
def main():
    orthogonal_vect = LinearAlgOrthogonalVector([-3,4],[4,3])
    orthogonal_vect.orthogonal_vector()
if __name__ == '__main__':
    main()