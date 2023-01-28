import sqlite3


# Routine to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Routine to print the existing table contents of already created urls
def main():
    conn = get_db_connection()
    sql_select_Query = "select * from url_table"
    cursor = conn.cursor()
    cursor.execute(sql_select_Query)
    # get all records in the table
    records = cursor.fetchall()
    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("original_url = ", row[1])
        print("short_id = ", row[2])


if __name__ == "__main__":
    main()
