'''
@Author : Priyanka
@Date : 2022-05-05  1:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 2:10:00
@Title :  Write a Python program to select the rows where the score is missing, i.e. is NaN.
'''

import pandas as pd
import numpy as np


def score_missing():
    """
      Description:
           Display a rows where the score is missing, i.e. is NaN.
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
    print(dataframe[dataframe["score"].isnull()])


if __name__ == '__main__':
    score_missing()
