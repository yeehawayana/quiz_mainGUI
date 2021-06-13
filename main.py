from tkinter import*
from functools import partial   # To prevent unwanted windows
import random

class Quiz:
  def __init__(self):
    #FORMATTING THE BACKGROUND COLOUR FOR MAIN SCREEN (temporary color = light blue)
    background_color = "light blue"

    #FORMATTING MAIN MENU GUI
    self.mainmenuquiz_frame = Frame(width=400, height=400,
                                pady=10, bg=background_color)
    self.mainmenuquiz_frame.grid()

    #Row 0 - MAIN MENU QUIZ HEADING
    self.quiz_heading_label = Label(self.mainmenuquiz_frame,
                                    text="QUIZ",
                                    font="Verdana 20 bold",
                                    bg=background_color,
                                    padx=10, pady=10,)
    self.quiz_heading_label.grid(row=0)

    #Row 1 - INSTRUCTIONS ABOUT MAIN MENU GUI FOR USERS  
    self.quiz_instructions_label = Label(text="Welcome to _ Quiz."
                                              " Here you will be quized on    your knowledge on _."
                                              " Please enter a username in order to complete the quiz",
                                        font="Helvetic 10 italic", wrap=300,
                                        bg=background_color, padx=10, 
                                        pady=10, justify=LEFT)
    self.quiz_instructions_label.grid(row=1)

    #ROW 2 -  ENTRY FOR GUI
    self.username_entry = Entry(self.mainmenuquiz_frame,
                                width=20, font ="Arial 14 bold")
    self.username_entry.grid(row=2)
    
    #ROW 3 - WARNING MESSAGE
    
    #ROW 4 - QUIZ AND RESULT BUTTONS
    self.quiz_results_frame = Frame(self.mainmenuquiz_frame)
    self.quiz_results_frame.grid(row=4)
    
    #ROW 4 - QUIZ BUTTON 
    self.quiz_button = Button(self.quiz_results_frame, width=10,
                              text="Quiz yourself")
    self.quiz_button.grid(row=0, column=0)

    #ROW 4 - RESULTS BUTTON
    self.results_button = Button(self.quiz_results_frame, width=10,
                                text="Results")
    self.results_button.grid(row=0, column=1)

    
#Main Routine #Problem with 1 positional argument
if __name__ == "__main__":
  root = Tk()
  root.title("Main Menu")
  something = Quiz()
  root.mainloop()