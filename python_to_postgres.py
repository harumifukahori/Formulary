import psycopg2
from peewee import PostgresqlDatabase

database = PostgresqlDatabase(None)

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'Bazinga3'
port_id = 5432
conn = None
cur = None
try:
    conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS usuario')

    create_script = ''' CREATE TABLE IF NOT EXISTS usuario (
                            id         int PRIMARY KEY,
                            nome       varchar(40) NOT NULL,
                            senha      int,
                            username  varchar(30)) '''
    cur.execute(create_script)

    insert_script = 'INSERT INTO usuario (id, nome, senha, username) VALUES (%s, %s, %s, %s)'
    insert_values = [(1, 'Harumi', '1200', 'Haru'), (2, 'Khaleesi', '1300', 'Kha'), (3, 'Yshtola', '1400', 'Ysh')]
    for record in insert_values:
        cur.execute(insert_script, record)

    cur.execute("SELECT * FROM USUARIO")
    for record in cur.fetchall():
        print(record)

    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


def db():
    return None
