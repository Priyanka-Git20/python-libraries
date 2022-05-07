'''
@Author : Priyanka
@Date : 2022-05-05  6:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 7:20:00
@Title : Write a Python program to iterate over rows in a DataFrame.
'''

import pandas as pd
import numpy as np


def iterate_rows():
    """
      Description:
           iterate over rows in a DataFrame using for loop.
      Parameter:
           none
      Return:
          Returning nothing.
    """
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
                          'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    dataframe = pd.DataFrame(exam_data, index=labels)
    print("Original dataFrame: \n",dataframe)
    for i, j in dataframe.iterrows():
        print(i, j)
        print()


if __name__ == '__main__':
    iterate_rows()
