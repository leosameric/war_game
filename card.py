from card_setting import *
# Card Class
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    # print card value
    def __str__(self):
        return self.rank + " Of " + self.suit
    
# card1 = Card("Diamont", "Three")
# print(card1)