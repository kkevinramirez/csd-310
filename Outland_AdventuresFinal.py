import mysql.connector


def display_data(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    print("\n - - {} - -".format(table_name))
    for row in rows:
        print(row)


def main():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',  # Update with your host
        user='root',  # Update with your username
        password='password',  # Update with your password
        database='Outland_Adventures'  # Your database name
    )

    cursor = connection.cursor()

    # List of tables to display data from
    tables = [
        'Department',
        'Employees',
        'Equipment',
        'Trip_Information',
        'Booking',
        'Customers',
        'Inventory'
    ]

    for table in tables:
        display_data(cursor, table)

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()