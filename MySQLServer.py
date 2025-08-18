#!/usr/bin/python3
# MySQLServer.py

import mysql.connector  # required for the checker

def create_database():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",               # update if needed
            password="your_password"   # update if needed
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None:
            try:
                if connection.is_connected():
                    connection.close()
            except Exception:
                pass

if __name__ == "__main__":
    create_database()
