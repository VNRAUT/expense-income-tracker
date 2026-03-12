import sqlite3

def init_db():
    # Connect to the SQLite database (it will create it if it doesn't exist)
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    # Create a table for expenses
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY,
                        description TEXT NOT NULL,
                        amount REAL NOT NULL,
                        date TEXT NOT NULL
                    )''')

    # Create a table for income
    cursor.execute('''CREATE TABLE IF NOT EXISTS income (
                        id INTEGER PRIMARY KEY,
                        source TEXT NOT NULL,
                        amount REAL NOT NULL,
                        date TEXT NOT NULL
                    )''')

    # Commit and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()