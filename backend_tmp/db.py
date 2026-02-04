import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
'''
This db.py creates a connection to my churn-data database. This will be used in conjunction with 
queries to get quieries for my database. In order for this to work PostgreSQL server must be running and all information below must be correct.
'''


# Function to get a connection to the PostgreSQL database
def get_connection():
    load_dotenv()# Load environment variables from .env file
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=None,  # It's generally not recommended to hardcode passwords, consider using environment variables
        cursor_factory=RealDictCursor
    )

'''
Using RealDictCursor in order to get better formatted SQL results
'''