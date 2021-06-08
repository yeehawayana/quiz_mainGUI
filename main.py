from tkinter import*
import random

class Quiz:
  def __init__(self):
    #FORMATTING THE BACKGROUND COLOUR FOR MAIN SCREEN (temporary color = light blue)
    background_color: "light_blue"

    #CODE FOR MAIN MENU QUIZ GUI
    self.mainquiz_frame = frame(width = 400, height = 400,
                            pady = 10)
    self.mainquiz_frame.grid()

    #FORMATTING MAIN MENU GUI
    self.mainquiz_frame = frame(width = 400, height = 400,
                                pady = 10, bg = background_color)
    self.main_quiz_frame.grid()

    #Row 0 - MAIN MENU QUIZ HEADING
    self.quiz_heading_label = label(self.mainquiz_frame,
                                    text = "QUIZ",
                                    font = "Verdana 20 bold",
                                    bg = background_color,
                                    padx = 10, pady = 10,)
    self.quiz_heading_label.grid(row=0)

    #Row 1 - INSTRUCTIONS ABOUT MAIN MENU GUI FOR USERS  
    self.quiz_instructions_label = label(text = "Welcome to _ Quiz."
                                                "Here you will be quized on    your knowledge on _."
                                                "Please enter a username in order to complete the quiz",
                                        font = "Helvetic 10 italic", wrap = 300,
                                        bg = background_color, padx = 10, 
                                        pady = 10, justify = LEFT)
    self.quiz_instructions_label.grid(row=1)

    #ROW 2 -  ENTRY FOR GUI

                                                