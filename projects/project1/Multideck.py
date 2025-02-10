import random 
from Card import Card
import copy
class Multideck:
    def __init__(self, num_decks):
        self.num_decks = num_decks
        self.multideck = self.create_deck()
        self.shuffle()
    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        single_deck = [Card(suit,rank) for suit in suits for rank in ranks]
        all_decks = []
        for i in range(self.num_decks):
            all_decks.append(copy.deepcopy(single_deck))
        return all_decks
    def shuffle(self):
        for deck in self.multideck:
            random.shuffle(deck)
    def deal_card(self):
        deck_num = random.randint(0,self.num_decks-1)
        return self.multideck[deck_num].pop()
        