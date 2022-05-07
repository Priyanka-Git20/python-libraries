'''
@Author : Priyanka
@Date : 2022-05-04  7:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 8:00:00
@Title : Write a Python program to create a 3-D array with ones on a diagonal and zeros
elsewhere.
'''

import numpy as np


def create_3D_array():
    """
      Description:
           create a 3x3 matrix by using eye()The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    # 3x3 matrix with 1 on main diagonal.
    x = np.eye(3)
    print(x)


if __name__ == '__main__':
    create_3D_array()
