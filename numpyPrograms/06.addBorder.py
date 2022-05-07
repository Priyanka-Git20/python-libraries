'''
@Author : Priyanka
@Date : 2022-05-04  4:25:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 4:35:00
@Title : Write a Python program to add a border (filled with 0's) around an existing array.
'''

import numpy as np


def add_border():
    """
      Description:
           add a border around an existing array.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.ones((3, 3))
    print("Original array:")
    print(x)
    print("0 on the border and 1 inside in the array")
    x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
    print(x)


if __name__ == '__main__':
    add_border()



    
