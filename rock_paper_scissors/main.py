from tkinter import *
from rock_paper_scissors import *
from rock_paper_scissors import rock, paper, scissor, Playagain

# The main window

root = Tk()
root.title("Rock Paper Scissors")
root.geometry('270x200')
root.config(bg="sky blue")

# widget to display choices
text_to_display = Text(root, height=3, width=30)
text_to_display.grid(row=0, columnspan=5, pady=10)

#buttons for rock, paper and scissor
bttn_rock = Button(root, text="Rock", width=6, command=lambda: rock(text_to_scores))
bttn_rock.grid(row=2, column=0, padx=10)

bttn_paper = Button(root, text="Paper", width=6,command=lambda: paper(text_to_scores) )
bttn_rock.grid(row=2, column=1, padx=5)

bttn_scissor =Button(root, text="Scissor", width=6, command=lambda: scissor(text_to_scores))
bttn_scissor.grid(row=2, column=2, padx=10)

#text to widget display scores
text_to_scores = Text(root, height=1, width=30)
text_to_scores.grid(row=4, columnspan=5, pady=5)

#play again button
Play_again = Button(root, text="Play Again", command=lambda: Playagain(text_to_display))
Play_again.grid(row=5, columnspan=3)

#start the tkinter event loop
root.mainloop()