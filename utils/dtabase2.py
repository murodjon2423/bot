import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_product(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()
