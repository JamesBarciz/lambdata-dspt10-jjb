import pandas as pd


def null_count(df: pd.DataFrame) -> int:
    """
    Helper function which will display the number of null_values
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :param df: pd.DataFrame - DataFrame object with which will be used to
                              count null values
    :return: null_sum: int - the number of null values in the entire DataFrame
    """

    null_sum = 0
    columns = df.isna().sum()
    for i in columns:
        null_sum += columns[i]

    return null_sum


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
