'''
@Author : Priyanka
@Date : 2022-05-04  6:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 6:50:00
@Title :Write a Python program compare two arrays using numpy
'''

import numpy as np


def compare_two_arrays():
    """
      Description:
          comparing two arrays.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """

    a = np.array([1, 2])
    b = np.array([4, 5])
    print("Array a = ", a)
    print("Array b = ", b)
    print("a > b",np.greater(a, b))
    print("a >= b",np.greater_equal(a, b))
    print("a < b",np.less(a, b))
    print("a <= b",np.less_equal(a, b))


if __name__ == '__main__':
      compare_two_arrays()

