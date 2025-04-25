#  Copyright (c) 2025.
import numpy as np
import  matplotlib.pyplot as plot
class LinearAlgVectorValue:

    def __init__(self,vector_one,vector_two,vector_three):
        self.vector_one= vector_one
        self.vector_two= vector_two
        self.vector_three= vector_three

def find_vector_value():
    call_vector = LinearAlgVectorValue([1,2],[2,3],[4,5])
    vector_value =  (call_vector.vector_one[0]**2)+(call_vector.vector_one[1]**2)+\
                    (call_vector.vector_two[0]**2)+(call_vector.vector_two[1]**2)+\
                    (call_vector.vector_three[0]**2)+(call_vector.vector_three[1]**2)
    print(f'{vector_value*1/2}')
    print(call_vector.vector_two[0])
    print(call_vector.vector_one,call_vector.vector_two)
    vector_x_point = call_vector.vector_one
    vector_y_point = call_vector.vector_two
    plot.title('Vector Value')
    plot.xlabel('X-Axis')
    plot.ylabel('Y-Axis')
    plot.plot(vector_x_point,vector_y_point,linewidth='2',color='red',marker='h', ms=10,mec='b')
    plot.axvline(x=1, color='black', linestyle='--')
    _ = plot.axhline(y=2, color='black', linestyle='--')
    plot.show()
    return call_vector

def main():
    find_vector_value()
if __name__ == '__main__':
    main()
