import sqlite3
import os

class Database:
    
    def __init__(self, db_name='chatbot_database.sqlite', check_connection=True):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(current_dir, f'../../data/{db_name}')
        
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            
            if check_connection:
                self._check_connection()
        
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database: {e}")
            raise

    def _check_connection(self):
        self.cursor.execute('SELECT SQLITE_VERSION()')
        data = self.cursor.fetchone()
        print(f"SQLite version: {data}")

    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            raise

    def fetch_all(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching all: {e}")
            raise

    def fetch_one(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error fetching one: {e}")
            raise

    def close(self):
        self.connection.close()