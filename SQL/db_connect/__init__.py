from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

conn = None
cursor = None

def Open():
    global conn
    conn = pyodbc.connect(f"""
                        Driver={{ODBC Driver 17 for SQL Server}};
                        Server={os.environ.get("SERVER")};
                        Database={os.environ.get("DATABASE")};
                        UID={os.environ.get("UID")};
                        """)

    global cursor
    cursor = conn.cursor()
    return cursor

def Close():
    global cursor
    cursor.close()

    global conn
    conn.close()
