import pandas as pd
import sqlalchemy as db
from backend.ETL.data.clean import categories, downcasting
from backend.ETL.data.read_data import load_churn_data
import os 
from dotenv import load_dotenv

# WIll be loading in cleaned data but plan to pipeline process
def main():
    df = load_churn_data("raw data/WA_Fn-UseC_-Telco-Customer-Churn.csv", dropna=True, dropcol=True)
    df = categories(df)
    df = downcasting(df)
    # print(df.info())
    load_dotenv()


    engine = db.create_engine(os.getenv("DATABASE_URL"))
    df.to_sql(
        name = os.getenv("DB_NAME"),
        con = engine,
        if_exists="replace",
        index = False
    )
    print(f"Data loaded successfully into the database. URL used: {os.getenv('DATABASE_URL')}). Database_name: {os.getenv('DB_NAME')}" )


main()