from neo4j import Driver, GraphDatabase
import os
import atexit

uri = os.environ['NEO4J_URI']
user = os.environ['NEO4J_USER']
password = os.environ['NEO4J_PASSWORD']

print("uri: {}".format(uri))
print("user: {}".format(user))
print("password: {}".format(password))

class Neo4jConnectionError(Exception):
    """
    Error raised when there is a problem connecting to the database.
    """
    pass

class Neo4jConnection:
    
    driver = None 
    
    def __init__(self):
        if Neo4jConnection.driver is None:
            Neo4jConnection.driver = GraphDatabase.driver(uri, auth=(user, password), connection_timeout=10)
            atexit.register(Neo4jConnection.close)
        self.driver = Neo4jConnection.driver

    @staticmethod
    def get_session(): 
        conn = Neo4jConnection()
        return conn.driver.session()

    @staticmethod
    def close():
        Neo4jConnection.driver.close()
        Neo4jConnection.driver = None


get_session = Neo4jConnection.get_session 



