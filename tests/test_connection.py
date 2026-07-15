import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from database.connection import get_connection

conn = get_connection()

if conn:
    print("Connected Successfully")
else:
    print("Connection Failed")