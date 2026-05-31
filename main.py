from tkinter import*
from tkinter.scrolledtext import*
import card

class Mainloop:
    def __init__ (self, parent):
        self.rule_screen_frame = Frame(parent)
        self.main_frame = Frame(parent)


        self.title_label = Label(self.main_frame, text="Sabacc", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, pady=10)

        self.rules_button = Button(self.main_frame,text="See Rules", command=lambda: self.switch_frame_rule(self.rule_screen_frame))
        self.rules_button.grid(row=1, column=0, pady=5)

        self.rule_screen_title = Label(self.rule_screen_frame, text="Rules", font=("Arial", 20))
        self.rule_screen_title.grid(row=0, column=0)

        self.exit_to_main_frame_button = Button(self.rule_screen_frame,text="Back", command=lambda: self.switch_frame_rule(self.main_frame))
        self.exit_to_main_frame_button.grid(row=1, column=0)

        # Start on main menu
        self.switch_frame_rule(self.main_frame)
       
    def switch_frame_rule(self, frame):
        self.main_frame.grid_forget()
        self.rule_screen_frame.grid_forget()
        frame.grid()

    
if __name__ == "__main__":

    root = Tk()
    gui = Mainloop(root)
    root.title("Sabbac")
    root.mainloop()