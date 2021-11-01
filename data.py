from dataclasses import dataclass

from firestore_connection import add_song


class Suggestion(object):
    def __init__(self, refferer = "anonymous"):
        self.refferers = [ refferer ] #start a list of people that have reffered this
        self.rating = None
        self.listened = False

    def add_refferer(self, refferer):
        self.refferers.append(refferer)
    
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
        super().__init__(refferer=refferer)
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
    