'''
@Author : Priyanka
@Date : 2022-05-04  2:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 3:10:00
@Title :Create a 3x3 matrix with values ranging from 2 to 10.
'''

import numpy as np


def create_matrix():
    """
      Description:
          Creating the 3*3 matrix by using reshape function.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """

    x = np.arange(2, 11).reshape(3, 3)
    print("3 * 3 Matrix with values ranging from 2 to 10 is: \n",x)


if __name__ == '__main__':
    create_matrix()