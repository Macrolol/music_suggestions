from psycopg2 import connect as pg_connect, OperationalError
import os



#build the connection string
connection_string = "dbname='{}' user='{}' host='{}' password='{}'".format(
    os.environ['DB_NAME'],
    os.environ['DB_USER'],
    os.environ['DB_HOST'],
    os.environ['DB_PASSWORD'])


class PostgresConnectionError(Exception):
    
    def __init__(self, message):
        super.__init__(self, message)
        self.message = message


def connect():
    #connect to the pg instance
    print("connecting") #debug
    try:
        conn = pg_connect(connection_string)
    except OperationalError as e:
        print("Unable to connect to the database") #debug
        raise PostgresConnectionError(e)
    print("connected") #debug
    return conn








