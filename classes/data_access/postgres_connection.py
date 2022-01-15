
"""
postgres_connection.py: This file defines the connect() function used to connect to the Postgres database.
    as well as the PostgresConnectionError exception. It also builds the connection string used to connect
    to the database.
    Ther connection string is built using the following environment variables:
    'DB_NAME' - the name of the database to connect to
    'DB_USER' - the username to connect with
    'DB_HOST' - the hostname of the database
    'DB_PASSWORD' - the password to connect with
"""

__author__ = "Michael Dormon"


import os

from psycopg2 import connect as pg_connect, OperationalError
from psycopg2.extras import RealDictCursor




#build the connection string
connection_string = ""
if os.environ['DB_NAME'] == 'testing_db':    
    connection_string = "dbname='{}' user='{}' host='{}'".format(
        os.environ['DB_NAME'],
        os.environ['DB_USER'],
        os.environ['DB_HOST'])
else:
    connection_string = "dbname='{}' user='{}' host='{}' password='{}'".format(
        os.environ['DB_NAME'],
        os.environ['DB_USER'],
        os.environ['DB_HOST'],
        os.environ['DB_PASSWORD'])

class PostgresConnectionError(Exception):
    """
    Error raised when there is a problem connecting to the database.
    """
    pass



def connect():
    #connect to the pg instance
    print("connecting with connection string: {}", connection_string) #debug
    try:
        conn = pg_connect(connection_string, cursor_factory=RealDictCursor)
    except OperationalError as e:
        print("Unable to connect to the database") #debug
        raise PostgresConnectionError(e)
    print("connected") #debug
    return conn








