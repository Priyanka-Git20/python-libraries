'''
@Author : Priyanka
@Date : 2022-05-04  3:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 3:50:00
@Title :Write a Python program to create a null vector of size 10 and update sixth value to 11.
'''

import numpy as np


def create_null_vector():
    """
      Description:
           By using zeros () creating a null vector and then update the value by using index.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """

    x = np.zeros(10)
    print("The null vector is \n",x)
    print("Update sixth value to 11")
    x[6] = 11
    print(x)


if __name__ == '__main__':
    create_null_vector()


