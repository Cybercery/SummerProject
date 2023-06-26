from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')

# root.geometry("1200x710")


clicked = True
moves_count = 0


def win(b1, b2, b3, player):
    global winner
    b1.config(bg="green")
    b2.config(bg="green")
    b3.config(bg="green")
    messagebox.showinfo("Tic Tac Toe", f"{player} wins")
    winner = True
    reset()


def checkifwon(player):
    winner = False

    # rows
    if button1["text"] == player and button2["text"] == player and button3["text"] == player:
        win(button1, button2, button3, player)

    elif button4["text"] == player and button5["text"] == player and button6["text"] == player:
        win(button1, button2, button3, player)

    elif button7["text"] == player and button8["text"] == player and button9["text"] == player:
        win(button1, button2, button3, player)

    # columns
    elif button1["text"] == player and button4["text"] == player and button7["text"] == player:
        win(button1, button4, button7, player)

    elif button2["text"] == player and button5["text"] == player and button8["text"] == player:
        win(button2, button5, button8, player)

    elif button3["text"] == player and button6["text"] == player and button9["text"] == player:
        win(button3, button6, button9, player)

    # diagonal
    elif button1["text"] == player and button5["text"] == player and button9["text"] == player:
        win(button1, button5, button9, player)

    elif button3["text"] == player and button5["text"] == player and button7["text"] == player:
        win(button3, button5, button7, player)


# button click
def button_click(button):
    global clicked, moves_count

    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        moves_count += 1
        checkifwon("X")
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        moves_count += 1
        checkifwon("O")
    else:
        messagebox.showerror("Tic Tac Toe", "use another button you blind buffoon")

    if moves_count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a tie")
        reset()


# Reset
def reset():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global clicked, moves_count
    clicked = True
    moves_count = 0
    # making buttons
    button1 = Button(root, text=" ", font=("Comic Sans MS", 20), height=3, width=6, bg="white",
                     command=lambda: button_click(button1))
    button2 = Button(root, text=" ", font=("Comic Sans MS", 20), height=3, width=6, bg="white",
                     command=lambda: button_click(button2))
    button3 = Button(root, text=" ", font=("Comic Sans MS", 20), height=3, width=6, bg="white",
                     command=lambda: button_click(button3))
    button4 = Button(root, text=" ", font=("Comic Sans MS", 20), height=3, width=6, bg="white",
                     command=lambda: button_click(button4))
    button5 = Button(root, text=" ", font=("Comic Sans MS", 20), height=3, width=6, bg="white",
                     command=lambda: button_click(button5))
    button6 = Button(root, text=" ", font=("Comic Sans MS", 20), height=3, width=6, bg="white",
                     command=lambda: button_click(button6))
    button7 = Button(root, text=" ", font=("Comic Sans MS", 20), height=3, width=6, bg="white",
                     command=lambda: button_click(button7))
    button8 = Button(root, text=" ", font=("Comic Sans MS", 20), height=3, width=6, bg="white",
                     command=lambda: button_click(button8))
    button9 = Button(root, text=" ", font=("Comic Sans MS", 20), height=3, width=6, bg="white",
                     command=lambda: button_click(button9))

    # placing buttons
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)


# Create menu
menu = Menu(root)
root.config(menu=menu)

options_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()
root.mainloop()
