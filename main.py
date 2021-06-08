from tkinter import*
import random

class Quiz:
  def __init__(self):
    #Formatting colours for main GUI (temporary color = light blue)
    background_color: "light_blue"

    #code for the Quiz frame
    self.mainquiz_frame = frame(width = 400, height = 400,
                            pady = 10)
    self.mainquiz_frame.grid()

    #Formatting main GUI
    self.mainquiz_frame = frame(width = 400, height = 400,
                                pady = 10, bg = background_color)
    self.main_quiz_frame.grid()

    #Row 0 - QUIZ heading
    self.quiz_heading_label = label(self.mainquiz_frame,
                                    text = "QUIZ",
                                    font = "Verdana 20 bold",
                                    bg = background_color,
                                    padx = 10, pady = 10,)
    self.quiz_heading_label.grid(row=0)

    #Row 1 
