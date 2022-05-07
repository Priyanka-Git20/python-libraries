'''
@Author : Priyanka
@Date : 2022-05-04  8:35:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 8:50:00
@Title :Write a Python program to make an array immutable (read-only).

'''

import numpy as np


def make_immutable_array():
    """
      Description:
           Create an array which does not have a writing access so when we try to change the array it gives a value error.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.ones(10)
    x.flags.writeable = False
    print("Test the array is read-only or not:")
    print("Try to change the value of the first element:")
    x[0] = 0


if __name__ == '__main__':
    make_immutable_array()