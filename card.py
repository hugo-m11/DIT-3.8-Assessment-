from tkinter import*

class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.name
    

deck = []

suits = ["Flask", "Saber", "Stave", "Coin"]

for suit in suits:
    for num in range(1, 12):
        deck.append(Card(f"{num} of {suit}", num, suit))

    deck.append(Card(f"{suit} Commander", 12, suit))
    deck.append(Card(f"{suit} Mistress", 13, suit))
    deck.append(Card(f"{suit} Master", 14, suit))
    deck.append(Card(f"Ace of {suit}", 15, suit))
    deck.append(Card("Balance", -11, "Special"))
    deck.append(Card("Demise", -13, "Special"))