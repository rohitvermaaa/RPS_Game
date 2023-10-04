from tkinter import *
import random
from PIL import Image, ImageTk

comp = 0
user = 0

def des():
    w.destroy()

def res():
    b4.grid_forget()
    b5.grid_forget()
    global comp
    global user
    comp = 0
    user = 0
    l = Label(text="ROCK  PAPER  SCISSORS", font=('Arial', 36), bg="#000000", fg="white", pady="20")
    la1.configure(text="\n\nMax points: 5\n\n", font=('Arial', 12, 'bold'), bg="#000000", fg="white")
    la2.configure(text=f'\n\nUser points: {user}\t\t\tComputer points: {comp}\n', font=(
        'Arial', 12, 'bold'), bg="#000000", fg="white")
    la1.grid(column=0, row=1, columnspan=6)
    b1.grid(column=0, row=4, columnspan=2)
    b2.grid(column=2, row=4, columnspan=2)
    b3.grid(column=4, row=4, columnspan=2)
    la2.grid(column=0, row=5, columnspan=6)
    l.grid(column=0, row=0, columnspan=6)

def rk():
    global comp
    global user
    cout = random.randint(1, 4)
    if cout == 1:
        la1.configure(font=('Arial', 12, 'bold'), bg="#000000", fg="white",
            text="\nUser's move: Rock\t\t\tComputer's move: Rock\n\nTIE!\n")
    elif cout == 2:
        comp = comp+1
        la1.configure(bg="#000000", fg="white", font=('Arial', 12, 'bold'), text="\nUser's move: Rock\t\t\tComputer's move: Paper\n\nComputer gets a point.\n")
    elif cout == 3:
        user = user+1
        la1.configure(font=('Arial', 12, 'bold'), bg="#000000", fg="white",
            text="\nUser's move: Rock\t\t\tComputer's move: Paper\n\nUser gets a point!\n")
    la2.configure(text=f'\n\nUser points: {user}\t\t\tComputer points: {comp}\n', font=(
        'Arial', 12, 'bold'), bg="#000000", fg="white")
    if user == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Arial', 16, 'bold'), bg="#000000", fg="hotpink1",
                      text="\nUser wins!!\nCongratulations!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)
    elif comp == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Arial', 16, 'bold'), bg="#000000", fg="tomato",
                      text="\nComputer wins!!\nBetter Luck Next time!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)

def pp():
    global comp
    global user
    cout = random.randint(1, 3)
    if(cout == 1):
        la1.configure(font=('Arial', 12, 'bold'), bg="#000000", fg="white",
            text="\nUser's move: Paper\t\t\tComputer's move: Paper\n\nTIE!\n")
    elif(cout == 2):
        comp = comp+1
        la1.configure(font=('Arial', 12, 'bold'), bg="#000000", fg="white",
            text="\nUser's move: Paper\t\t\tComputer's move: Scissor\n\nComputer gets a point!\n")
    elif(cout == 3):
        user = user+1
        la1.configure(font=('Arial', 12, 'bold'), bg="#000000", fg="white",
            text="\nUser's move: Paper\t\t\tComputer's move: Rock\n\nUser gets a point!\n")
    la2.configure(text=f'\n\nUser points: {user}\t\t\tComputer points: {comp}\n', font=(
        'Arial', 12, 'bold'), bg="#000000", fg="white")
    if user == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Arial', 16, 'bold'), bg="#000000", fg="hotpink1",
                      text="\nUser wins!!\nCongratulations!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)
    elif comp == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Arial', 16, 'bold'), bg="#000000", fg="tomato",
                      text="\nComputer wins!!\nBetter Luck Next time!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)

def sc():
    global comp
    global user
    cout = random.randint(1, 3)
    if(cout == 1):
        la1.configure(font=('Arial', 12, 'bold'), bg="black", fg="white",
            text="\nUser's move: Scissor\t\t\tComputer's move: Scissor\n\nTIE!\n")
    elif(cout == 2):
        comp = comp+1
        la1.configure(font=('Arial', 12, 'bold'), bg="black", fg="white",
            text="\nUser's move: Scissor\t\t\tComputer's move: Rock\n\nComputer gets a point!\n")
    elif(cout == 3):
        user = user+1
        la1.configure(font=('Arial', 12, 'bold'), bg="black", fg="white",
            text="\nUser's move: Scissor\t\t\tComputer's move: Paper\n\nUser gets a point!\n")
    la2.configure(text=f'\n\nUser points: {user}\t\t\tComputer points: {comp}\n', font=(
        'Arial', 12, 'bold'), bg="black", fg="white")
    if user == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Arial', 16, 'bold'), bg="black", fg="hotpink1",
                      text="\nUser wins!!\nCongratulations!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)
    elif comp == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Arial', 16, 'bold'), bg="black", fg="tomato",
                      text="\nComputer wins!!\nBetter Luck Next time!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)
        
w = Tk()
w.minsize(840, 500)
w.title("rock-paper-scissor-game")
w.configure(bg="#000000")
icon_image = Image.open("icon.png")
icon = ImageTk.PhotoImage(icon_image)
w.iconphoto(True, icon)

l = Label(text="ROCK  PAPER  SCISSORS", font=('Arial', 36), bg="#000000", fg="white", pady="20")

la1 = Label(text="\n\nMax points: 5\n\n", font=(
    'Arial', 12, 'bold'), bg="#000000", fg="white")
la2 = Label(text=f'\n\nUser points: {user}\t\t\tComputer points: {comp}\n', font=(
    'Arial', 12, 'bold'), bg="#000000", fg="white")

rock_img = PhotoImage(file="rockplayer.png")
paper_img = PhotoImage(file="paperplayer.png")
scissors_img = PhotoImage(file="scissorsplayer.png")

b1 = Button(w, image=rock_img, command=rk, pady="20", padx="32", bd=0, bg="black", activebackground="tomato")
b2 = Button(w, image=paper_img, command=pp, pady="20", padx="32", bd=0, bg="black", activebackground="gold")
b3 = Button(w, image=scissors_img, command=sc, pady="20", padx="32", bd=0, bg="black", activebackground="turquoise1")
b4 = Button(w, text="END", command=des, pady="14", padx="30", bd=0, bg="black", fg="white", font=('Arial', 13, 'bold'), activebackground="IndianRed1", activeforeground="white")
b5 = Button(w, text="RESTART", command=res, pady="14", padx="20", bd=0, bg="black", fg="white", font=('Arial', 13, 'bold'), activebackground="forest green", activeforeground="white")

l.grid(column=0, row=0, columnspan=6)
la1.grid(column=0, row=1, columnspan=6)
b1.grid(column=0, row=4, columnspan=2)
b2.grid(column=2, row=4, columnspan=2)
b3.grid(column=4, row=4, columnspan=2)
la2.grid(column=0, row=5, columnspan=6)

# Function to configure button on mouse enter and leave
def on_enter(e):
    e.widget.config(bg='red4', fg="white")

def on_leave(e):
    e.widget.config(bg='black', fg="white")

buttons = [b1, b2, b3, b4, b5]

for button in buttons:
    button.bind('<Enter>', on_enter)
    button.bind('<Leave>', on_leave)

w.grid_rowconfigure(0, weight=1)
w.grid_rowconfigure(1, weight=1)
w.grid_rowconfigure(2, weight=1)
w.grid_rowconfigure(3, weight=1)
w.grid_rowconfigure(4, weight=1)
w.grid_rowconfigure(5, weight=1)
w.grid_rowconfigure(6, weight=1)
w.grid_rowconfigure(7, weight=1)
w.grid_rowconfigure(8, weight=1)
w.grid_columnconfigure(0, weight=1)
w.grid_columnconfigure(1, weight=1)
w.grid_columnconfigure(2, weight=1)
w.grid_columnconfigure(3, weight=1)
w.grid_columnconfigure(4, weight=1)
w.grid_columnconfigure(5, weight=1)

w.mainloop()
