class AbstractPlayer:
    """Abstract class for containing basic player information"""

    def __init__(self, name=None, cards=[]):
        self.name = name
        self.cards = list(cards)

    def name(self):
        return self.name

    def hand(self):
        """Returns a copy of the player's hand"""
        return self.cards

    def add_card(self, card):
        """Adds the given card to the existing cards"""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes the given card from the player's hand"""
        self.cards.remove(card)

    def __repr__(self):
        return self.name

    def __str__(self):
        return str(self.name)
