"""
suggesters.py: This file contains the suggesters class.
"""

__author__ = "Michael Dormon"

from dataclasses import field, dataclass

try:
    from classes.data_access.suggester_da import AuthenticationError, SuggesterDA, DuplicateError
except ModuleNotFoundError as e:
    from data_access.suggester_da import AuthenticationError, SuggesterDA, DuplicateError




@dataclass
class Suggester(object):
    """This is a class that holds information about a suggester.

    Information about the suggester includes name, email and some prefferences.
    
    """
    id : int
    tag: str
    email : str
    wants_suggestions : bool = True
    wants_feedback : bool = True


    @staticmethod
    def from_id(id):
        sug = SuggesterDA.get_suggester_by_id(id)
        return Suggester( sug['id'], sug['tag'], sug['email'], sug['wants_suggestions'], sug['wants_feedback'] )


    # this method is called when a suggeseter is attempting to login
    # it returns a suggester object if the login is successful.
    # it returns false if the login is unsuccessful.
    @staticmethod
    def try_login(email, password):
        try:
            sug = SuggesterDA.try_login(email, password)
            return Suggester( sug['id'], sug['tag'], sug['email'], sug['wants_suggestions'], sug['wants_feedback'] )
        except AuthenticationError:
            return False 


    # this method is called when a suggeseter is attempting to register
    # it returns a suggester id if successful.
    # otherwise it returns false.
    @staticmethod
    def try_register(email, password, username):
        try:
            id = SuggesterDA.create_suggester(email, password, username) 
            return id
        except DuplicateError:
            return False 

