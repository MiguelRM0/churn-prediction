import psycopg2
from psycopg2.extras import RealDictCursor
'''
This db.py creates a connection to my churn-data database. This will be used in conjunction with 
queries to get quieries for my database. In order for this to work PostgreSQL server must be running and all information below must be correct.
'''



def get_connection():
    return psycopg2.connect(
        host='localhost',
        dbname="churn_data",
        user="miguelromero",
        password=None,
        cursor_factory=RealDictCursor
    )

'''
Using RealDictCursor in order to get better formatted SQL results
'''