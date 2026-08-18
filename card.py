import random

class Card:
    #set ups up a card, assigning it a name, value and suit from the loop below
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

    #makes sure that the object displayed is legible 
    def __str__(self):
        return self.name

class Player:
    #sets up indiviudial platers with a name, a hand, amount of money, how much theyve, bet, and if theyve folded 
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.credits = 100
        self.current_bet = 0
        self.has_folded = False

    #takes a card from the deck and add it to the player's hand
    def draw(self):
        card = draw_card()
        #makes sure the deck wasn't empty
        if card:
            self.hand.append(card)

    #method for when a player folds or discards 
    def clear_hand(self):
        global discarded_cards 
        #adds all the cards to the discard pile
        discarded_cards.extend(self.hand)
        #empties a players hand 
        self.hand.clear()

    #loops through all the cards in the platers hand and adds them up
    def get_hand_value(self):
        return sum(card.value for card in self.hand)
    
    #method for discarding cards out of a players hand 
    def discard(self, card_index):
        #checks to make sure if the index actually exists in the players hand and removes it from the hand and adds its to the discards pile
        if 0 <= card_index < len(self.hand):
            discarded_card = self.hand.pop(card_index)
            discarded_cards.append(discarded_card)

#list of all the cards 
deck = []
#list of all the discarded cards 
discarded_cards = []

#suits of the cards 
suits = ["Flask", "Saber", "Stave", "Coin"]

#loops through each of the available suits and creates the cards 1-11, and the face cards
for suit in suits:

    for num in range(1, 12):
        deck.append(Card(f"{num} of {suit} | ({num})", num, suit))
    deck.append(Card(f"Commander of {suit} | (12)", 12, suit))
    deck.append(Card(f"Mistress of {suit} | (13)", 13, suit))
    deck.append(Card(f"Master of {suit} | (14)", 14, suit))
    deck.append(Card(f"Ace of {suit} | (15)", 15, suit))


#list of tuples containing the names and values of special cards
special_cards = [
    ("Balance | (-11)", -11),
    ("Idiot | (0)", 0),
    ("Endurance | (-8)", -8),
    ("Moderation | (-14)", -14),
    ("Evil One | (-15)", -15),
    ("Queen of Air and Darkness | (-2)", -2),
    ("Demise | (-13)", -13),
    ("Star | (-17)", -17)
]


#loops through the special cards and makes two of them 
for name, value in special_cards:
    for _ in range(2):
        deck.append(Card(name, value, "Special"))

#shuffles the deck
def shuffle_deck():
    random.shuffle(deck)

#takes the last off the deck and returns it 
def draw_card():
    if len(deck) > 0:
        return deck.pop()
    return None

#creates the requested numaber of players
def create_players(num_players):

    players = []

#loops however many times there are players
    for i in range(num_players):
        players.append(Player(f"Player {i+1}"))

    return players


#deals the starting hands, shuffles deck, deals two cards per player
def deal_starting_hands(players):

    shuffle_deck()

    for player in players:
        player.draw()
        player.draw()




    

    