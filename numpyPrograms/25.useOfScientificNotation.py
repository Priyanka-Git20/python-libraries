'''
@Author : Priyanka
@Date : 2022-05-04  9:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 10:00:00
@Title :Write a Python program to suppresses the use of scientific notation for small
numbers in numpy array.
'''

import numpy as np


def suppresses_the_use_of_scientific_notation():
    """
      Description:
           program to suppresses the use of scientific notation for small numbers in numpy array.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.array([1.60000000e-10,1.60000000e+00,1.20000000e+03,2.35000000e-01])
    print("Original array elements:\n",x)
    print("Print array values with precision 3:")
    np.set_printoptions(suppress=True)
    print(x)


if __name__ == '__main__':
    suppresses_the_use_of_scientific_notation()
