"""
suggesters.py: This file contains the suggesters class.
"""

__author__ = "Michael Dormon"

from dataclasses import field, dataclass

from data_access.suggester_da import AuthenticationError, SuggesterDA




@dataclass
class Suggester(object):
    """This is a class that holds information about a suggester.

    Information about the suggester includes name, email and some prefferences.
    Also, there are dictionaries that hold the suggested items to and by the suggester
    that are used to cache results only after they are requested.
    """
    id : int
    name: str
    email : str
    wants_suggestions : bool = True
    suggested_to_items : dict = field(default_factory=dict)
    suggested_by_items : dict = field(default_factory=dict)


    @staticmethod
    def from_id(id):
        sug = SuggesterDA.get_suggester_by_id(id)
        return Suggester( sug['id'], sug['name'], sug['email'], sug['wants_suggestions'])

    @staticmethod
    def try_login(email, password):
        try:
            sug = SuggesterDA.try_login(email, password)
        except AuthenticationError:
            return None
        return Suggester(sug['id'], sug['name'], sug['email'], sug['wants_suggestions'])


    # bad old dead code, probably will be removed soon

    # #this function gets the items that have been suggested to the suggester
    # #this will take a key of albums, artists, or songs and return a list of items according
    # #to what was requested
    # def get_suggested_to(self, key):
    #     if self.suggested_to_items[key] is not None:
    #         return self.suggested_to_items[key]

    #     if key in Suggester.suggested_to_functions.keys():
    #         self.suggested_to_items[key] = Suggester.suggested_to_functions[key](self.id)
    #         return self.suggested_to_items[key]
        
    #     else:
    #         raise ValueError(f"Invalid key: {key}")

    # #this function gets the items that have suggested by the suggester
    # #this will take a key of albums, artists, or songs and return a list of items according
    # #to what was requested
    # def get_suggested_by(self, key):
    #     if self.suggested_by_items[key] is not None:
    #         return self.suggested_by_items[key]

    #     if key in Suggester.suggested_by_functions.keys():
    #         self.suggested_by_items[key] = Suggester.suggested_by_functions[key](self.id)
    #         return self.suggested_by_items[key]

    #     raise ValueError(f"Invalid key: {key}") #if key didnt match 

    
    # def __str__(self):
    #     return f"Name: {self.name}, contact_info: {self.contact_info}, Preferences: {self.preferences}"
