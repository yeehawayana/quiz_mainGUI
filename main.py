from tkinter import*
from functools import partial   # To prevent unwanted windows
import random


class Quiz:
  def __init__(self):
    #FORMATTING THE BACKGROUND COLOUR FOR MAIN SCREEN (temporary color = light blue)
    background_color = "light blue"

    #FORMATTING MAIN MENU GUI
    self.mainmenuquiz_frame = Frame(pady=10, bg=background_color, width=200)
    self.mainmenuquiz_frame.grid()

    #Row 0 - MAIN MENU QUIZ HEADING
    self.quiz_heading_label = Label(self.mainmenuquiz_frame,
                                    text="QUIZ",
                                    font="Verdana 20 bold",
                                    bg=background_color,
                                    padx=10, pady=10, width=10)
    self.quiz_heading_label.grid(row=0)

    #Row 1 - INSTRUCTIONS ABOUT MAIN MENU GUI FOR USERS  
    self.quiz_instructions_label = Label(text="Welcome to _ Quiz."
                                              " Here you will be quized on your knowledge on _."
                                              " Please enter a username in order to complete the quiz.",
                                        font="Helvetic 11 italic", wrap=200,
                                        bg=background_color, padx=20,
                                        pady=10, justify=LEFT)
    self.quiz_instructions_label.grid(row=1)

    #ROW 2 -  ENTRY FOR GUI
    self.username_entry = Entry(self.mainmenuquiz_frame,
                                width=15, font ="Arial 14")
    self.username_entry.grid(row=2)
    
    #ROW 3 - WARNING MESSAGE
    
    #ROW 4 - QUIZ AND RESULT BUTTONS
    self.quiz_results_frame = Frame(self.mainmenuquiz_frame)
    self.quiz_results_frame.grid(row=4)
    
    #ROW 4 - QUIZ BUTTON 
    self.quiz_button = Button(self.quiz_results_frame, width=10, padx=10,
                              pady=10, text="Quiz yourself", bg="lavender")
    self.quiz_button.grid(row=0, column=0)

    #ROW 4 - RESULTS BUTTON
    self.results_button = Button(self.quiz_results_frame, width=5, padx=10,
                                pady=10, text="Results", bg="yellow", command=self.results)
    self.results_button.grid(row=0, column=1)

  def results(self):
    print("You have asked for your results")
    get_results = Results(self)
    get_results.results_text.configure(text="Here the results done below")


class Results:
    #Setting up frame for result GUI
    def __init__ (self, partner):
      background_color="orange"

      #Results Button becomes dsiabled when results GUI pops up
      partner.results_button.config(state=DISABLED)

      self.result_box=Toplevel()

      #GUI FRAME for Results
      self.results_frame=Frame(self.results_box, bg=background_color, width=200)
      self.results_frame.grid()

      #Text for Results GUI - ROW 0
      self.results_heading=Label(self.results_frame, text="Results",
                                  font="arial 14 bold", bg=background_color)
      self.results_heading.grid(row=0)

      #ROW 1 -
      self.results_text=Label(self.help_frame, text="",
                        justify=LEFT, width=40, bg=background, wrap=250)
      self.results_text.grid(column=0, row=1)#column=0 added - SGF





#Main Routine
if __name__ == "__main__":
  root = Tk()
  root.title("Main Menu")
  something = Quiz()
  root.mainloop()