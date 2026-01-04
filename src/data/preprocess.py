import pandas as pd
from src.data.load_data import load_churn_data
from src.config import DROP_COLUMNS, TARGET_COLUMN,CATEGORICAL_COLUMNS, INTEGER_COLUMNS, FLOAT_COLUMNS


def drop_columns(df: pd.DataFrame):
    df = df.copy()
    for column in DROP_COLUMNS:
        if column in df.columns:
            df.drop(column, axis=1, inplace=True)
    return df 


def categories(df: pd.DataFrame):
    df = df.copy()
    for column in CATEGORICAL_COLUMNS + TARGET_COLUMN:
        if column in df.columns:
            df[column] = pd.Categorical(df[column])
    return df


def downcasting(df: pd.DataFrame):
    df = df.copy()
    for col in INTEGER_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col],errors= "coerce", downcast='integer')

    for col in FLOAT_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col],errors= "coerce", downcast='float')
    return df


def drop_na_values(df: pd.DataFrame):
    df = df.copy()
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def main():
    df = load_churn_data("/Users/miguelromero/Documents/Projects/churn-prediction/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    df = drop_columns(df)
    df = drop_na_values(df)
    df =categories(df)
    df = downcasting(df)
    print(df.info())

main()