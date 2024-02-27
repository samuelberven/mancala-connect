class Player:
    """Takes player name as a parameter and creates object representing player.
    Also initializes pit and store data members"""
    def __init__(self, player_name, offset):
        self._name = player_name
        self._pits_and_store = [4, 4, 4, 4, 4, 4, 0]
        self._offset = offset

    def get_name(self):
        """
        Returns Player name
        """
        return self._name

    def get_offset(self):
        """
        Returns Player pits and store as a single list
        """
        return self._offset

    def get_pits_and_store(self):
        """
        Returns Player pits and store as a single list
        """
        return self._pits_and_store

    def set_pits_and_store(self, string): # NOTE "string" is probably not an accurate word here
        """
        Sets Player pits and store to values in given list (containing six pits first and then the store)
        """
        self._pits_and_store = string

    def get_store(self):
        """
        """
        return self._pits_and_store[6]

    def get_pits(self):
        """
        Returns Player pit
        """
        return self._pits_and_store[0:6:]
    