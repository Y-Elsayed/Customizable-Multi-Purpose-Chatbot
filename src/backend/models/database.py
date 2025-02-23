import sqlite3



class Database:
    def __init__(self, db_path,check_connection=False):
        self.db_path = db_path
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()

            if check_connection:
                self._check_connection()

        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database: {e}")
            raise

    def _check_connection(self):
        self.cursor.execute("SELECT SQLITE_VERSION()")
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
