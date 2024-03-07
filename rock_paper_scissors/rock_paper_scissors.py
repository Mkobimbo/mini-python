from tkinter import *
import random

#defining global variables
your_choice = ""
Comp_choice = ""
computer_score = 0 
your_score = 0

#map integers to choices
Comp_dict = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

#clear the text area where choices are displayed
def Playagain(text_to_display):
    text_to_display.delete("1,0", "end")



#update pointrs after every game
def points(text_to_scores):
    text_to_scores.delete("1.0", "end")
    text_to_scores.insert(END, f"{your_score}     {computer_score}")  



#result after user selects rock    
def rock(text_to_display, text_to_scores):
    global computer_score
    global your_score
    your_choice = "Rock"
    Comp_choice = Comp_dict[str(random.randint(0,2))]
    text_to_display.insert(END, f"Your Choice: {your_choice}\nComputer's Choice:    {Comp_choice}")        

    if Comp_choice == "Paper":
        computer_score += 1
    if Comp_choice == "Scissor":
        your_score += 1
    points(text_to_scores)


def paper(text_to_display, text_to_scores):
    global computer_score
    global your_score
    your_choice = "Paper"
    Comp_choice = Comp_dict[str(random.randint(0, 2))]
    text_to_display.insert(END, f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}")

    if Comp_choice == "Scissor":
        computer_score += 1
    if Comp_choice == "Rock":
        your_score += 1
    points(text_to_scores)

# Function to define what happens when the user selects Scissor
def scissor(text_to_display, text_to_scores):
    global computer_score
    global your_score
    your_choice = "Scissor"
    Comp_choice = Comp_dict[str(random.randint(0, 2))]
    text_to_display.insert(END, f"Your Choice:          {your_choice}\nComputer's Choice:    {Comp_choice}")

    if Comp_choice == "Rock":
        computer_score += 1
    if Comp_choice == "Paper":
        your_score += 1
    points(text_to_scores)

