'''
@Author : Priyanka
@Date : 2022-05-05  12:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 12:20:00
@Title : Write a Python program to get the first 3 rows of a given DataFrame.
'''

import pandas as pd
import numpy as np


def display_first3_rows():
    """
      Description:
           get the first 3 rows of a given DataFrame
      Parameter:
           none
      Return:
          Returning nothing but print the result.
    """
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
                          'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    data = pd.DataFrame(exam_data,labels)
    # print(data.head(3))
    print(data.loc[["a","b","c"], :])


if __name__ == '__main__':
    display_first3_rows()