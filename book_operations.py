from connect_database import connect_db
from mysql.connector import Error


def add_book(title, author_id, genre_id, isbn, publication_date):
    conn = connect_db()
    if conn:
        try: 
            cursor = conn.cursor()
            query = "INSERT INTO Books (title, author_id, genre_id, publication_date) VALUES (%s, %s, %s, %s)"

            cursor.execute(query, (title, author_id, genre_id, publication_date))
            conn.commit()
            print("Book added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def borrow_book(user_id, book_id, borrow_date):
    conn = connect_db()

    if conn: 
        try: 
            cursor = conn.cursor()
            query = "UPDATE Books SET availability = FALSE WHERE id = %s"
            cursor.execute(query, (book_id,))

            query = "INSERT INTO Borrowed_Books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, book_id, borrow_date))
            conn.commit()
            print("Book borrowed successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()


def return_book(user_id, book_id, return_date):
    conn = connect_db()
    if conn: 
        try:
            cursor = conn.cursor()
            query = "UPDATE Books SET availability = TRUE WHERE id = %s"
            cursor.execute(query, (book_id,))

            query = "UPDATE Borrowed_Books SET return_date = %s WHERE user_id = %s AND book_id = %s AND return_date = NULL"
            cursor.execute(query, (user_id, book_id, return_date))
            conn.commit()
            print("Book returned successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()


def search_book(search_parameters):
   conn = connect_db()
   if conn:
        try: 
           cursor = conn.cursor()
           query = "SELECT b.title, a.name, b.isbn, b.publication_date, b.availability FROM Books b JOIN Authors a ON b.author_id = a.id WHERE b.isbn = %s"
           cursor.execute(query, (search_parameters))
           results = cursor.fetchall()

           for row in results:
               print(f"Title: {row[0]}, Author: {row[1]}, ISBN: {row[2]}, Publication Date: {row[3]}, Available: {'Yes' if row[4] else 'No'}")
        except Error as e:
            print(f"Error: {e}")
        finally: 
            cursor.close()
            conn.close()


def display_books():
    conn = connect_db()
    if conn:
        try: 
            cursor = conn.cursor()
            query = "SELECT b.title, a.name, b.isbn, b.publication_date, b.availability FROM Books b JOIN Author a ON b.author_id = a.id"
            cursor.execute(query)
            results = cursor.fetchall()

            for row in results:
                print(f"Title: {row[0]}, Author: {row[1]}, ISBN: {row[2]}, Publication Date: {row[3]}, Available: {'Yes' if row[4] else 'No'}")
        except Error as e:
            print(f"Error: {e}")
        finally: 
            cursor.close()
            conn.close()