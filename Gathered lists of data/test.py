import sqlite3
import os
import re

def create_table(conn, table_name):
    # Check if table exists
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    if cursor.fetchone():
        print(f"Table '{table_name}' already exists.")
        return

    # Table doesn't exist, create it
    create_table_query = f"""
    CREATE TABLE "{table_name}" (
        data TEXT
    )
    """
    cursor.execute(create_table_query)
    print(f"Table '{table_name}' created successfully.")

def read_data_from_file(file_path):
    if not os.path.isfile(file_path):
        print(f"File '{file_path}' not found.")
        return []

    with open(file_path, 'r') as file:
        # Read the whole file content and split it by newline characters
        data = file.read().split('\n')
        # Remove empty lines
        data = [line.strip() for line in data if line.strip()]
        return [(line,) for line in data]

def insert_data(conn, table_name, data):
    cursor = conn.cursor()
    insert_query = f"INSERT INTO \"{table_name}\" (data) VALUES (?)"
    cursor.executemany(insert_query, data)
    conn.commit()
    print(f"Data inserted into '{table_name}' successfully.")

def main():
    # Connect to SQLite database
    conn = sqlite3.connect('mydatabase.db')

    while True:
        table_name = input("Enter the name of the table (or type 'quit' to exit): ").strip()
        if table_name.lower() == 'quit':
            break

        # Remove any characters that are not alphanumeric or underscores
        table_name = re.sub(r'\W+', '_', table_name)

        create_table(conn, table_name)

        file_path = input("Enter the path of the file containing data: ").strip()
        data = read_data_from_file(file_path)

        if data:
            insert_data(conn, table_name, data)

        more_tables = input("Do you want to create more tables? (yes/no): ").strip().lower()
        if more_tables != 'yes':
            break

    conn.close()

if __name__ == "__main__":
    main()
