'''
@Author : Priyanka
@Date : 2022-05-04  5:25:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 5:35:00
@Title : Write a Python program to find the number of elements of an array, length of one
array element in bytes and total bytes consumed by the elements.
'''

import numpy as np


def find_size():
    """
      Description:
           program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.array([1, 2, 3], dtype=np.float64)
    print("Size of the array: ", x.size)
    print("Length of one array element in bytes: ", x.itemsize)
    print("Total bytes consumed by the elements of the array: ", x.nbytes)


if __name__ == '__main__':
    find_size()
