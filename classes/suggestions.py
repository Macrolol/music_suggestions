from abc import abstractmethod, ABC
from dataclasses import dataclass
from classes.data_access.suggester_da import SuggesterDA

from data_access.suggestion_da import (get_songs_suggested_to,
                  get_songs_suggested_by,
                  get_albums_suggested_by,
                  get_albums_suggested_to,
                  get_artists_suggested_by,
                  get_artists_suggested_to)


class Suggestion(ABC):
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

    @staticmethod
    def from_id(id):
        pass
    
    @abstractmethod
    @staticmethod
    def suggested_to(self, suggestee_id, limit=10):
        pass

    @abstractmethod
    @staticmethod
    def suggested_by(self, suggestee_id, limit=10):
        pass


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

    @staticmethod
    def suggested_to(suggestee_id, limit=10):
        return get_songs_suggested_to(suggestee_id, limit)
        
    @staticmethod
    def suggested_by(suggestee_id, limit=10):
        return get_songs_suggested_by(suggestee_id, limit)

@dataclass
class Album(Suggestion):
    """this is a class to hold data about albums
    it has properties title, artist, songs, and rating"""
    title: str
    artist: str
    songs: list
    
    def __repr__(self):
        return f'{self.title} by {self.artist}'

    @staticmethod
    def suggested_to(suggestee_id, limit=10):
        return get_albums_suggested_to(suggestee_id, limit)

    @staticmethod
    def suggested_by(suggestee_id, limit=10):
        return get_albums_suggested_by(suggestee_id, limit)
    
    
    
@dataclass
class Artist(Suggestion):
    """this is a class to hold data about artists
    it has properties name, albums, and rating"""
    name: str
    albums: list
    
    def __repr__(self):
        return f'{self.name}'

    @staticmethod
    def suggested_to(suggestee_id, limit=10):
        return get_artists_suggested_to(suggestee_id, limit)
    
    @staticmethod
    def suggested_by(suggestee_id, limit=10):
        return get_artists_suggested_by(suggestee_id, limit)
    


if __name__ == "__main__":
    pass