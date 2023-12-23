import tkinter as tk

def addition():
    try:
        ans = float(val1.get())+float(val2.get())
        label = tk.Label(WINDOW, text=ans)
        label.grid(row=5,column=1)
    except ValueError:
        label = tk.Label(WINDOW, text="Please enter correct values")
        label.grid(row=5, column=1)
def subtract():
    try:
        ans = float(val1.get())-float(val2.get())
        label = tk.Label(WINDOW, text=ans)
        label.grid(row=5,column=1)
    except ValueError:
        label = tk.Label(WINDOW, text="Please enter correct values")
        label.grid(row=5, column=1)
def divide():
    try:
        ans = float(val1.get())/float(val2.get())
        label = tk.Label(WINDOW, text=ans)
        label.grid(row=5,column=1)
    except ValueError:
        label = tk.Label(WINDOW, text="Please enter correct values")
        label.grid(row=5, column=1)
def multiply():
    try:
        ans = float(val1.get())*float(val2.get())
        label = tk.Label(WINDOW, text=ans)
        label.grid(row=5,column=1)
    except ValueError:
        label = tk.Label(WINDOW, text="Please enter correct values")
        label.grid(row=5, column=1)
############
#The App
WINDOW =  tk.Tk()

title = tk.Label(text="Calculator")
title.grid(row=0,column=0)

#label for val1
val1_title = tk.Label(text="First value:")
val1_title.grid(row=1,column=0)
#entry box for val1
val1 = tk.StringVar()
val1_entry = tk.Entry(WINDOW, textvariable=val1)
val1_entry.grid(row=1,column=1)

#label for val2
val2_title = tk.Label(text="Second value:")
val2_title.grid(row=2,column=0)
#entry box for val1
val2 = tk.StringVar()
val2_entry = tk.Entry(WINDOW, textvariable=val2)
val2_entry.grid(row=2,column=1)

#buttons for math stuff
add_btn = tk.Button(WINDOW, text="Add", command=addition)
add_btn.grid(row=3, column=0)
sub_btn = tk.Button(WINDOW, text="Subtract", command=subtract)
sub_btn.grid(row=3, column=1)
div_btn = tk.Button(WINDOW, text="Divide", command=divide)
div_btn.grid(row=4, column=0)
mul_btn = tk.Button(WINDOW, text="Multiply", command=multiply)
mul_btn.grid(row=4, column=1)

#label(??)
answer = tk.Label(WINDOW, text="Answer is:")
answer.grid(row=5,column=0)

WINDOW.mainloop()