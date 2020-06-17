import psycopg2 as pg

conn = pg.connect("dbname=example user=postgres password=abcd@1234")
cur = conn.cursor()

SQL_ = """
CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    describe VARCHAR,
    isboy BOOLEAN DEFAULT False
);
"""
cur.execute(SQL_)

conn.commit()
cur.close()
conn.close()
