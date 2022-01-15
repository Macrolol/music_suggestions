import re
from neo4j_connection import get_session
from da_exceptions import DatabaseConnectionError, NotFoundError, UnexpectedDatabaseError

class SuggesterManagerDA:


    # returns a list of dicts with keys 'id' and 'tag'
    @staticmethod
    def get_friends_of(suggester_id):
        cypher_string = "MATCH (s:Suggester {{id: {}}})-[:FRIEND]->(f:Suggester)" \
                        "RETURN f.id AS id, f.tag AS tag".format(suggester_id)
        # print("cypher_string: {}".format(cypher_string)) # debug
        try:
            with get_session() as session:
                result = session.run(cypher_string)
                record = result.values()
                return record
        except Exception as e:
            print("Error: {}".format(e)) #debug




    # adds a friend relationship between two suggesters
    @staticmethod
    def add_friend(suggester_id, friend_id):
        cypher_string = "MATCH (s:Suggester {{id: {}}}), (f:Suggester {{id: {}}})" \
                        "CREATE (s)-[r:FRIEND]->(f)" \
                        "RETURN s,r,f".format(suggester_id, friend_id)
        # print("cypher_string: {}".format(cypher_string)) # debug
        try:
            with get_session() as session:
                result = session.run(cypher_string)
                record = result.single()
                if record['r'] is None:
                    raise UnexpectedDatabaseError("Friend not created.")
                return record['s']['id'], record['f']['id']
        except Exception as e:
            print("Error: {}".format(e))
    
    # removes a friend relationship between two suggesters
    @staticmethod
    def remove_friend(suggester_id, friend_id):
        cypher_string = "MATCH (s:Suggester {{id: {}}})-[r:FRIEND]->(f:Suggester {{id: {}}})" \
                        "DELETE r".format(suggester_id, friend_id)
        # print("cypher_string: {}".format(cypher_string)) # debug
        try:
            with get_session() as session:
                result = session.run(cypher_string)
                return result
        except Exception as e:
            print("Error: {}".format(e))
            raise DatabaseConnectionError("Error connecting to the database.")
    