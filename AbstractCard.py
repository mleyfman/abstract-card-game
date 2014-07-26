class AbstractCard:
    """Abstract class for handling comparisons between cards based on rank"""

    def __init__(self, value=None, suit=None, rank=None):
        self.value = value
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        if isinstance(other, AbstractCard):
            return self.rank < other.rank
        raise TypeError("Cannot compare to non-card types")

    def __le__(self, other):
        if isinstance(other, AbstractCard):
            return self.rank <= other.rank
        raise TypeError("Cannot compare to non-card types")

    def __eq__(self, other):
        if isinstance(other, AbstractCard):
            return self.rank == other.rank
        raise TypeError("Cannot compare to non-card types")

    def __ne__(self, other):
        if isinstance(other, AbstractCard):
            return self.rank != other.rank
        raise TypeError("Cannot compare to non-card types")

    def __gt__(self, other):
        if isinstance(other, AbstractCard):
            return self.rank > other.rank
        raise TypeError("Cannot compare to non-card types")

    def __ge__(self, other):
        if isinstance(other, AbstractCard):
            return self.rank >= other.rank
        raise TypeError("Cannot compare to non-card types")

    def __repr__(self):
        data = (self.value, self.suit, self.rank)
        return "(value:{}, suit:{}, rank:{})".format(*data)

    def __str__(self):
        data = (self.value, self.suit)
        return "{} of {}".format(*data)
