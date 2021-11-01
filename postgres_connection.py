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



def get_songs_suggested_to(suggestee, limit=10):
    '''
    This function returns a list of songs that the suggestee has been
    suggeseted
    '''
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM suggestion WHERE suggestee_id = %s AND suggestion_type = 'SO' LIMIT %s", (suggestee, limit))
    songs = cur.fetchall()
    conn.close()
    return songs

def get_songs_suggested_by(suggester, limit=10):
    '''
    This function returns a list of songs that the suggester has suggested to others
    '''
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM suggestion WHERE suggester_id = %s AND suggestion_type = 'SO' LIMIT %s", (suggester, limit))
    songs = cur.fetchall()
    conn.close()
    return songs

def get_albums_suggested_to(suggestee, limit=10):
    '''
    This function returns a list of albums that the suggester has been suggested
    '''
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM suggestion WHERE suggestee_id = %s AND suggestion_type = 'AL' LIMIT %s", (suggestee, limit))
    albums = cur.fetchall()
    conn.close()
    return albums

def get_albums_suggested_by(suggester, limit=10):
    '''
    This function returns a list of albums that the suggester has suggested to others
    '''
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM suggestion WHERE suggester_id = %s AND suggestion_type = 'AL' LIMIT %s", (suggester, limit))
    albums = cur.fetchall()
    conn.close()
    return albums

def get_artists_suggested_to(suggestee, limit=10):
    '''
    This function returns a list of artists that the suggester has been suggested
    '''
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM suggestion WHERE suggestee_id = %s AND suggestion_type = 'AR' LIMIT %s", (suggestee, limit))
    artists = cur.fetchall()
    conn.close()
    return artists

def get_artists_suggested_by(suggester, limit=10):
    '''
    This function returns a list of artists that the suggester has suggested to others
    '''
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM suggestion WHERE suggester_id = %s AND suggestion_type = 'AR' LIMIT %s", (suggester, limit))
    artists = cur.fetchall()
    conn.close()
    return artists









