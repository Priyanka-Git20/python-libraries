'''
@Author : Priyanka
@Date : 2022-05-04  5:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 6:00:00
@Title :Write a Python program to find the set difference of two arrays. The set difference
will return the sorted, unique values in array1 that are not in array2
'''

import numpy as np


def find_set_difference():
    """
      Description:
          By using the setdiff method finding the common values between two arrays.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    array1 = np.array([0, 10, 20, 40, 60, 80])
    print("Array1: ", array1)
    array2 = [10, 30, 40, 50, 70]
    print("Array2: ", array2)
    print("Unique values in array1 that are not in array2:")
    print(np.setdiff1d(array1, array2))


if __name__ == '__main__':
    find_set_difference()