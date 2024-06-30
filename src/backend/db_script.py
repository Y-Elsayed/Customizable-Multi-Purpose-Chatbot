import sqlite3
import os

class Database:
    
    def __init__(self, db_name='database.sqlite', check_connection = True):
        # Get the path to the current directory where the script is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the path to the database file in the data folder
        self.db_path = os.path.join(current_dir, f'../../data/{db_name}')
        
        # Connect to the SQLite database
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        if check_connection == True:
            self._check_connection()

    def _check_connection(self):
        self.cursor.execute('SELECT SQLITE_VERSION()')
        data = self.cursor.fetchone()
        print(f"SQLite version: {data}")

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()

# Example usage
if __name__ == "__main__":
    db = Database('example_database.sqlite')
    
    # Example: Creating a table
    db.execute_query('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
    ''')

    # Example: Inserting data
    db.execute_query('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 22))

    # Example: Fetching data
    users = db.fetch_all('SELECT * FROM users')
    print(users)

    # Close the database connection when done
    db.close()
