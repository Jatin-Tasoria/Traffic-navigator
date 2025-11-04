import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="traffic_db",
        user="postgres",
        password="your_password",
        host="localhost",
        port="5432"
    )
