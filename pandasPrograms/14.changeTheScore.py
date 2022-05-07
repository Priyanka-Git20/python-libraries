'''
@Author : Priyanka
@Date : 2022-05-05  2:35:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 2:50:00
@Title : Write a Python program to change the score in row 'd' to 11.5.
'''

import pandas as pd
import numpy as np


def select_rows():
    """
      Description:
           change the score in row 'd'
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
    print("Original data \n",dataframe)
    dataframe.loc["d","score"] = 11.5
    print("After changing the score:\n",dataframe)


if __name__ == '__main__':
    select_rows()