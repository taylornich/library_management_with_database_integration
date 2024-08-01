from connect_database import connect_db
from mysql.connector import Error

def add_user(name, library_id):
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Users (name, library_id) VALUES (%s, %s)"
            cursor.execute(query, (name, library_id))
            conn.commit()
            print("User added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def view_user_details(library_id):
    conn = connect_db()

    if conn: 
        try: 
            cursor = conn.cursor()
            query = "SELECT name, library_id, FROM Users WHERE library_id = %s"
            cursor.execute(query, (library_id,))
            result = cursor.fetchall()

            if result:
                print(f"User details: Name {result[0]}, Library ID: {result[1]}")
            else:
                print("User not in database.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def display_users():
    conn = connect_db()

    if conn: 
        try: 
            cursor = conn.cursor()
            query = "SELECT name, library_id FROM Users"
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(f"Name: {row[0]}, Library ID: {row[1]}")
        except Error as e:
            print(f"Error: {e}")
        finally: 
            cursor.close()
            conn.close()

