import pandas as pd
from src.data.load_data import load_churn_data
from src.config import TARGET_COLUMN,CATEGORICAL_COLUMNS, INTEGER_COLUMNS, FLOAT_COLUMNS



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



def main():
    df = load_churn_data("/Users/miguelromero/Documents/Projects/churn-prediction/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    df = categories(df)
    df = downcasting(df)

    df.to_csv("data/cleaned_churn.csv", index=False)
    print("✅ Stage 1 Complete: Cleaned data saved to data/cleaned_churn.csv")


if __name__ == "__main__":
    main()