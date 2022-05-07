'''
@Author : Priyanka
@Date : 2022-05-04  4:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-04 5:00:00
@Title : Write a Python program to convert a list and tuple into arrays
'''

import numpy as np


def convert_into_array():
    """
      Description:
           Converting the list and tuple into arrays.
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    lst = [1,2,3,4,5]
    print("Original list is \n",lst)
    print("List to array\n",np.array(lst))
    mytuple = ([1, 2, 3, 4, 5],[5,6,7,8,1])
    print("Original tuple is \n",mytuple )
    print("Tuple to array\n", np.array(mytuple))


if __name__ == '__main__':
    convert_into_array()
