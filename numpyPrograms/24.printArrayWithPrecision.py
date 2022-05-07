'''
@Author : Priyanka
@Date : 2022-05-04  9:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 9:50:00
@Title :Write a Python program to convert a NumPy array into Python list structure
'''

import numpy as np


def print_array_with_precision():
    """
      Description:
           Printing the array with precision.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """

    x = np.array([0.26153123, 0.52760141, 0.5718299, 0.5927067, 0.7831874, 0.69746349,
                  0.35399976, 0.99469633, 0.0694458, 0.54711478])
    print("Original array elements:\n",x)
    print("Print array values with precision 3:")
    np.set_printoptions(precision=3)
    print(x)


if __name__ == '__main__':
    print_array_with_precision()