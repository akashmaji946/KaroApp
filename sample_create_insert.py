import psycopg2 as pg

conn = pg.connect("dbname=example user=postgres password=iw2cGB@now")
cur = conn.cursor()

SQL_ = """
CREATE TABLE table3 (
    id INTEGER PRIMARY KEY,
    describe VARCHAR,
    isboy BOOLEAN DEFAULT False
);
"""
cur.execute(SQL_)

insert = """
INSERT INTO table3(id, describe) VALUES (%s, %s)
"""
values = (1, "Akash")

cur.execute(insert, values)

insert2 = """
INSERT INTO table3(id, describe) VALUES (%(id)s, %(describe)s)
"""
values2 = {"id": 2, "describe": "Akash MAji"}

cur.execute(insert2, values2)

conn.commit()
cur.close()
conn.close()
