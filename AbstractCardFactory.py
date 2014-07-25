from AbstractCard import AbstractCard

class AbstractCardFactory:
    """Factory for making AbstractCards"""

    def __init__(self, values=None, suits=None, rank_generator=None):
        self.values = values
        self.suits = suits
        self.rank_generator = rank_generator
        
    def __repr__(self):
        return "Values: {}\nSuits: {}".format(self.values, self.suits)
    
    def __str__(self):
        return self.__repr__()
    
    def generate(self):
        for suit in self.suits:
            for value in self.values:
                card = AbstractCard(value, suit)
                card.rank = self.rank_generator.rank_card(card)
                yield card
    
    
