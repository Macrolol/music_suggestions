"""
suggestion_da.py: Data Access Object for Suggestions
"""

__author__ = "Michael Dormon"

from data_access.postgres_connection import connect, PostgresConnectionError


#this is a dictionary of suggestion types keyed by their name
KEYS = {
    'song' : 'SO',
    'artist': 'AR',
    'album' : 'AL'
}

def get_suggestions_to(suggestee_id, suggestion_type, limit=10):
    '''
    This function returns a list of suggestions of a specific type
    '''
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
    '''
    This function returns a list of suggestions of a specific type
    '''
    try:
        with connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM suggestion WHERE suggester_id = %s AND suggestion_type = %s LIMIT %s", (suggester_id, KEYS[suggestion_type], limit))
            suggestions = cur.fetchall()
            conn.close()
    except PostgresConnectionError as e:
        print(e)
    return suggestions

class SuggestionDA:

    #the following three functions get suggestions suggested to a
    # specific user 
    @staticmethod
    def get_songs_suggested_to(suggestee_id, limit=10):
        '''
        This function returns a list of songs that the suggestee has been
        suggeseted
        '''
        return get_suggestions_to(suggestee_id, 'song', limit)

    @staticmethod
    def get_albums_suggested_to(suggestee_id, limit=10):
        '''
        This function returns a list of albums that the suggester has been suggested
        '''
        return get_suggestions_to(suggestee_id, 'album', limit)

    @staticmethod
    def get_artists_suggested_to(suggestee_id, limit=10):
        '''
        This function returns a list of artists that the suggester has been suggested
        '''
        return get_suggestions_to(suggestee_id, 'artist', limit)


    #the following three functions get suggestions suggested by a
    # specific user

    @staticmethod
    def get_songs_suggested_by(suggester_id, limit=10):
        '''
        This function returns a list of songs that the suggester has suggested to others
        '''
        return get_suggestions_by(suggester_id, 'song', limit)

    @staticmethod
    def get_albums_suggested_by(suggester_id, limit=10):
        '''
        This function returns a list of albums that the suggester has suggested to others
        '''
        return get_suggestions_by(suggester_id, 'album', limit)
    
    @staticmethod
    def get_artists_suggested_by(suggester_id, limit=10):
        '''
        This function returns a list of artists that the suggester has suggested to others
        '''
        return get_suggestions_by(suggester_id, 'artist', limit)


    #the following function gets a single suggestion by its id
    @staticmethod
    def get_suggestion_by_id(suggestion_id):
        '''
        This function returns a single suggestion with a specific id
        '''
        try:
            with connect() as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM suggestion WHERE suggestion_id = %s", (suggestion_id))
                suggestion = cur.fetchone()
                conn.close()
        except PostgresConnectionError as e:
            print(e)
        return suggestion

    
if __name__ == "__main__":
    pass