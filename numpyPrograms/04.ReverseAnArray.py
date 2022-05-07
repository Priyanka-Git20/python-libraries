'''
@Author : Priyanka
@Date : 2022-05-04  3:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 4:00:00
@Title :Write a Python program to reverse an array
'''

import numpy as np


def reverse_an_array():
    """
      Description:
          Reversing the array by negative indexing.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    arr = np.arange(12,38)
    print("The array is \n",arr)
    reverseArray = arr[::-1]
    print(reverseArray)


if __name__ == '__main__':
    reverse_an_array()