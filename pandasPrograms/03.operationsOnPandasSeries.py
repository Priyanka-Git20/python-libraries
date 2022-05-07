'''
@Author : Priyanka
@Date : 2022-05-05  11:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 11:40:00
@Title :Write a Python program to add, subtract, multiple and divide two Pandas Series.
'''

import pandas as pd


def operations_on_series():
    """
      Description:
           . By using the operators do the addition ,subtraction ,multiplication and division.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    arr1 = pd.Series([2, 4, 6, 8, 10,12])
    arr2 = pd.Series([5, 3, 15, 7, 9,21])
    arr = arr1 + arr2
    print("Add two Series:\n",arr)
    arr = arr1 - arr2
    print("Subtract two Series:\n",arr)
    arr = arr1 * arr2
    print("Multiply two Series:\n",arr)
    arr = arr1 / arr2
    print("Divide Series1 by Series2:\n",arr)


if __name__ == '__main__':
    operations_on_series()
