#  Copyright (c) 2025.
"""
      ||X|| = Sqr
                    2
           2   E  x    i
               i
"""
import numpy as np

class LinearAlgNorms:
    def __init__(self,_norm,_l1_norm,_l2_norm,_l2sqr_norm):
        self._norm = np.array(_norm)
        self._l1_norm = _l1_norm
        self._l2_norm = _l2_norm
        self._l2sqr_norm = _l2sqr_norm
    def norm_array(self):
        print(f'Norm Vector = {self._norm}')
    def norm_max(self):
        print(f'Norm  Max Vector = {np.max([np.abs(self._l1_norm[0]),np.abs(self._l1_norm[1]),np.abs(self._l1_norm[2])])}')
    def norm_l1(self):
        print(f'Norm L1 Vector = {np.abs(self._l1_norm[0]+self._l1_norm[1]+self._l1_norm[2])}')
    def norm_l2(self):
        print(f'Norm L2 Vector = = {np.linalg.norm(self._l2_norm)}')
    def norm_l2_sqr(self):
        print(f'Norm L2 SQR Vector = = {np.dot(self._l2sqr_norm,self._l2sqr_norm)}')

def main():
    norms_input = LinearAlgNorms([25,2,5],[25,2,5],[25,2,5,2],[25,2,5,9])
    norms_input.norm_array()
    norms_input.norm_l1()
    norms_input.norm_max()
    norms_input.norm_l2()
    norms_input.norm_l2_sqr()
if __name__ == '__main__':
    main()