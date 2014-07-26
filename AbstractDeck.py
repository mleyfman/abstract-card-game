from random import *

class AbstractDeck:
    """Abstract class for shuffling and iterating over a collection of cards"""

    def __init__(self, cards=None):
        self.cards = cards

    def __len__(self):
        return len(cards)

    def __iter__(self):
        return iter(self.cards)

    def shuffle(self):
        """Shuffles the deck with the Fisher-Yates shuffle"""
        num_cards = len(self.cards)
        for i in range(0, num_cards):
            
            j = randint(i, num_cards - 1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    
