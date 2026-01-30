import pandas as pd
import sqlalchemy as db
from src.data.clean import categories, downcasting
from src.data.read_data import load_churn_data
# Testing Loading data into postgressSQL local database
# WIll be loading in cleaned data but plan to pipeline process
def main():
    print("Hello World")
    df = load_churn_data("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    df = categories(df)
    df = downcasting(df)
    # print(df.info())


    engine = db.create_engine("postgresql+psycopg2://miguelromero@localhost:5432/churn-data")
    df.to_sql(
        name = "churn-data",
        con = engine,
        if_exists="replace",
        index = False
    )
    


main()