from tkinter import*
from functools import partial   # To prevent unwanted windows
import random


class Main_Menu:
  def __init__(self):
    #FORMATTING THE BACKGROUND COLOUR FOR MAIN SCREEN (temporary color = light blue)
    background_color = "light blue"

    #FORMATTING MAIN MENU GUI
    self.mainmenuquiz_frame = Frame(pady=10, bg=background_color, width=200)
    self.mainmenuquiz_frame.grid()

    #Row 0 - MAIN MENU QUIZ HEADING
    self.mainmenu_heading_label = Label(self.mainmenuquiz_frame,
                                    text="QUIZ",
                                    font="Verdana 20 bold",
                                    bg=background_color,
                                    pady=10, width=10)
    self.mainmenu_heading_label.grid(row=0)

    #Row 1 - INSTRUCTIONS ABOUT MAIN MENU GUI FOR USERS  
    self.mainmenu_instructions_label = Label(text="Welcome to _ Quiz."
                                              " Here you will be quized on your knowledge on _."
                                              " Please enter a username in order to complete the quiz.",
                                        font="Helvetic 11 italic", wrap=200,
                                        bg=background_color, padx=10,
                                        pady=10, justify=LEFT)
    self.mainmenu_instructions_label.grid(row=1)

    #ROW 2 -  ENTRY FOR GUI
    self.username_entry = Entry(self.mainmenuquiz_frame,
                                width=15, font ="Arial 14")
    self.username_entry.grid(row=2)
    
    #ROW 3 - WARNING MESSAGE
    
    #ROW 4 - QUIZ AND RESULT BUTTONS
    self.mainmenu_results_frame = Frame(self.mainmenuquiz_frame)
    self.mainmenu_results_frame.grid(row=4)
    
    #ROW 4 - QUIZ BUTTON 
    self.quiz_button = Button(self.mainmenu_results_frame, width=10, padx=10,
                              pady=10, text="Quiz yourself", bg="lavender")
    self.quiz_button.grid(row=0, column=0)

    #ROW 4 - RESULTS BUTTON
    self.results_button = Button(self.mainmenu_results_frame, width=5, padx=10,
                                pady=10, text="Results", bg="yellow", command=self.results)
    self.results_button.grid(row=0, column=1)

  def results(self):
    print("You have asked for your results")
    get_results = Results(self)
    get_results.results_text.configure(text="Here the results done below")

  def quiz(self):
    go_quiz = Quiz(self)
    go_quiz.quiz_text.configure(text="Quiz")


class Results:
    #Setting up frame for result GUI
    def __init__ (self, partner):
      background_color="orange"

      #Results Button becomes dsiabled when results GUI pops up
      partner.results_button.config(state=DISABLED)

      self.results_box=Toplevel()

      #GUI FRAME for Results
      self.results_frame=Frame(self.results_box, bg=background_color, width=100)
      self.results_frame.grid()

      #Text for Results GUI - ROW 0
      self.results_heading=Label(self.results_frame, text="Results",
                                  font="arial 14 bold", bg=background_color)
      self.results_heading.grid(row=0)

      #ROW 1 - Results pops up 
      self.results_text=Label(self.results_frame, text="",
                        justify=LEFT, width=40, bg=background_color, wrap=250)
      self.results_text.grid(column=0, row=1)#column=0 added - SGF

      #ROW 2 - Return to main menu button
      self.results_button = Button(self.results_frame, padx=10, pady=10,
                                  text="Return to Main Menu", command=self.close_results)
      self.results_button.grid(row=2, pady=5)

    def close_results(self):
      root.deiconify()
      self.results_box.destroy()
      self.results_button.config(state=NORMAL)

class Quiz:
  def __init__(self, partner):
    #Background colour for quiz GUI
    background_color: "light pink"

    #disabling quiz button when quiz GUI pops up
    partner.quiz_button.config(state=DISABLED)

    self.quiz_box = Toplevel()

    #GUI FRAME for Quiz
    self.quiz_frame=Frame(self.quiz_box, bg=background_color, width=150)
    self.quiz_frame.grid()

    #ROW 0 - 

#Main Routine
if __name__ == "__main__":
  root = Tk()
  root.title("Main Menu")
  something = Main_Menu()
  root.mainloop()