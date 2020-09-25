class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
    
    # Remove card from 
    def remove_one(self):
        return self.all_cards.pop(0)

    # Add new cards into player's list
    def add_cards(self, new_cards):
        self.all_cards.extend(new_cards)
    

    


