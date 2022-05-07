'''
@Author : Priyanka
@Date : 2022-05-04  4:35:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 4:45:00
@Title :Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern
'''

import numpy as np


def checkerboard_pattern():
    """
      Description:
           Creating 8x8 matrix and fill it with a checkerboard pattern.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.ones((3, 3))
    print("Checkerboard pattern:")
    x = np.zeros((8, 8), dtype=int)
    x[1::2, 0::2] = 1
    x[::2, 1::2] = 1
    print(x)


if __name__ == '__main__':
    checkerboard_pattern()