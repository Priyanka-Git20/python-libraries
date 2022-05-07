'''
@Author : Priyanka
@Date : 2022-05-04  5:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 5:20:00
@Title : Write a Python program to find the real and imaginary parts of an array of complex number.
'''

import numpy as np


def find_real_and_imaginary_part():
    """
      Description:
           finding the real and imaginary part of the array.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.sqrt([1.00000000+0.j])
    y = np.sqrt([0.70710678+0.70710678j])
    print("The original array x:",x)
    print("The original array y:",y)
    print("Real part of the array:")
    print(x.real)
    print(y.real)
    print("Imaginary part of the array:")
    print(x.imag)
    print(y.imag)


if __name__ == '__main__':
    find_real_and_imaginary_part()
