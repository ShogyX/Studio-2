import sqlite3
from sqlite3 import Error

#This document is currently made to be an interface with the main_db, to allow us to create and modify tables and data.
#Currently no production tables has been made.


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

#This is the proposed strucutre for the table with all the common words.
sql_create_table_word_table = """ 
CREATE TABLE IF NOT EXISTS common_words_table (
id integer PRIMARY KEY,
word text NOT NULL,
language text NOT NULL,
region text); 
"""

#This is the proposed strucutre for table with common passwords. 
#The language and region are included but not neccesasry to allow for the option of sorting common passwords in different languages if that is a route we wish to tread.
sql_create_table_password_table = """ 
CREATE TABLE IF NOT EXISTS common_password_table (
id integer PRIMARY KEY,
password text NOT NULL,
language text,
region text); 
"""

sql_delete = 'DELETE FROM Test_Table WHERE id=?'

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