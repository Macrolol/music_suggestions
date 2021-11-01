from dataclasses import dataclass

from postgres_connection import (get_songs_suggested_to,
                                 get_songs_suggested_by,
                                 get_albums_suggested_by,
                                 get_albums_suggested_to,
                                 get_artists_suggested_by,
                                 get_artists_suggested_to)

@dataclass
class Suggester(object):
    """This isa a classs that holds information about
    a suggester, including name, email address, and user prefferences"""
    id : int
    name: str
    email: str
    preferences: dict
    suggested_to_items : dict
    suggested_by_items : dict
    def __init__(self, name, email, preferences=None):
        self.name = name
        self.email = email
        self.preferences = {} if preferences is None else preferences

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

        if key == "albums":
            self.suggested_to_items[key] = get_albums_suggested_to(self.id)
            return self.suggested_to_items[key]
        elif key == "artists":
            self.suggested_to_items[key] = get_artists_suggested_to(self.id)
            return self.suggested_to_items[key]
        elif key == "songs":
            self.suggested_to_items[key] = get_songs_suggested_to(self.id)
            return self.suggested_to_items[key]
        else:
            raise ValueError(f"Invalid key: {key}")

    #this function gets the items that have suggested by the suggester
    #this will take a key of albums, artists, or songs and return a list of items according
    #to what was requested
    def get_suggested_by(self, key):
        if self.suggested_by_items[key] is not None:
            return self.suggested_by_items[key]

        if key == "albums":
            self.suggested_by_items[key] = get_albums_suggested_by(self.id)
            return self.suggested_by_items[key]
        elif key == "artists":
            self.suggested_by_items[key] = get_artists_suggested_by(self.id)
            return self.suggested_by_items[key]
        elif key == "songs":
            self.suggested_by_items[key] = get_songs_suggested_by(self.id)
            return self.suggested_by_items[key]
        else:
            raise ValueError(f"Invalid key: {key}")

    
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Preferences: {self.preferences}"

    


class Suggestion(object):
    def __init__(self, suggester = "anonymous"):
        self.suggesters = [ suggester ] #start a list of people that have suggested this
        self.rating = None
        self.listened = False

    def add_refferer(self, refferer):
        self.suggesters.append(refferer)
    
    def listen(self):
        self.listened = True
    
    def rate(self, rating):
        self.rating = rating






@dataclass
class Song(Suggestion):
    """this is a class to hold data about song suggestions
     it has properties title, artist, album, listened, and rating"""
    title: str
    artist: str
    album: str
    
    def __repr__(self):
        return f'{self.title} by {self.artist}'

    def __init__(self, refferer="anonymous", title="", artist="", album=""):
        super().__init__(suggester=refferer)
        self.listened = False
        self.rating = None
        self.title = title
        self.artist = artist
        self.album = album
        

@dataclass
class Album(Suggestion):
    """this is a class to hold data about albums
    it has properties title, artist, songs, and rating"""
    title: str
    artist: str
    songs: list
    
    def __repr__(self):
        return f'{self.title} by {self.artist}'
    
    
    
@dataclass
class Artist(Suggestion):
    """this is a class to hold data about artists
    it has properties name, albums, and rating"""
    name: str
    albums: list
    
    def __repr__(self):
        return f'{self.name}'
    


if __name__ == "__main__":
    # test code
    # create a song
    song = Song(refferer="me")
    print(vars(song))
    