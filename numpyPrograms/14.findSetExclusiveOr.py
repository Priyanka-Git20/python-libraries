'''
@Author : Priyanka
@Date : 2022-05-04  6:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 6:25:00
@Title :Write a Python program to find the set exclusive-or of two arrays. Set exclusive-or
will return the sorted, unique values that are in only one (not both) of the input arrays
'''

import numpy as np


def find_set_exclusive():
    """
      Description:
          By using the setxor method finding thw values that are in only one(not both) of the input arrays.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    array1 = np.array([0, 10, 20, 40, 60, 80])
    print("Array1 is : ", array1)
    array2 = np.array([10, 30, 40, 50, 70])
    print("Array2 is : ", array2)
    print("Unique values that are in only one (not both) of the input arrays : \n",np.setxor1d(array1, array2) )


if __name__ == '__main__':
    find_set_exclusive()