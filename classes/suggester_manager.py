from suggesters import Suggester


class SuggesterManager(object):
    """This class is used to manage suggesters.
    
    Its main purpose is to agregate suggesters
    as well as use the SuggesterManagerDA class
    to access the graph database used to keep 
    track of suggesters friends.
    """

    def __init__(self):
        """
        This method initializes the SuggesterManager object.
        """
        self.suggesters = {}

    def add_suggester(self, suggester: Suggester):
        """
        This method adds a suggester to the SuggesterManager object.
        """
        self.suggesters[suggester.id] = suggester

    def get_suggester_by_id(self, suggester_id: int):
        """
        This method returns a suggester object from the SuggesterManager object.
        """
        return self.suggesters[suggester_id]

    def get_suggester_by_email(self, suggester_email: str):
        """
        This method returns a suggester object from the SuggesterManager object.
        """
        for suggester in self.suggesters.values():
            if suggester.email == suggester_email:
                return suggester
        return None

    def get_suggester_by_tag(self, suggester_tag: str):
        """
        This method returns a suggester object from the SuggesterManager object.
        """
        for suggester in self.suggesters.values():
            if suggester.tag == suggester_tag:
                return suggester
        return None

    def get_friends_of(self, suggester_id: int):
        """
        This method returns a list of the suggester's friends.
        """
        friends = []
        for friend_id in self.suggesters[suggester_id].friends:
            friends.append(self.suggesters[friend_id])
        return friends

    def get_suggestions_of(self, suggester_id: int):
        """
        This method returns a list of the suggester's suggestions.
        """
        suggestions = []
        for suggestion_id in self.suggesters[suggester_id].suggestions:
            suggestions.append(self.suggesters[suggestion_id])
