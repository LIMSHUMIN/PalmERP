import pyodbc
from config import Config


def get_connection():

    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={Config.DB_SERVER};"
        f"DATABASE={Config.DB_DATABASE};"
        "Trusted_Connection=yes;"
    )

    try:
        conn = pyodbc.connect(connection_string)
        print("SQL Server connection successful")
        return conn

    except Exception as e:
        print("Database connection failed")
        print(e)
        return None