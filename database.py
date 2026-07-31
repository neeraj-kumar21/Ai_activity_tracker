import sqlite3

def create_database():
    conn = sqlite3.connect("data/activity_tracker.db")

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS activity_log
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                  window_title TEXT)''')
    
    conn.commit()
    conn.close()

def save_activity(timestamp, window_title):

    conn = sqlite3.connect("data/activity_tracker.db")

    cursor = conn.cursor()

    cursor.execute('''INSERT INTO activity_log (timestamp, window_title)
                      VALUES (?, ?)''', (timestamp, window_title))
    
    conn.commit()
    conn.close()


def get_all_activity():
    conn = sqlite3.connect("data/activity_tracker.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM activity_log")
    
    rows = cursor.fetchall()

    conn.close()

    return rows