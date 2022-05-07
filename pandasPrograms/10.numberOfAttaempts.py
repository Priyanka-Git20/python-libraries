'''
@Author : Priyanka
@Date : 2022-05-05  1:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 1:20:00
@Title : Write a Python program to select the rows where the number of attempts in the
examination is greater than 2.
'''

import pandas as pd
import numpy as np


def number_of_attempts():
    """
      Description:
           select the rows where the number of attempts in the examination is greater than 2.
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

    dataframe = pd.DataFrame(exam_data,index=labels)
    print("Data frame where attempts greater than 2 is :")
    # print(dataframe[dataframe["attempts"] > 2])
    print(dataframe.loc[(dataframe["attempts"] > 2)])


if __name__ == '__main__':
    number_of_attempts()