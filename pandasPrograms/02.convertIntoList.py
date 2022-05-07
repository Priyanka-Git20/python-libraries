'''
@Author : Priyanka
@Date : 2022-05-05  11:15:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 11:26:00
@Title :Write a Python program to convert a Panda module Series to Python list and it's type.
'''

import pandas as pd


def convert_into_list():
    """
      Description:
           . By using the tolist() method converting the Series into the list and printing the type.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    arr1 = pd.Series([12, 5, 7, 8, 9, 10])
    print("Pandas series and type :\n",arr1)
    print("Covert the python series into the list \n",arr1.tolist())
    print(type(arr1.tolist()))


if __name__ == '__main__':
    convert_into_list()