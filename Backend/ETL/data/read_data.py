import pandas as pd
from backend.ETL.config import DROP_COLUMNS

def load_churn_data(path: str, dropna: bool = True, dropcol: bool=True) -> pd.DataFrame:
    """
    Loads the Telco Churn dataset from a CSV file and performs initial cleaning.

    This function serves as the entry point for the data pipeline, handling 
    the transition from a raw local file to a memory-optimized DataFrame.

    Args:
        path (str): The absolute or relative system path to the raw CSV file.
        dropna (bool): (Defualt = True)If True, removes rows with missing values 
        dropcol (bool): (Defualt = True) If True, removes non-informative columns defined in config.DROP_COLUMNS .

    Returns:
        pd.DataFrame: A cleaned and filtered Pandas DataFrame ready for 
            further preprocessing or exploratory data analysis.
            
    Raises:
        FileNotFoundError: If the provided path does not exist.
    """
    df = pd.read_csv(path)
    if dropna:
        df= drop_na_values(df)
    if dropcol:
        df = drop_columns(df)
    return df

def drop_na_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for column in DROP_COLUMNS:
        if column in df.columns:
            df.drop(column, axis=1, inplace=True)
    return df 

