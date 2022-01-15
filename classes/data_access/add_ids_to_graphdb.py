from neo4j_connection import get_session
from postgres_connection import connect, PostgresConnectionError
from da_exceptions import DatabaseConnectionError

def get_ids_and_tags():
    ids_and_tags = []
    try:
        with connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT suggester_id AS id, suggester_tag AS tag FROM suggester_tags_view")
            ids_and_tags = [ dict(row) for row in cur.fetchall() ]
    except PostgresConnectionError as e:
        print("Error: {}".format(e)) #debug
        raise DatabaseConnectionError("Error connecting to the database.")
    return ids_and_tags

def create_cypher_string(ids_and_tags):
    cypher_string = "CREATE "
    for id_and_tag in ids_and_tags:
        cypher_string += "(:Suggester{{id: {}, tag: '{}' }}), ".format(id_and_tag['id'], id_and_tag['tag'])
    cypher_string = cypher_string[:-2]
    return cypher_string


def add_ids_to_graphdb(ids_and_tags):
    cypher_string = create_cypher_string(ids_and_tags)
    # print("cypher_string: {}".format(cypher_string)) #debug
    try:
        with get_session() as session:
            result = session.run(cypher_string)
            return result
    except Exception as e:
        # print("Error: {}".format(e)) #debug
        raise DatabaseConnectionError("Error connecting to the database.")


if __name__ == "__main__":
    ids_and_tags = get_ids_and_tags()
    result = add_ids_to_graphdb(ids_and_tags)
    print("result: {}".format(result)) #debug
