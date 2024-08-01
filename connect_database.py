import mysql.connector
from mysql.connector import Error

def connect_db():
    db_name = "LibraryManagementSystem"
    user = "root"
    password = ""
    host = "localhost"

    try: 
        conn = mysql.connector. connect (
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected:
            print("Connected to MySQL database successfully.")
    
    except Error as e:
        print(f"Error: {e}")
        return None
