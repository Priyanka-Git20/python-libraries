'''
@Author : Priyanka
@Date : 2022-05-05  12:20:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 12:40:00
@Title : Write a Python program to select the 'name' and 'score' columns from the following DataFrame.
'''

import pandas as pd
import numpy as np


def display_selected_column():
    """
      Description:
           select the 'name' and 'score' columns from the DataFrame.
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
    dataframe = pd.DataFrame(exam_data,labels)
    print(dataframe[["name","score"]])


if __name__ == '__main__':
    display_selected_column()