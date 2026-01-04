import pandas as pd

def load_churn_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)