"""
suggester_da.py: This file holds the SuggesterDA class. The SuggesterDA class
is responsible for handling all data access for the Suggester class.

The AuthenticationError class is also defined here as it is only raised in the SuggesterDA class.
"""

__author__ = "Michael Dormon"


from psycopg2.errors import UniqueViolation


from data_access.postgres_connection import connect, PostgresConnectionError
from data_access.security.hashing import Hashing
from data_access.da_exceptions import NotFoundError, DuplicateError, DatabaseConnectionError, UnexpectedDatabaseError

class AuthenticationError(Exception):
    """
    Exception raised by the try_login method when username and password given do
    not match the username and password combination in the database.
    """
    pass


class SuggesterDA:
    """
    Data access object for the Suggester class.

    Each method raises a DatabaseConnectionError if the database connection
    fails.
    """

    @staticmethod
    def get_suggester(suggester_id):
        '''
        This function returns the suggester's details from the database based on an id.

        If the suggester does not exist, a NotFoundError is raised.
        If the suggester is successfully retrieved, the function returns the suggester's details in a dictionary.
        '''
        result =  None
        try:
            with connect() as conn:
                cur = conn.cursor()
                cur.execute("SELECT suggester_id as id, suggester_name as name, suggester_email as email, suggester_password as password, suggester_wants_suggestions as wants_suggestions FROM suggester WHERE suggester_id = %s", str(suggester_id))
                result = cur.fetchone()
                print(result) #debug
        except PostgresConnectionError as e:
            print("Error: {}".format(e)) #debug
            raise DatabaseConnectionError("Error connecting to the database.")
        
        if result is None:
            raise NotFoundError("Suggester not found.")

        return result

    @staticmethod
    def try_login(suggester_email, suggester_password):
        """
        This method uses the suggester's email and password to try to log in.

        If the email and password match the username and password in the database,
        the suggester's details are returned in a dictionary.
        
        Otherwise, an AuthenticationError is raised.

        If the email does not exist a not found error is raised.
        """
        result = None
        try:
            with connect() as conn:
                cur = conn.cursor()
                cur.execute("SELECT try_login(%s, %s)", (suggester_email, suggester_password))
                result = cur.fetchone()
                print(result) #debug              
        except PostgresConnectionError as e:
            print("Error: {}".format(e)) #debug
            raise DatabaseConnectionError("Error connecting to database.", orig=e)
        
        if result is None:
            raise NotFoundError("Suggester not found.")

        if Hashing.verify(suggester_password, result['password']):
            return result

        raise AuthenticationError("Incorrect password.")

    @staticmethod
    def update_suggester(suggester):
        """
        This function updates the suggester's name and contact info

        If the suggester does not exist, a NotFoundError is raised.
        """
        result = None
        try:
            with connect() as conn:
                cur = conn.cursor()
                effected_rows = cur.execute("UPDATE suggester SET suggester_name = %s, suggester_email = %s WHERE suggester_id = %s", (suggester.name, suggester.email, suggester.id))
                print(result) #debug
        except PostgresConnectionError as e:
            print("Error: {}".format(e))
            raise DatabaseConnectionError("Error connecting to database.", orig=e)

        if effected_rows == 0:
            raise NotFoundError("Suggester not found.")

        return result

    @staticmethod
    def create_suggester(suggester):
        """
        This method adds a new suggester to the database if one of the same name does not already exist.

        If the suggester already exists, a DuplicateError is raised.
        This method returns the id of the new suggester.
        """
        result = None
        try:
            with connect() as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO suggester (suggester_name, suggester_email, suggester_password) VALUES (%s, %s, %s) RETURNING suggester_id", (suggester.name, suggester.email, suggester.password))
                result = cur.fetchone()
                print(result) #debug
        except PostgresConnectionError as e:
            print("Error: {}".format(e)) #debug
            raise DatabaseConnectionError("Error connecting to database.", orig=e)

        except UniqueViolation as e: # type: ignore  #idk why pylance is complaining
            print("Error: {}".format(e)) #debug
            print(type(e)) #debug
            raise DuplicateError("Suggester already exists.", e)

        if result is None:
            raise UnexpectedDatabaseError("Unexpected error, something is very wrong.")

        return result['suggester_id']

if __name__ == "__main__":
    """
    This main method is currently only used for testing
    """
    from dataclasses import dataclass

    @dataclass # define a simple suggester class for testing
    class Suggester(object):
        """This is a class that holds information about a suggester.

        Information about the suggester includes name, email and some prefferences.
        Also, there are dictionaries that hold the suggested items to and by the suggester
        that are used to cache results only after they are requested.
        """
        name: str
        email : str
        password : str

    suggester = Suggester("Michael", "email@email.com", "password")
    returned_value = SuggesterDA.create_suggester(suggester)