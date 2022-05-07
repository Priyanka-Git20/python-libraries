'''
@Author : Priyanka
@Date : 2022-05-04  5:35:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 5:50:00
@Title :Write a Python program to find common values between two arrays
'''

import numpy as np


def find_common_values():
    """
      Description:
          By using the intersect method finding the common values between two arrays.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    array1 = np.array([0, 10, 20, 40, 60])
    print("Array1 is:",array1)
    array2 = [10, 30, 40]
    print("Array2 is:", array2)
    print("Common values between two arrays \n:",np.intersect1d(array1, array2))


if __name__ == '__main__':
    find_common_values()
