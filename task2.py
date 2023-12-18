#!python3

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.attributes('-topmost',True)

entry1=tk.Entry(win,width=6)
entry2=tk.Entry(win,width=6)
spin1=tk.Spinbox(win,width=4,values=['+','-','x','/'])
button=tk.Button(win,width=2,text='=')
answer=tk.Entry(win,width=6)

entry1.grid(column=1,row=1)
spin1.grid(column=2,row=1)
entry2.grid(column=3,row=1)
button.grid(column=4,row=1)
answer.grid(column=5,row=1)


win.mainloop()