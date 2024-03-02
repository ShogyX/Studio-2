import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Connected!")
            return conn
    
#This is the default db connection
conn = create_connection(r"Database_main.db")

def Execute_command(conn, create_table_sql):
    #Wortker function that will create a table using the default db connection
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def Fetch_data(conn, select_statement):
    cur = conn.cursor()
    cur.execute(select_statement)

    rows = cur.fetchall()
    return rows


sql_delete = 'DELETE FROM Test_Table WHERE id=?'

sql_create_table = """ 
CREATE TABLE IF NOT EXISTS Test_Table (
id integer PRIMARY KEY,
name text NOT NULL,
begin_date text,
end_date text); 
"""

sql_insert = """ 
INSERT INTO Test_Table (id, name, begin_date, end_date)
VALUES(1, 'hello2', 01012001, 01012001)"""

sql_update = '''
UPDATE Test_Table
SET
priority = ? ,
begin_date = ? ,
end_date = ?
WHERE id = ?
'''

sql_select = "SELECT * FROM Test_Table"



#Execute_command(conn, sql_insert)

for row in Fetch_data(conn, sql_select):
    print(row)