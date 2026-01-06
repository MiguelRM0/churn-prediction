from src.config import TARGET_COLUMN
import pandas as pd

def build_features(df: pd.DataFrame):
    X = df.drop(columns=TARGET_COLUMN)
    y = df[TARGET_COLUMN]
    return X, y