from backend.ETL.config import TARGET_COLUMNS
import pandas as pd

def build_features(df: pd.DataFrame):
    X = df.drop(columns=TARGET_COLUMNS)
    y = df[TARGET_COLUMNS]
    return X, y