import random
from card_setting import *
from card import Card
class Deck:
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal(self):
        for card in self.all_cards:
            print(card)
    
    def deal_one(self):
        return self.all_cards.pop()

new_deck = Deck()