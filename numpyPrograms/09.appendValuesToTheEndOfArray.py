'''
@Author : Priyanka
@Date : 2022-05-04  5:00:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 5:10:00
@Title : Write a Python program to append values to the end of an array.
'''

import numpy as np


def append_values_to_the_end():
    """
      Description:
           By using the append method add elements at the end of the array.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    arr = [10,20,30]
    print("Original array is \n",arr)
    arr = np.append(arr,[40,50,60,70,80,90])
    print("After appending the values at the end of the array \n",arr)


if __name__ == '__main__':
    append_values_to_the_end()