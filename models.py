class Database:
    def __init__(self, connection):
        self.connection = connection

    def initialize_tables(self):
        with self.connection:
            self.connection.execute('''CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                amount REAL,
                category TEXT,
                date TEXT
            )''')

            self.connection.execute('''CREATE TABLE IF NOT EXISTS income (
                id INTEGER PRIMARY KEY,
                amount REAL,
                source TEXT,
                date TEXT
            )''')

            self.connection.execute('''CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY,
                amount REAL,
                category TEXT
            )''')