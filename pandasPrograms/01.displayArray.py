'''
@Author : Priyanka
@Date : 2022-05-05  11:05:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 11:15:00
@Title :Write a Python program to create and display a one-dimensional array-like object
containing an array of data using Pandas module.
'''

import pandas as pd


def display_array():
    """
      Description:
           . By using the series convert the one dimensional array in the table format one column display index number and another column element.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """

    arr1 = pd.Series([12,5,7,8,9,10])
    print("One dimensional array in table format:\n",arr1)


if __name__ == '__main__':
    display_array()


