import pandas as pd


def remove_duplicates(df):
    return df.drop_duplicates()


def validate_positive(df, column):
    return df[df[column] > 0]


def report_missing(df):
    return df.isnull().sum()


def report_duplicates(df):
    return df.duplicated().sum()