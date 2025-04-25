#  Copyright (c) 2025. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
import numpy as tor
class LinearAlgVectorTransposition:
    def __init__(self,vector):
        self.vector = tor.array(vector)
def main():
    vector_transposition()
def vector_transposition():
    _vector_transposition_1d =  LinearAlgVectorTransposition(([2,3,6]))
    print(f'No transposing regular 1-D Array thus ==> {_vector_transposition_1d.vector.T}')
    _vector_transposition_2d = LinearAlgVectorTransposition(([[12,23,36]]))
    print(f'Transposing with 2-D thus ==> {_vector_transposition_2d.vector.T}')
if __name__ == '__main__':
    main()

