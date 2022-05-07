'''
@Author : Priyanka
@Date : 2022-05-04  10:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 10:25:00
@Title :Write a Python program to how to add an extra column to an numpy array
'''

import numpy as np


def add_extra_column_to_numpy_array():
    """
      Description:
          By using append method add column to the original array.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.array([[10, 20, 30], [40, 50, 60]])
    print("The original array is :\n",x)
    y = np.array([[100], [200]])
    print("Array after adding column is :\n",np.append(x, y, axis=1))


if __name__ == '__main__':
    add_extra_column_to_numpy_array()
