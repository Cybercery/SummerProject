from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')

# root.geometry("1200x710")


clicked = True
moves_count = 0


# button click
def button_click(button):
    global clicked, moves_count

    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        moves_count += 1
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        moves_count += 1
    else:
        messagebox.showerror("Tic Tac Toe", "use another button you blind buffoon")


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

root.mainloop()
