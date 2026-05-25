from tkinter import*
import random

class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.name
        
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self):
        card = draw_card()
        if card:
            self.hand.append(card)

    def show_hand(self):
        for card in self.hand:
            print(card)

deck = []


suits = ["Flask", "Saber", "Stave", "Coin"]

for suit in suits:
    for num in range(1, 12):
# normal cards
        deck.append(Card(f"{num} of {suit}", num, suit))
# face cards 
    deck.append(Card(f"{suit} Commander", 12, suit))
    deck.append(Card(f"{suit} Mistress", 13, suit))
    deck.append(Card(f"{suit} Master", 14, suit))
    deck.append(Card(f"Ace of {suit}", 15, suit))


special_cards = [
    ("Balance", -11),
    ("Idiot", 0),
    ("Endurance", -8),
    ("Moderation", -14),
    ("Evil One", -15),
    ("Queen of Air and Darkness", -2),
    ("Demise", -13),
    ("Star", -17)
]

# adds two copies of each special card
for name, value in special_cards:
    for i in range(2):
        deck.append(Card(name, value, "Special"))

    
def shuffle_deck():
    random.shuffle(deck)


def draw_card():
    if len(deck) > 0:
        return deck.pop()
    return None

    




    

    