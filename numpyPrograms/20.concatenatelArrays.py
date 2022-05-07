'''
@Author : Priyanka
@Date : 2022-05-04  8:20:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 8:30:00
@Title :Write a Python program to concatenate two 2-dimensional arrays.
'''

import numpy as np


def concatenate_array():
    """
      Description:
           Concatenate two arrays.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    a = np.array([[0, 1, 3], [5, 7, 9]])
    print("Array a is:\n",a)
    b = np.array([[0, 2, 4], [6, 8, 10]])
    print("Array b is:\n",b)
    c = np.concatenate((a,b), 1)
    print("Array after concatenating is:\n",c)


if __name__ == '__main__':
    concatenate_array()