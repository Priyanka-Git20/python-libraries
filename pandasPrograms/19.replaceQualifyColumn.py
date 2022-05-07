'''
@Author : Priyanka
@Date : 2022-05-05  4:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-05 4:30:00
@Title : Write a Python program to replace the 'qualify' column contains the values 'yes' and
'no' with True and False
'''

import pandas as pd
import numpy as np


def replace_column():
    """
      Description:
          replace the 'qualify' column contains the values 'yes' and 'no' with True and False
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
    dataframe = dataframe.replace({'qualify': {'yes': True,'no': False}})
    print("After changing the qualify column :\n",dataframe)


if __name__ == '__main__':
    replace_column()

