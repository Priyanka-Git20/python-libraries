'''
@Author : Priyanka
@Date : 2022-05-04  6:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 7:00:00
@Title : Write a Python program to create a contiguous flattened array.
'''

import numpy as np


def create_flattened_array():
    """
      Description:
           By using the reshape(-1) method creating a contiguous flattened array.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.array([[10, 20, 30], [20, 40, 50]])
    print("Original array:\n",x)
    y = x.reshape(-1)
    print("New flattened array:\n",y)


if __name__ == '__main__':
    create_flattened_array()