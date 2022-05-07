'''
@Author : Priyanka
@Date : 2022-05-05  1:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 1:50:00
@Title : Write a Python program to count the number of rows and columns of a DataFrame
'''

import pandas as pd
import numpy as np


def count_rows_column():
    """
      Description:
          count the number of rows and columns of a DataFrame.
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
    print(dataframe)
    # row_count = len(dataframe)
    row_count = dataframe.shape[0]
    print("Number of rows:",row_count)
    # column_count = len(dataframe.columns)
    column_count = dataframe.shape[1]
    print("Number of columns:",column_count)


if __name__ == '__main__':
    count_rows_column()
