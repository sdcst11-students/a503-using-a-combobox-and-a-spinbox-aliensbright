#!python3

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""
import tkinter as tk
from tkinter import ttk
from tkinter.constants import END

win = tk.Tk()
win.attributes('-topmost',True)

def calculate(event):
    a=entry1.get()
    a=float(a)
    b=entry2.get()
    b=float(b)
    op=spin1.get()
    if op=="+":
        ansr=a+b
    elif op=="-":
        ansr=a-b
    elif op=="x":
        ansr=a*b
    elif op=="/":
        ansr=a/b
    else:
        ansr='Invalid'
    answer.delete(0,END)
    answer.insert(0,ansr)

inst=tk.Label(text='Press the "=" to calculate.')
entry1=tk.Entry(win,width=6)
entry2=tk.Entry(win,width=6)
spin1=tk.Spinbox(win,width=4,values=['+','-','x','/'])
button=tk.Button(win,width=2,text='=')
answer=tk.Entry(win,width=6)

button.bind("<Button>",calculate)


inst.grid(column=1,columnspan=5,row=1)
entry1.grid(column=1,row=2)
spin1.grid (column=2,row=2)
entry2.grid(column=3,row=2)
button.grid(column=4,row=2)
answer.grid(column=5,row=2)


win.mainloop()