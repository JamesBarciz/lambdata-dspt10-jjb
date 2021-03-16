import pandas as pd
import numpy as np


# class HelperFunction:
#     """
#     This is a helper function class
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     :param df: pd.DataFrame - DataFrame object
#     """
#
    # def __init__(self, df):
    #     self.df = df
    #
    # def null_count(self) -> int:
    #     """
    #     Helper function which will display the number of null_values
    #     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #     :param df: pd.DataFrame - DataFrame object with which will be used to
    #                               count null values
    #     :return: null_sum: int - the number of null values in the entire DataFrame
    #     """
    #     nulls = self.df.isna().sum().sum()
    #     return nulls
    #
    # def train_test_split(self, train_size) -> (pd.DataFrame, pd.DataFrame):
    #     """
    #     Helper function which will return shuffled train and test subsets
    #     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #     :param df: pd.DataFrame - DataFrame object with which to split
    #     :param train_size: float - percentage of data to set aside for train
    #     :return: (train, test): pd.DataFrame - DataFrame subsets after split
    #     """
    #     temp_df = self.df.copy()
    #     training = temp_df.sample(frac=train_size, random_state=42)
    #     testing = temp_df.drop(training.index).sample(frac=1, random_state=42)
    #     return training, testing
    #

def null_count(df: pd.DataFrame) -> int:
    """
    Helper function which will display the number of null_values
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :param df: pd.DataFrame - DataFrame object with which will be used to
                              count null values
    :return: null_sum: int - the number of null values in the entire DataFrame
    """

    columns = df.isna().sum()
    return sum(columns.values)


def train_test_split(df: pd.DataFrame, train_size: float) -> (pd.DataFrame, pd.DataFrame):
    """
    Helper function which will return shuffled train and test subsets
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :param df: pd.DataFrame - DataFrame object with which to split
    :param train_size: float - percentage of data to set aside for train
    :return: (train, test): pd.DataFrame - DataFrame subsets after split
    """

    temp_df = df.copy()
    training = temp_df.sample(frac=train_size, random_state=42)
    testing = temp_df.drop(training.index).sample(frac=1, random_state=42)

    return training, testing

#
# if __name__ == '__main__':
#     data = {
#         'a': [1, 3, 2, 4, np.NaN, 6, 5, 7, 10],
#         'b': [1, 3, np.NaN, 4, np.NaN, 6, 5, 7, 10],
#         'c': [1, np.NaN, 2, 4, np.NaN, 6, 5, 7, 10],
#     }
#
#     temp = pd.DataFrame(data)
#
#     h = HelperFunction(temp)
#
#     train, test = h.train_test_split(train_size=0.8)
#
#     print(h.df)
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#     print(f'Number of Null Values in DataFrame: {h.null_count()}')
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#     print('TRAINING DATA')
#     print(train)
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#     print('TESTING DATA')
#     print(test)
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
