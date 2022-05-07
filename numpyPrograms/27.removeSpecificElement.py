'''
@Author : Priyanka
@Date : 2022-05-04  10:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 10:50:00
@Title :Write a Python program to remove specific elements in a numpy array.
'''

import numpy as np


def remove_specific_element():
    """
      Description:
          By using delete method remove specific elements in a numpy array.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print("Original array:\n",arr)
    print("Delete first, fourth and fifth elements:")
    new_arr = np.delete(arr, [0,3,4])
    print(new_arr)


if __name__ == '__main__':
    remove_specific_element()