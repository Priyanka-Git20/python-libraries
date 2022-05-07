'''
@Author : Priyanka
@Date : 2022-05-04  8:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 8:15:00
@Title : Write a Python program to create an array which looks like below array.
'''

import numpy as np


def create_array():
    """
      Description:
           create array.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.tri(4, 3, -1)
    print(x)


if __name__ == '__main__':
    create_array()