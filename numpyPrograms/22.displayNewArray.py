'''
@Author : Priyanka
@Date : 2022-05-04  8:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 9:00:00
@Title :Write a Python program to create an array of (3, 4) shape, multiply every element
value by 3 and display the new array.
'''

import numpy as np


def display_new_array():
    """
      Description:
           . create an array of (3, 4) shape, multiply every element value by 3 and display the new array.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.arange(12).reshape(3, 4)
    print("Original array elements:")
    print(x)
    for a in np.nditer(x, op_flags=['readwrite']):
          a[...] = 3 * a
    print("New array elements:")
    print(x)


if __name__ == '__main__':
    display_new_array()
