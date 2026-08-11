import sqlite3
import os

DB_PATH = "data/activity_tracker.db"

def create_database():

    os.makedirs("data" ,exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()
    # window activity table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activity_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_time TEXT,
            end_time TEXT,
            duration TEXT,
            window_title TEXT
        )
    """)
    # Browser activity table 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS browser_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            title TEXT,
            url TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("Database ready")


def save_activity(start_time, end_time, duration, window_title):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO activity_log
        (start_time, end_time, duration, window_title)
        VALUES (?, ?, ?, ?)
    """, (
        str(start_time),
        str(end_time),
        str(duration),
        str(window_title),
    ))

    conn.commit()
    conn.close()



def get_all_activity():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, start_time, end_time, duration, window_title
        FROM activity_log
        ORDER BY id DESC
    """)
    
    rows = cursor.fetchall()

    conn.close()

    return rows

def save_browser_activity(title , url):
    conn = sqlite3.connect("data/activity_tracker.db")
    cursor = conn.cursor()


    cursor.execute("""
        INSERT INTO browser_activity
        (timestamp , title ,url)
        VALUES (datetime('now','localtime'), ?, ?)
    """, (title, url))

    conn.commit()
    conn.close()


def get_browser_activity():

    conn = sqlite3.connect("data/activity_tracker.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp,title , url
        FROM browser_activity
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()

    return rows



