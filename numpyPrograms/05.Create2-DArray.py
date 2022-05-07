'''
@Author : Priyanka
@Date : 2022-05-04  4:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 4:20:00
@Title :Write a Python program to create a 2d array with 1 on the border and 0 inside.
'''

import numpy as np


def create_2dimensionl_array():
    """
      Description:
           create a 2d array with 1 on the border and 0 inside.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """

    x = np.ones((5, 5))
    print("Original array:")
    print(x)
    print("1 on the border and 0 inside in the array")
    x[1:4, 1:4] = 0
    print(x)


if __name__ == '__main__':
    create_2dimensionl_array()