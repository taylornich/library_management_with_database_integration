from connect_database import connect_db
from mysql.connector import Error

def add_genre(name, description, category):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Genres (name, description, category) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, description, category))
            conn.commit()
            print("Genre added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally: 
            cursor.close()
            conn.close()

def view_genre_details(name):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT name, description, category FROM Genres WHERE name = %s"
            cursor.execute(query, (name,))
            conn.commit()
            result = cursor.fetchone()
            if result:
                genre_name, description, category = result
                print(f"Genre Details: Name {genre_name}, Description: {description}, Category: {category}")
            else:
                print("Genre not in database.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def display_genres():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT name, description, category from Genres"
            cursor.execute(query)
            conn.commit()
            results = cursor.fetchall()

            if results:
                for row in results:
                    print(f"Genre Details: Name: {row[0]}, Description: {row[1]}, Category: {row[2]}")
            else:
                print("No genres in the database.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
