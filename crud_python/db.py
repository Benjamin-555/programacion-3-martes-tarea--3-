import sqlite3

class Database:
    def __init__(self, db_name="app.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = ?"
        self.conn.execute(query, (user_id,))
        self.conn.commit()

    def update_user(self, user_id, new_name, new_email):
        query = """
        UPDATE users
        SET name = ?, email = ?
        WHERE id = ?
        """
        self.conn.execute(query, (new_name, new_email, user_id))
        self.conn.commit()
