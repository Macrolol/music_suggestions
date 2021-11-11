from data_access.postgres_connection import connect, PostgresConnectionError


#this is a dictionary of suggestion types keyed by their name
KEYS = {
    'song' : 'SO',
    'artist': 'AR',
    'album' : 'AL'
}

def get_suggestions_to(suggestee, suggestion_type, limit=10):
    '''
    This function returns a list of suggestions of a specific type
    '''
    try:
        with connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM suggestion WHERE suggestee_id = %s AND suggestion_type = %s LIMIT %s", (suggestee, KEYS[suggestion_type], limit))
            suggestions = cur.fetchall()
            conn.close()
    except PostgresConnectionError as e:
        print(e)
    return suggestions

def get_suggestions_by(suggester, suggestion_type, limit=10):
    '''
    This function returns a list of suggestions of a specific type
    '''
    try:
        with connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM suggestion WHERE suggester_id = %s AND suggestion_type = %s LIMIT %s", (suggester, KEYS[suggestion_type], limit))
            suggestions = cur.fetchall()
            conn.close()
    except PostgresConnectionError as e:
        print(e)
    return suggestions

class SuggestionDA:

    #the following three functions get suggestions suggested to a
    # specific user 

    def get_songs_suggested_to(suggestee, limit=10):
        '''
        This function returns a list of songs that the suggestee has been
        suggeseted
        '''
        return get_suggestions_to(suggestee, 'song', limit)

    def get_albums_suggested_to(suggestee, limit=10):
        '''
        This function returns a list of albums that the suggester has been suggested
        '''
        return get_suggestions_to(suggestee, 'album', limit)

    def get_artists_suggested_to(suggestee, limit=10):
        '''
        This function returns a list of artists that the suggester has been suggested
        '''
        return get_suggestions_to(suggestee, 'artist', limit)


    #the following three functions get suggestions suggested by a
    # specific user

    def get_songs_suggested_by(suggester, limit=10):
        '''
        This function returns a list of songs that the suggester has suggested to others
        '''
        return get_suggestions_by(suggester, 'song', limit)

    def get_albums_suggested_by(suggester, limit=10):
        '''
        This function returns a list of albums that the suggester has suggested to others
        '''
        return get_suggestions_by(suggester, 'album', limit)

    def get_artists_suggested_by(suggester, limit=10):
        '''
        This function returns a list of artists that the suggester has suggested to others
        '''
        return get_suggestions_by(suggester, 'artist', limit)

