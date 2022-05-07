'''
@Author : Priyanka
@Date : 2022-05-05  3:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 3:40:00
@Title : Write a Python program to append a new row 'k' to data frame with given values for
each column. Now delete the new row and return the original DataFrame.
'''

import pandas as pd
import numpy as np


def append_data():
    """
      Description:
          append a new row 'k' to data frame with given values for each column and delete it by using drop()
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
    dataframe.loc['k'] = [ "Suresh",15.5,1,"yes"]
    print("After append the data:\n",dataframe)
    print("After deleting :\n",dataframe.drop('k'))


if __name__ == '__main__':
    append_data()