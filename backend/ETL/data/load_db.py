import pandas as pd
import sqlalchemy as db
from ETL.data.clean import categories, downcasting
from ETL.data.read_data import load_churn_data
import os 
from dotenv import load_dotenv

# WIll be loading in cleaned data but plan to pipeline process
def main():
    load_dotenv()
    df = load_churn_data("raw data/WA_Fn-UseC_-Telco-Customer-Churn.csv", dropna=True, dropcol=True)
    df = categories(df)
    df = downcasting(df)
    # print(df.info())
   
    # Construct the DATABASE_URL using environment variables
    DATABASE_URL = (f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")


    engine = db.create_engine(DATABASE_URL)
    df.to_sql(
        name = os.getenv("DB_NAME"),
        con = engine,
        if_exists="replace",
        index = False
    )
    print(f"Data loaded successfully into the database. URL used: {DATABASE_URL}). Database_name: {os.getenv('DB_NAME')}" )


main()