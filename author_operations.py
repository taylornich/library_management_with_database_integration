from connect_database import connect_db
from mysql.connector import Error

def add_author(name, biography):
    conn = conn.cursor()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Authors (name, biography) VALUES (%s, %s)"
            cursor.execute(query, (name, biography))
            conn.commit()
            print("Author added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def view_author_details(author_id):
    conn = conn.cursor()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT name, biography FROM Authors WHERE id = %s"
            cursor.execute(query, (author_id,))
            conn.commit()
            result = cursor.fetchone()
            if result:
                print(f"Author Details: Name {result[0]}, Biography: {result[1]}")
            else:
                print("Author not in the database.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def display_authors():
    conn = conn.cursor()
    if conn:
        try: 
            cursor = conn.cursor()
            query = "SELECT name, biography FROM Authors"
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(f"Author Details: Name: {row[0]}, Biography: {row[1]}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

