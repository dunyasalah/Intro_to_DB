#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server
    db = mysql.connector.connect(
        host="localhost",
        user="root",          
        password="D40021142aynud"  
    )

    if db.is_connected():
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()
