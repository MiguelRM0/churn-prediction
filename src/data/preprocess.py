import pandas as pd
from src.data.load_data import load_churn_data
from src.config import DROP_COLUMNS, TARGET_COLUMN, NUMERIC_COLUMNS, CATEGORICAL_COLUMNS


df = load_churn_data("/Users/miguelromero/Documents/Projects/churn-prediction/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())