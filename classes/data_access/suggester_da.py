from data_access.postgres_connection import connect, PostgresConnectionError


class SuggesterDA:

    @staticmethod
    def get_suggester(suggester_id):
        '''
        This function returns the suggester's name
        '''
        result =  None
        try:
            with connect() as conn:
                cur = conn.cursor()
                cur.execute("SELECT suggester_id as id, suggester_name as name, suggester_contact as contact_info FROM suggester WHERE suggester_id = %s", str(suggester_id))
                result = cur.fetchone()
                print(result) #debug
        except PostgresConnectionError as e:
            print("Error: {}".format(e)) #debug

        return result

    @staticmethod
    def update_suggester(suggester):
        '''
        This function updates the suggester's name and contact info
        '''
        result = None
        try:
            with connect() as conn:
                cur = conn.cursor()
                cur.execute("UPDATE suggester SET suggester_name = %s, suggester_contact = %s WHERE suggester_id = %s", (suggester.name, suggester.contact_info, suggester.id))
                result = cur.fetchone()
                print(result) #debug
        except PostgresConnectionError as e:
            print("Error: {}".format(e))