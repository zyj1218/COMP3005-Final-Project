import psycopg2


def connect_to_postgresql():
    # Get user inputs for database connection details
    db_name = input("Enter database name: ")
    user = input("Enter username(postgres): ")
    password = input("Enter password: ")

    conn_string = f"dbname='{db_name}' user='{user}' host='localhost' password='{password}'"

    try:
        conn = psycopg2.connect(conn_string)
        # Check if the connection was successful
        if conn is not None:
            print("Successfully connected to PostgreSQL database!")
            return conn
    except Exception as e:
        print(f"An error occurred: {e}")
