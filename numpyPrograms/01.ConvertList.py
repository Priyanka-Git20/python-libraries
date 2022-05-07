'''
@Author : Priyanka
@Date : 2022-05-04  2:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-020 2:50:00
@Title : Write a Python program to convert a list of numeric value into a one-dimensional
NumPy array.
'''

import numpy as np


def convert_list():
    """
      Description:
          Converting the list into the one-dimensional array by importing the numPy library.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """

    lst = [12.23, 13.32, 100, 36.32]
    print("Original List:",lst)
    oneDimensionalNumpyarray = np.array(lst)
    print("One-dimensional NumPy array: ",oneDimensionalNumpyarray)


if __name__ == '__main__':
    convert_list()

