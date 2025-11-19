import sqlite3

def get_user_details(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerable: direct string concatenation
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    cursor.execute(query)

    return cursor.fetchall()
