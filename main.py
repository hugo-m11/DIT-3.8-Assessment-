from tkinter import*
import card

class Mainloop:
    def __init__ (self, parent):
        self.rule_screen_frame = Frame(parent)
        self.hand_chart_frame = Frame(parent)
        self.main_frame = Frame(parent)
        self.player_one_frame = Frame(parent)
        self.player_two_frame = Frame(parent)
        self.player_three_frame = Frame(parent)
        self.player_four_frame = Frame(parent)
        

    
if __name__ == "__main__":

    root = Tk()
    gui = Mainloop(root)
    root.title("Sabbac")
    root.mainloop()