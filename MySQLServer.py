def create_database():
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",     
            user="Ofentse",           
            password="Thedaywemet@2013" 
       

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle connection or execution errors
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure connection is closed
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()