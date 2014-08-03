class AbstractGame:
    """Abstract class for running a card game"""

    def __init__(self, players=[], deck=None):
        self.players = list(players)
        self.deck = deck

    def play_game(self):
        """Override this function for custom game logic"""
        pass

    

