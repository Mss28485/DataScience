#  Copyright (c) 2025.

import numpy as np
class LinearAlgZeroVector:
    def __init__(self,zero_vector_one,zero_vector_two):
        self.zero_vector_one = np.zeros(zero_vector_one)
        self.zero_vector_two = np.zeros(zero_vector_two)
def main():
    zero_vector()
def zero_vector():
    _zero_vector = LinearAlgZeroVector(3,3)
    print(f'Zero Array One : {_zero_vector.zero_vector_one}')
    print(f'Zero Array Two : {_zero_vector.zero_vector_two}')
    _zero_vector_combination = np.stack((_zero_vector.zero_vector_one,_zero_vector.zero_vector_two),axis=0)
    print(f'Zero Array One : {_zero_vector_combination}')
if __name__ == '__main__':
    main()