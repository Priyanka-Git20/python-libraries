'''
@Author : Priyanka
@Date : 2022-05-04  9:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 9:25:00
@Title :Write a Python program to convert a NumPy array into Python list structure.
'''

import numpy as np


def convert_array_into_list():
    """
      Description:
           By using the tolist() method convert the numpy array into list.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.arange(6).reshape(3, 2)
    print("Original array elements:\n",x)
    print("Array to list:")
    print(x.tolist())


if __name__ == '__main__':
    convert_array_into_list()