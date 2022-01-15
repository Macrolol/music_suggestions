"""
suggestion_da.py: Data Access Object for Suggestions
"""

__author__ = "Michael Dormon"

from classes.data_access.da_exceptions import DatabaseConnectionError
from data_access.postgres_connection import connect, PostgresConnectionError


#this is a dictionary of suggestion types as stored in the DB keyed by their name
KEYS = {
    'song' : 'SO',
    'artist': 'AR',
    'album' : 'AL'
}


def get_suggestions_to(suggestee_id, suggestion_type, limit=10):
    """
    This function returns a list of suggestions of a specific type
    that have been suggested to a specific user

    This is not meant to be used outside of the methods definded in the
    SuggestionDA class. 
    """
    try:
        with connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM suggestion WHERE suggestee_id = %s AND suggestion_type = %s LIMIT %s", (suggestee_id, KEYS[suggestion_type], limit))
            suggestions = cur.fetchall()
            conn.close()
    except PostgresConnectionError as e:
        print(e)
    return suggestions

def get_suggestions_by(suggester_id, suggestion_type, limit=10):
    """
    This function returns a list of suggestions of a specific type
    that have been suggested by a specific user

    This is not meant to be used outside of the methods definded in the
    SuggestionDA class.
    """
    try:
        with connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM suggestion WHERE suggester_id = %s AND suggestion_type = %s LIMIT %s", (suggester_id, KEYS[suggestion_type], limit))
            suggestions = cur.fetchall()
            conn.close()
    except PostgresConnectionError as e:
        print(e)
    return suggestions

def add_artist(artist_name):
    """
    This function adds an artist to the database

    This is not meant to be used outside of the methods definded in the
    SuggestionDA class.
    """
    try:
        with connect() as conn:
            cur = conn.cursor()
            effected_rows = cur.execute("INSERT INTO artist (artist_name) VALUES (%s)", (artist_name))
            conn.close()
    except PostgresConnectionError as e:
        print(e) #debug
        raise DatabaseConnectionError("Could not connect to database")

def add_album(album_name, artist_name):
    """
    This function adds an album to the database

    This is not meant to be used outside of the methods definded in the
    SuggestionDA class.
    """
    try:
        with connect() as conn:
            cur = conn.cursor()
            cur.execute("SQL query that checks if an artist by the given name exists and if not ")
            conn.commit()
            conn.close()
    except PostgresConnectionError as e:
        print(e) #debug
        raise DatabaseConnectionError("Could not connect to database")

    



class SuggestionDA:

    #the following three functions get suggestions suggested to a
    # specific user 

    @staticmethod
    def get_songs_suggested_to(suggestee_id, limit=10):
        """
        This function returns a list of songs that the suggestee has been
        suggested
        """
        return get_suggestions_to(suggestee_id, 'song', limit)

    @staticmethod
    def get_albums_suggested_to(suggestee_id, limit=10):
        """
        This function returns a list of albums that the suggester has been suggested
        """
        return get_suggestions_to(suggestee_id, 'album', limit)

    @staticmethod
    def get_artists_suggested_to(suggestee_id, limit=10):
        """
        This function returns a list of artists that the suggester has been suggested
        """
        return get_suggestions_to(suggestee_id, 'artist', limit)


    #the following three functions get suggestions suggested by a
    # specific user

    @staticmethod
    def get_songs_suggested_by(suggester_id, limit=10):
        """
        This function returns a list of songs that the suggester has suggested to others
        """
        return get_suggestions_by(suggester_id, 'song', limit)

    @staticmethod
    def get_albums_suggested_by(suggester_id, limit=10):
        """
        This function returns a list of albums that the suggester has suggested to others
        """
        return get_suggestions_by(suggester_id, 'album', limit)
    
    @staticmethod
    def get_artists_suggested_by(suggester_id, limit=10):
        """
        This function returns a list of artists that the suggester has suggested to others
        """
        return get_suggestions_by(suggester_id, 'artist', limit)


    @staticmethod
    def get_suggestion_by_id(suggestion_id):
        """
        This function returns a single suggestion with a specific id
        """
        try:
            with connect() as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM suggestion WHERE suggestion_id = %s", (suggestion_id))
                suggestion = cur.fetchone()
                conn.close()
        except PostgresConnectionError as e:
            print(e)
        return suggestion


    @staticmethod
    def add_artist_suggestion(suggester_id, suggestee_id, artist_name):
        """
        This function adds an artist suggestion to the DB.

        If the artist already exists in the database only the suggestion
        relationship will be added, otherwise the artist and the suggestion
        relationship will be added.
        """
        pass #TODO implement this

    @staticmethod
    def add_album_suggestion(suggester_id, suggestee_id, album_name, artist_name):
        """
        This function adds an album suggestion to the DB.

        If the album already exists in the database only the suggestion
        relationship will be added, otherwise the album and the suggestion
        relationship will be added.
        """
        pass
    
    @staticmethod
    def add_song_suggestion(suggester_id, suggestee_id, song_name, album_name, artist_name):
        """
        This function adds a song suggestion to the DB.

        If the song already exists in the database only the suggestion
        relationship will be added, otherwise the song and the suggestion
        relationship will be added.
        """
        pass #TODO: implement this






    
if __name__ == "__main__":
    pass