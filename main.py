from tkinter import*
from tkinter.scrolledtext import*
import card
from tkinter import messagebox


class Mainloop:
    def __init__ (self, parent):

        #sets up the required windows 
        self.rule_screen_frame = Frame(parent)
        self.main_frame = Frame(parent)
        self.game_frame = Frame(parent)
        self.betting_frame = Frame(self.game_frame)
        self.betting_frame.grid(row=6, column=3, pady=10)
      


        #list where the players are set 
        self.players = []

        #default value that gets changed in card.py 
        self.current_players = 0
        
        #sets the vaule of the pot (betting reward)
        self.pot = 0
        
        #bet made by player
        self.current_highest_bet = 0
        self.game_phase = "Betting"
        self.players_acted = 0 


        #title screen 
        self.title_label = Label(self.main_frame, text="| Sabacc |", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, pady=5)

        #button that takse you to the rules 
        self.rules_button = Button(self.main_frame,text="| See Rules |", command=lambda: self.switch_frame_rule(self.rule_screen_frame))
        self.rules_button.grid(row=1, column=0, pady=5)

        #title indicating that you are on the rules screen 
        self.rule_screen_title = Label(self.rule_screen_frame, text="| Rules |", font=("Arial", 16))
        self.rule_screen_title.grid(row=0, columnspan=3)

        #button that takes you back to the main screen 
        self.exit_to_main_frame_button = Button(self.rule_screen_frame,text="| Back |", command=lambda: self.switch_frame_rule(self.main_frame))
        self.exit_to_main_frame_button.grid(row=1, columnspan=3)

        #the widget that displays the rules 
        self.display_rules = ScrolledText(self.rule_screen_frame, width = 60, height = 20, state = 'disabled', wrap = 'word')
        self.display_rules.grid(row = 5, columnspan = 3, padx=30)

        #button that stars a new game 
        self.new_game_button = Button(self.main_frame, text = "| Start Game |", command=self.start_game)
        self.new_game_button.grid(row=2, column=0, pady=5)

        #sets up the screen that displays individual players 
        self.player_label = Label(self.game_frame, text="", font=("Arial", 16))
        self.player_label.grid(row=0, column=3, pady=10)

        #self.hand_label = Label(self.game_frame, text="", font=("Arial", 12))
        #self.hand_label.grid(row=1, column=0, pady=10)

        #displays the cards the player holds 
        self.hand_listbox = Listbox(self.game_frame, font=("Arial", 12), width=40, height=10)
        self.hand_listbox.grid(row=1, column=3, padx=110)

        #sets up a button for drawing cards 
        self.draw_card_button = Button(self.game_frame, text="Draw Card", command=self.player_draw_card, state="disabled")
        self.draw_card_button.grid(row=2, column=3)
        
        #sets up a button for ending turn to the next player
        self.end_turn_button = Button(self.game_frame, text="End Turn", command=self.next_player)
        self.end_turn_button.grid(row=3, column=3)

        #sets up a button for discarding of the cards 
        self.discard_button = Button(self.game_frame, text="Discard", command=self.discard_selected, state="disabled")
        self.discard_button.grid(row=4, column = 3)

        self.check_button = Button(self.betting_frame, text="Check", command=self.check)
        self.check_button.grid(row=0, column=0, padx=5)

        self.fold_button = Button(self.betting_frame, text="Fold", command=self.fold)
        self.fold_button.grid(row=0, column=1, padx=5)
        
        self.call_button = Button(self.betting_frame, text="Call", command=self.call)
        self.call_button.grid(row=0, column=2, padx=5)

        self.bet_entry = Entry(self.betting_frame, width=5)
        self.bet_entry.grid(row=0, column=3, padx=5)

        self.bet_button = Button(self.betting_frame, text="Bet/Raise", command=self.bet)
        self.bet_button.grid(row=0, column=4, padx=5)


        #what is displayed in the rules section 
        self.display_rules.configure(state = 'normal')
        self.display_rules.insert(END, """
                                  
—-----------------------------------------------------------
                                  
Step 2:
The deal two cards to each player.
                                  
—-----------------------------------------------------------
                                  
Step 3:
After the cards are dealt, you begin the betting round of the hand. Each player, starting with the player to the left of the dealer and continuing clockwise takes turns to Bet, Call, Check, Raise, or Fold their hand much like in Poker:
                                  
Bet, If no one has yet placed a starting bet you may call bet and place an amount of Credits
                                  
Call, You may call to equal the highest bet.
                                  
Check, If no one has yet placed the starting bet or if your current bet is equal to the highest bet you may call check. (When checking, a player declines to make a bet, but wishes to keep their cards and continue playing.
                                  
Fold, If a player folds they believe there is no chance of winning and forfeit the hand. (they must discard their cards facedown and anything they had bet goes into the hand pot.)
                                  
The betting round continues until all the remaining players have checked or when all the bets are the same.
(If a player can't fold or check they are forced to fold or “go all in.” [see the all in rules below.])
                                  
—---------------------------------------------------------
                                  
Step 4:
The next step is the trading ground. Each player takes turns choosing one or more of the following:
Drawing a card from the top of the deck.
                                  
Trade out one card (discard a card then draw the top card.)
                                  
Do nothing (stand.)                               
                                  
—--------------------------------------------------------
                                 
Step 5:
                                  
All players reveal their hands. The winner is the person with the closest hand to 23 or -23. Negatives beat positive (-22 would beat 22 etc.) The winner of the hand claims the hand pot. If the winner had a True Sabacc (a perfect 23 or -23) then they would also claim the Sabacc pot.
If a player's final hand is 0, more than 23, or less then -23 they “`bomb out“ 
—---------------------------------------------------------
""" + "\n")
        self.display_rules.configure(state = 'disabled')
        # Start on main menu


        self.switch_frame_rule(self.main_frame)
       
    def switch_frame_rule(self, frame):
      
        self.main_frame.place_forget()
        self.rule_screen_frame.place_forget()
        self.game_frame.place_forget()
        
        frame.place(relx=0.5, rely=0.5, anchor='center')


        #method for starting games 
    def start_game(self):
        #creates four players 
        self.players = card.create_players(4)
        #deals the starting hands 
        card.deal_starting_hands(self.players)
        self.current_player = 0
        self.update_player_display()
        self.switch_frame_rule(self.game_frame)


    def update_player_display(self):
        #gets the current player 
        player = self.players[self.current_player]

        #player varibles
        display_text = f"{player.name}'s Turn | Credits: {player.credits}\n"
        display_text += f"Pot: {self.pot} | Current Bet to Call: {self.current_highest_bet}"
        
        self.player_label.config(text=display_text)
      

        self.hand_listbox.delete(0, END)
        
        #check the players hand then add it in the listbox
        for card in player.hand:
            self.hand_listbox.insert(END, str(card))

    #calls the draw method in card.py, then disables the button after
    def player_draw_card(self):
        player = self.players[self.current_player]
        player.draw()
        self.draw_card_button.config(state='disabled')
        #updates the display
        self.update_player_display() 


    def discard_selected(self):
        #looks at the listbox and returns a tuple of what the user selected 
        selection = self.hand_listbox.curselection()
        
        if selection:
            #get the first selected index
            index_to_discard = selection[0] 
            player = self.players[self.current_player]
            
            #uses the discard method added in card.py 
            player.discard(index_to_discard) 
            
            #locks the button
            self.discard_button.config(state='disabled')
            #updates the display 
            self.update_player_display()

    def fold(self):
        player = self.players[self.current_player]
        player.has_folded = True
        #if they fold, put all of their cards in the discard pile 
        player.clear_hand() 
        
        #look the buttons so they cannot reget cards after folding 
        self.bet_button.config(state='disabled')
        self.fold_button.config(state='disabled')
        self.check_button.config(state='disabled')
        self.call_button.config(state='disabled') 
        
        #logs that a player has made a move, when all make a move betting phase ends 
        self.players_acted += 1 
        
        #checks if the phase is over, if not move to next player 
        if not self.check_betting_end():
            self.next_player()
    
    def check(self):
        player = self.players[self.current_player]


        #checks if the player bet matches the highest bet 
        if player.current_bet == self.current_highest_bet:
            self.bet_button.config(state='disabled')
            self.fold_button.config(state='disabled')
            self.check_button.config(state='disabled')
            self.call_button.config(state='disabled')
            
            #logs that a player has made a move, when all make a move betting phase ends 
            self.players_acted += 1 
            
            #checks if the phase is over, if not move to next player 
            if not self.check_betting_end():
                self.next_player()
        #pop up explaining why the user cannot check at that point in the game       
        else:
            messagebox.showinfo("", "you cannot check! You must call the highest bet or fold.")


    def next_player(self):
        # if the game state is in the trading phase, check that everyone has had a turn yet 
        if self.game_phase == "Trading":
            self.players_acted += 1
            #creates a list of players who have not folded 
            active_players = [p for p in self.players if not p.has_folded]
            
            #checks that everyone has had two turns 
            if self.players_acted >= len(active_players * 3):
                
                #
                self.check_winners()
                return

        # next players turn 
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0

        # checks to skip players that have folded 
        if self.players[self.current_player].has_folded:
            self.next_player() # recursively call to skip to the next
            return
        
        #turns on the correspondingly correct buttons for each phase 
        if self.game_phase == "Betting":
            self.bet_button.config(state='normal')
            self.fold_button.config(state='normal')
            self.check_button.config(state='normal')
            self.call_button.config(state='normal')
            self.draw_card_button.config(state='disabled')
            self.discard_button.config(state='disabled')
            
        elif self.game_phase == "Trading":
            self.draw_card_button.config(state='normal')
            self.discard_button.config(state='normal')
            self.bet_button.config(state='disabled')
            self.fold_button.config(state='disabled')
            self.check_button.config(state='disabled')
            self.call_button.config(state='disabled')
            
        self.update_player_display()

    def call(self):
            player = self.players[self.current_player]

            #calculates how much the player needs to pay to match the highest bet
            amount_to_call = self.current_highest_bet - player.current_bet

            if amount_to_call > 0:
                #check that they have enough to actually pay it 
                if player.credits >= amount_to_call:
                    #add players credits to the pot 
                    player.credits -= amount_to_call
                    self.pot += amount_to_call
                    #show that that player now has the highest bet
                    player.current_bet = self.current_highest_bet
                    
                    #lock the buttons 
                    self.bet_button.config(state='disabled')
                    self.fold_button.config(state='disabled')
                    self.check_button.config(state='disabled')
                    self.call_button.config(state='disabled')
            
                    
                   #logs that a player has made a move, when all make a move betting phase ends 
                    self.players_acted += 1 
            
                    #checks if the phase is over, if not move to next player 
                    if not self.check_betting_end():
                        self.next_player()
                    #message explaining why they cannot do what they did 
                else:
                    messagebox.showinfo("", "not enough credits to call")
            #same as above 
            else:
                messagebox.showinfo("", "there is no need to call, the bet is already matched. You can check.")
        
    def bet(self):
        player = self.players[self.current_player]

        #makes sure that the user does not type a letter when betting
        try:
            #get() pulls the string out of the entry box, int() turns it into a number.
            raise_amount = int(self.bet_entry.get())
        except ValueError:
            #closes the function if they typed a letter 
            messagebox.showinfo("", "please enter a valid whole number to bet.")
            return


        if raise_amount > 0:
            #cost = the whatever it takes to catch up plus the new raise amount
            cost_to_player = (self.current_highest_bet - player.current_bet) + raise_amount
            
            # the if and else must line up perfectly for the bet to go through 
            if player.credits >= cost_to_player:
                player.credits -= cost_to_player
                self.pot += cost_to_player
                
                # makes a new highest bet that everyone has to beat
                self.current_highest_bet += raise_amount
                player.current_bet = self.current_highest_bet
                
                #cleans the entry box 
                self.bet_entry.delete(0, 'end')
                
                # Lock buttons on a successful bet
                self.bet_button.config(state='disabled')
                self.fold_button.config(state='disabled')
                self.check_button.config(state='disabled')
                self.call_button.config(state='disabled')
                
                #the counter resets cause everyone is forced to act
                self.players_acted = 1 
                
                if not self.check_betting_end():
                    self.next_player()
            else:
                messagebox.showinfo("", "not enough credits to make this bet/raise!")
        else:
            messagebox.showinfo("", "your bet must be greater than 0.")

    def check_betting_end(self):
        # determines if the conditions for ending the betting round are met
        active_players = [p for p in self.players if not p.has_folded]
        
        #if everyone else folded, the last person standing wins 
        if len(active_players) == 1:
            messagebox.showinfo("winner!", f"{active_players[0].name} wins by default!")
            return True
            
        #check if every active player has matched the highest bet
        all_matched = all(p.current_bet == self.current_highest_bet for p in active_players)
        
        #betting is over if everyone has had a turn and everyone's bet matches
        if self.players_acted >= len(active_players) and all_matched:
            messagebox.showinfo("phase complete", "betting is over! moving to the trading phase. improve your hand!")
            
            #starts the game phase
            self.start_trading_phase()
           
            return True
        

    def start_trading_phase(self):
        self.game_phase = "Trading"
        self.players_acted = 0
        
        # finds the first active player to start the trading phase
        self.current_player = 0
        while self.players[self.current_player].has_folded:
            self.current_player += 1
            
        # enable buttons used for trading phase 
        self.draw_card_button.config(state='normal')
        self.discard_button.config(state='normal')
        
        # lock all the buttons that are used for the betting phase
        self.bet_button.config(state='disabled')
        self.fold_button.config(state='disabled')
        self.check_button.config(state='disabled')
        self.call_button.config(state='disabled')
        
        self.update_player_display()

    
    def check_winners(self):

        active_players = [p for p in self.players if not p.has_folded]
        
        valid_players = []
        bombed_out = []
        idiots_array_winners = []
        
        result_message = "| results | \n"

        #loop through all the players that made it to the end (didnt fold)
        for p in active_players:
            val = p.get_hand_value()
            result_message += f"{p.name}'s hand: {val}\n"
            
            # special loop used to check for an idiots array 
            card_values = [c.value for c in p.hand]
            if 0 in card_values and 2 in card_values and 3 in card_values:
                idiots_array_winners.append(p)
                #instant win skip the rest of the loop for the player
                continue 
                
            # check to see if someone went under -23 or over 23 (they lose)
            if val == 0 or val > 23 or val < -23:
                bombed_out.append(p)
            else:
                #check how close each player is to -23 or 23 
                distance = 23 - abs(val)
                # store a tuple grouping their distance score, a tiebreaker score, and the player object
                valid_players.append((distance, -1 if val < 0 else 1, p))
        
        result_message += "\n"

        # used for determining winner
        if idiots_array_winners:
            winner = idiots_array_winners[0]
            winner.credits += self.pot
            result_message += f"\n{winner.name} wins with an Idiot's Array \n"
            result_message += f"they claim the pot of {self.pot} credits\n"
            self.pot = 0
            
        elif valid_players:

            #sorts by the first item in tuple (distance), then the second (tiebreaker)
            valid_players.sort(key=lambda x: (x[0], x[1]))
            #person at 0 = winner 
            winner = valid_players[0][2]
            winner.credits += self.pot
            result_message += f"\n {winner.name} wins the pot of {self.pot} credits! \n"
            self.pot = 0
        else:
            result_message += "\n everyone bombed out! The pot rolls over to the next hand. \n"
            
        messagebox.showinfo("game over!", result_message)
        self.update_player_display()

    
if __name__ == "__main__":

    root = Tk()
    gui = Mainloop(root)
    root.title("Sabbac")
    root.geometry("500x400+200+200")
    root.mainloop()