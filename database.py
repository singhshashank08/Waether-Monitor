import sqlite3

def create_db():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            city TEXT,
            date TEXT,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_daily_summary(city, date, avg_temp, max_temp, min_temp, dominant_condition):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO daily_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (city, date, avg_temp, max_temp, min_temp, dominant_condition))

    conn.commit()
    conn.close()

def fetch_all_summaries():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM daily_summary')
    rows = cursor.fetchall()

    conn.close()
    return rows
