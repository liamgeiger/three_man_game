#attempt threeman
#import the packages
from tkinter import *
import random

# build the window
window = Tk()
window.title('Three man simulator')
window.geometry('1200x500')
lbl = Label(window, text='Roll the dice', font=('Arial Bold', 50))
lbl.grid(column = 1, row = 0)
dice_1 = Label(window, text="", font=('Arial', 45))
dice_1.grid(column = 0, row = 2)
dice_2 = Label(window, text="", font=('Arial', 45))
dice_2.grid(column = 2, row = 2)
tot = Label(window, text="", font=('Arial', 45))
tot.grid(column = 1, row = 3)
task_1 = Label(window, text="Who's drinking?", font=('arial', 32))
task_1.grid(column =0, row = 4)
task_2 = Label(window, text="Let's pick a three man", font=('arial', 36))
task_2.grid(column =1, row = 5)

#clicker function for one dice
def clicked_1():
    a = str(random.randrange(1, 7, 1))
    dice_1.configure(text = a)
    dice_2.configure(text = "")
    tot.configure(text = "")
    if a == "3":
        task_2.configure(text="You're three man!")
        task_1.configure(text ="")
#clicker function for two dice
def clicked_2():
    a = str(random.randrange(1, 7, 1))
    b = str(random.randrange(1, 7, 1))
    c = str(int(a)+int(b))
    dice_1.configure(text = a)
    dice_2.configure(text = b)
    tot.configure(text = c)
    task_1.configure(text="")
    if a == b:
        task_2.configure(text="Doubles split em or give em")
    elif c == "7":
        task_2.configure(text="To the left drinks!")
    elif c == "11":
        task_2.configure(text="To the right drinks!")
    elif c == "3" or a == "3" or b == "3":
        task_2.configure(text="Three man drinks!")
    else:
        task_2.configure(text = "No one drinks pass the dice")
#buttons

btn_1 = Button(window, text ="Roll a single dice", font=('Arial', 30), command=clicked_1)
btn_1.grid(column = 0, row = 1)
btn_2 = Button(window, text ="Roll both dice", font=('Arial', 30), command=clicked_2)
btn_2.grid(column = 2, row = 1)

window.mainloop()


