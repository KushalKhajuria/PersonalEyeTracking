import psycopg2

DB_NAME =
DB_USER =
DB_PASS =
DB_HOST =

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)

cur = conn.cursor()

cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR")

cur.close()

conn.close()