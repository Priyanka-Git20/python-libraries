'''
@Author : Priyanka
@Date : 2022-05-04  7:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 7:50:00
@Title : Write a Python program to change the data type of an array
'''

import numpy as np


def change_data_type():
    """
      Description:
           By using the astype() method changing the type of the array.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
    print(x)
    print("Data type of the array x is:", x.dtype)
    # Changing  the data type of the original array from int to float
    y = x.astype(float)
    print("New Type: ", y.dtype)
    print(y)


if __name__ == '__main__':
    change_data_type()
