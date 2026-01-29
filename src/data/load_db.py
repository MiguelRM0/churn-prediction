import pandas as pd
import sqlalchemy as db
# Testing Loading data into postgressSQL local database
# WIll be loading in cleaned data but plan to pipeline process
def main():
    print("Hello World")
    df = pd.read_csv("/Users/miguelromero/Documents/Projects/churn-prediction/data/cleaned_churn.csv")
    print(df.head())
    print(df.info())


main()