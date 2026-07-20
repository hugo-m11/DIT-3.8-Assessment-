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
        self.credits = 100
        self.current_bet = 0
        self.has_folded = False

    def draw(self):
        card = draw_card()
        if card:
            self.hand.append(card)

    def clear_hand(self):
        # Move all cards to the discard pile instead of just deleting them
        global discarded_cards 
        discarded_cards.extend(self.hand)
        self.hand.clear()

    def get_hand_value(self):
        return sum(card.value for card in self.hand)
    
    def discard(self, card_index):
        if 0 <= card_index < len(self.hand):
            discarded_card = self.hand.pop(card_index)
            discarded_cards.append(discarded_card)


deck = []
discarded_cards = []

suits = ["Flask", "Saber", "Stave", "Coin"]

for suit in suits:

    for num in range(1, 12):
        deck.append(Card(f"{num} of {suit} | ({num})", num, suit))
    deck.append(Card(f"Commander of {suit} | (12)", 12, suit))
    deck.append(Card(f"Mistress of {suit} | (13)", 13, suit))
    deck.append(Card(f"Master of {suit} | (14)", 14, suit))
    deck.append(Card(f"Ace of {suit} | (15)", 15, suit))


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

for name, value in special_cards:
    for _ in range(2):
        deck.append(Card(name, value, "Special"))


def shuffle_deck():
    random.shuffle(deck)


def draw_card():
    if len(deck) > 0:
        return deck.pop()
    return None


def create_players(num_players):

    players = []

    for i in range(num_players):
        players.append(Player(f"Player {i+1}"))

    return players


def deal_starting_hands(players):

    shuffle_deck()

    for player in players:
        player.draw()
        player.draw()




    

    