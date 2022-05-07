'''
@Author : Priyanka
@Date : 2022-05-05  3:50:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 4:00:00
@Title :Write a Python program to sort the DataFrame first by 'name' in descending order,
then by 'score' in ascending order
'''

import pandas as pd
import numpy as np


def sort_data():
    """
      Description:
           Python program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order
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
    dataframe.sort_values(by=["name","score"],ascending=[False,True])
    print("Printing name by descending order and score by ascending order \n",dataframe)


if __name__ == '__main__':
    sort_data()
