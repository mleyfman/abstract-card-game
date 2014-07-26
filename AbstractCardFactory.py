from AbstractCard import AbstractCard

class AbstractCardFactory:
    """Factory for making AbstractCards"""

    def __init__(self, values=None, suits=None, rank_function=None):
        self.values = values
        self.suits = suits
        self.rank_function = rank_function
        
    def __repr__(self):
        return "Values: {}\nSuits: {}".format(self.values, self.suits)
    
    def __str__(self):
        return self.__repr__()

    def generate(self):
        if self.rank_function:
            for suit in self.suits:
                for value in self.values:
                    card = AbstractCard(value, suit)
                    card.rank = rank_function(card)
                    yield card
        else:
            for suit in self.suits:
                for value in self.values:
                    yield AbstractCard(value, suit)
    
    
