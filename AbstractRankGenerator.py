from AbstractCard import AbstractCard

class AbstractRankGenerator:
    """Generator for rankings"""
    
    def rank_card(card):
        raise NotImplementedError("Override this method to rank cards")
    
    
    
