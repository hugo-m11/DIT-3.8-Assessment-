from tkinter import*
from tkinter.scrolledtext import*
import card

class Mainloop:
    def __init__ (self, parent):
        self.rule_screen_frame = Frame(parent)
        self.main_frame = Frame(parent)
        self.game_frame = Frame(parent)

        self.players = []
        self.current_players = 0

        

        self.title_label = Label(self.main_frame, text="| Sabacc |", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, pady=10)

        self.rules_button = Button(self.main_frame,text="| See Rules |", command=lambda: self.switch_frame_rule(self.rule_screen_frame))
        self.rules_button.grid(row=1, column=0, pady=5)

        self.rule_screen_title = Label(self.rule_screen_frame, text="| Rules |", font=("Arial", 16))
        self.rule_screen_title.grid(row=0, column=0)

        self.exit_to_main_frame_button = Button(self.rule_screen_frame,text="| Back |", command=lambda: self.switch_frame_rule(self.main_frame))
        self.exit_to_main_frame_button.grid(row=1, column=0)

        self.display_rules = ScrolledText(self.rule_screen_frame, width = 60, height = 20, state = 'disabled', wrap = 'word')
        self.display_rules.grid(row = 6, columnspan = 2)

        self.new_game_button = Button(self.main_frame, text = "| Start Game |", command=self.start_game)
        self.new_game_button.grid(row=2, column=0, pady=5)

        self.player_label = Label(self.game_frame, text="", font=("Arial", 16))
        self.player_label.grid(row=0, column=0, pady=10)

        self.hand_label = Label(self.game_frame, text="", font=("Arial", 12))
        self.hand_label.grid(row=1, column=0, pady=10)

        self.draw_card_button = Button(self.game_frame, text="Draw Card", command=card.draw_card)
        self.draw_card_button.grid(row=2, column=0)
        
        self.end_turn_button = Button(self.game_frame, text="End Turn", command=self.next_player)
        self.end_turn_button.grid(row=3, column=0)

        self.display_rules.configure(state = 'normal')
        self.display_rules.insert(END, """Step 1:
Choose a dealer. The person to the right of the dealer puts a blind into the hand pot. (In a two player game this would always be the dealer.) The blind is a previously agreed upon amount which must be paid at the start of each hand. The dealer rotates to the player on the left at the end of each round. The purpose of the blind is to ensure that there is always something to win in the hand pot, even if nobody bets.
—-----------------------------------------------------------------------------------------------------------------------
Step 2:
The dealer deals two cards to each player.
—-----------------------------------------------------------------------------------------------------------------------
Step 3:
After the cards are dealt, you begin the betting round of the hand. Each player, starting with the player to the left of the dealer and continuing clockwise takes turns to Bet, Call, Check, Raise, or Fold their hand much like in Poker:
                                  
Bet, If no one has yet placed a starting bet you may call bet and place an amount of Credits in front of you (septet from both your stash of credits and the pots for easy counting.)
                                  
Call, You may call to equal the highest bet.
                                  
Check, If no one has yet placed the starting bet or if your current bet is equal to the highest bet you may call check. (When checking, a player declines to make a bet, but wishes to keep their cards and continue playing.
                                  
Raise, if a player raises they're matching and increasing the current bet. (If a player raises the other players will continue around the table and choose to either call, check the new bet or fold.
                                  
Fold, If a player folds they believe there is no chance of winning and forfeit the hand. (they must discard their cards facedown and anything they had bet goes into the hand pot.)
                                  
The betting round continues until all the remaining players have checked or when all the bets are the same.
(If a player can't fold or check they are forced to fold or “go all in.” [see the all in rules below.])
—-----------------------------------------------------------------------------------------------------------------------
Step 4:
The next step is the trading ground. Each player takes turns choosing one or more of the following:
Drawing a card from the top of the deck.
                                  
Trade out one card (discard a card then draw the top card.)
                                  
Do nothing (stand.)
                                  
Alderaan (calling the game.)
                                  
(By calling Alderaan you think you have the hand closest to -23 or 23 all players who haven't finished the trading round may do so then cards are revealed and you move to the Show Down phase.)
—-----------------------------------------------------------------------------------------------------------------------
Step 5:
The final step is the dice round. The dealer roles two dice, if those dice land on different symbols/numbers then nothing happens. If both dice land on the same symbol/number “the shift“ commences. All players' cards are re-shuffle into the deck along with the discard pile. Each player is then dealt the same amount of cards they had before “The Shift”.
(These steps are repeated in order over & over until someone calls Alderaan during the trading round [step number 4.])
The Show Down
                                  
All players reveal their hands. The winner is the person with the closest hand to 23 or -23. Negatives beat positive (-22 would beat 22 etc.) The winner of the hand claims the hand pot. If the winner had a True Sabacc (a perfect 23 or -23) then they would also claim the Sabacc pot.
If a player's final hand is 0, more than 23, or less then -23 they “`bomb out“ they must calculate what 10% of the hand pot would be then they pay that amount from their own stash into the Sabacc pot.)
—-----------------------------------------------------------------------------------------------------------------------
""" + "\n")
        self.display_rules.configure(state = 'disabled')


        # Start on main menu
        self.switch_frame_rule(self.main_frame)
       
    def switch_frame_rule(self, frame):
        self.main_frame.grid_forget()
        self.rule_screen_frame.grid_forget()
        frame.grid()

    def start_game(self):
        self.players = card.create_players(4)
        card.deal_starting_hands(self.players)
        self.current_player = 0
        self.update_player_display()
        self.switch_frame_rule(self.game_frame)

    def update_player_display(self):

        player = self.players[self.current_player]

        self.player_label.config(text=f"{player.name}'s Turn" )
        hand_text = ""
        
        for card in player.hand:
            hand_text += str(card) + "\n"

        self.hand_label.config(text=hand_text)

    def next_player(self):

        self.current_player += 1

        if self.current_player >= len(self.players):
            self.current_player = 0

        self.update_player_display()




    
if __name__ == "__main__":

    root = Tk()
    gui = Mainloop(root)
    root.title("Sabbac")
    root.mainloop()