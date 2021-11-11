from dataclasses import dataclass
from data_access.suggestion_da import SuggestionDA
from data_access.suggester_da import SuggesterDA




@dataclass
class Suggester(object):
    """This is a a classs that holds information about
    a suggester, including name, contact_info address, and user prefferences"""
    id : int
    name: str
    contact_info: str
    preferences: dict
    suggested_to_items : dict
    suggested_by_items : dict

    #funcitons for getting items suggested to the suggester
    suggested_to_functions ={
    "albums": SuggestionDA.get_albums_suggested_to,
    "artists": SuggestionDA.get_artists_suggested_to,
    "songs": SuggestionDA.get_songs_suggested_to
    }

    #functions for getting items suggested by the suggester
    suggested_by_functions = {
    "albums": SuggestionDA.get_albums_suggested_by,
    "artists": SuggestionDA.get_artists_suggested_by,
    "songs": SuggestionDA.get_songs_suggested_by
    }

    def __init__(self, name, contact_info, preferences=None):
        self.name = name
        self.contact_info = contact_info
        self.preferences = {} if preferences is None else preferences

    def __init__(self, id, name, contact_info, preferences=None):
        self.id = id
        self.name = name
        self.contact_info = contact_info
        self.preferences = {} if preferences is None else preferences

    @staticmethod
    def from_id(id):
        return Suggester(**SuggesterDA.get_suggester_by_id(id))

    def add_preference(self, key, value):
        self.preferences[key] = value

    def update_preference(self, key, value):
        self.preferences[key] = value

    def remove_preference(self, key):
        self.preferences.pop(key)

    def get_preference(self, key):
        return self.preferences.get(key)

    def has_preference(self, key):
        return key in self.preferences

    def get_all_preferences(self):
        return self.preferences
    
    #this function gets the items that have been suggested to the suggester
    #this will take a key of albums, artists, or songs and return a list of items according
    #to what was requested
    def get_suggested_to(self, key):
        if self.suggested_to_items[key] is not None:
            return self.suggested_to_items[key]

        if key in Suggester.suggested_to_functions.keys():
            self.suggested_to_items[key] = Suggester.suggested_to_functions[key](self.id)
            return self.suggested_to_items[key]
        
        else:
            raise ValueError(f"Invalid key: {key}")

    #this function gets the items that have suggested by the suggester
    #this will take a key of albums, artists, or songs and return a list of items according
    #to what was requested
    def get_suggested_by(self, key):
        if self.suggested_by_items[key] is not None:
            return self.suggested_by_items[key]

        if key in Suggester.suggested_by_functions.keys():
            self.suggested_by_items[key] = Suggester.suggested_by_functions[key](self.id)
            return self.suggested_by_items[key]

        raise ValueError(f"Invalid key: {key}") #if key didnt match 

    
    def __str__(self):
        return f"Name: {self.name}, contact_info: {self.contact_info}, Preferences: {self.preferences}"
