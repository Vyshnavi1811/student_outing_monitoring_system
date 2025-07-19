import sqlite3
from datetime import datetime, timedelta

DB_NAME = 'outing.db'

def connect_db():
    return sqlite3.connect(DB_NAME, detect_types=sqlite3.PARSE_DECLTYPES)

def init_db():
    with connect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS outings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                out_time TIMESTAMP NOT NULL,
                in_time TIMESTAMP
            )
        ''')
        conn.commit()

def register_outing(student_id):
    with connect_db() as conn:
        conn.execute('''
            INSERT INTO outings (student_id, out_time) VALUES (?, ?)
        ''', (student_id, datetime.now()))
        conn.commit()

def check_in(student_id):
    with connect_db() as conn:
        conn.execute('''
            UPDATE outings SET in_time = ? 
            WHERE student_id = ? AND in_time IS NULL
        ''', (datetime.now(), student_id))
        conn.commit()

def get_pending_students():
    threshold = datetime.now() - timedelta(hours=24)
    with connect_db() as conn:
        cursor = conn.execute('''
            SELECT student_id, out_time FROM outings 
            WHERE in_time IS NULL AND out_time < ?
        ''', (threshold,))
        rows = cursor.fetchall()
    return [{'student_id': row[0], 'out_time': row[1].isoformat() if row[1] else None
             } for row in rows]
def get_logs(student_id):
    with connect_db() as conn:
        cursor = conn.execute(
            "SELECT out_time, in_time FROM outings WHERE student_id = ? ORDER BY out_time DESC",
            (student_id,)
        )
        rows = cursor.fetchall()
    return [{'out_time': row[0], 'in_time': row[1]} for row in rows]

