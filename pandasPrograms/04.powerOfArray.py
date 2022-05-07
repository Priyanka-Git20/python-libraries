'''
@Author : Priyanka
@Date : 2022-05-05  2:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 2:40:00
@Title :Write a Python program to get the powers of an array values element-wise.
'''

import pandas as pd


def power_of_element():
    """
      Description:
           By using the pow() method finding the power.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    arr = pd.Series([0,1,2,3,4,5,6])
    print("The power of array is :",arr.pow(3))


if __name__ == '__main__':
    power_of_element()
