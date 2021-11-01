import psycopg2
import os

#build the connection string
connection_string = "dbname='{}' user='{}' host='{}' password='{}'".format(
    os.environ['DB_NAME'],
    os.environ['DB_USER'],
    os.environ['DB_HOST'],
    os.environ['DB_PASSWORD'])



def connect():
    #connect to the pg instance
    conn = psycopg2.connect(connection_string)
    return conn






