import pyodbc

from config import *


def get_connection():

    try:

        if USE_WINDOWS_AUTH:

            conn = pyodbc.connect(
                f"""
                DRIVER={{ODBC Driver 18 for SQL Server}};
                SERVER={SERVER};
                DATABASE={DATABASE};
                Trusted_Connection=yes;
                TrustServerCertificate=yes;
                """
            )

        else:

            conn = pyodbc.connect(
                f"""
                DRIVER={{ODBC Driver 18 for SQL Server}};
                SERVER={SERVER};
                DATABASE={DATABASE};
                UID={USERNAME};
                PWD={PASSWORD};
                TrustServerCertificate=yes;
                """
            )

        return conn

    except Exception as e:

        print(e)

        return None