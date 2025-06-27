import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.conn = None

    def connect(self):
        """Connect to the PostgreSQL database server."""
        try:
            self.conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )
            print("Database connection established.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def disconnect(self):
        """Disconnect from the PostgreSQL database server."""
        if self.conn is not None:
            self.conn.close()
            print("Database connection closed.")

    def execute_query(self, query, params=None):
        """Execute a SQL query."""
        if self.conn is None:
            self.connect()
        
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, params)
                self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.conn.rollback()

    def fetch_query(self, query, params=None):
        """Execute a SQL query and return results."""
        if self.conn is None:
            self.connect()
            
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, params)
                return cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

if __name__ == '__main__':
    db = Database()
    db.connect()
    # Example usage (optional)
    # db.execute_query("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, name VARCHAR(255));")
    # db.execute_query("INSERT INTO test (name) VALUES (%s);", ('test_value',))
    # print(db.fetch_query("SELECT * FROM test;"))
    db.disconnect()
