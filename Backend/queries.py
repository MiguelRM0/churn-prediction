from .db import get_connection # Look at db.py


def list_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows