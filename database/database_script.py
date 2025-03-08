import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('domainRadar.db')
cursor = conn.cursor()

# Create a table for storing domain information
cursor.execute('''
CREATE TABLE IF NOT EXISTS domains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_name TEXT NOT NULL,
    registration_date TEXT NOT NULL,
    registrar TEXT NOT NULL,
    industry_keywords TEXT,
    whois_data TEXT
)
''')

# Create a table for storing user keywords
cursor.execute('''
CREATE TABLE IF NOT EXISTS user_keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    keyword TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()