#!python3

"""
##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?
"""
import tkinter as tk
from tkinter import ttk
from tkinter.constants import END
win = tk.Tk()
win.attributes('-topmost',True)

def clicky(event):
    x=month.get()
    y=day.get()
    z=year.get()
    EntryDone=f'{x} {y} {z}'
    entry.delete(0,END)
    entry.insert(0,EntryDone)

month=ttk.Combobox(win,width=5,values=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
month.set('Jan')
day=ttk.Combobox(win,width=2,values=list(range(1,32)))
day.set(1)
year=ttk.Combobox(win,width=5,values=list(range(1969,2024)))
year.set(1969)
entry=tk.Entry(win,width=20)
button=tk.Button(win,width=5,text='Info')

button.bind("<Button>",clicky)

button.pack(side=tk.LEFT)
entry.pack(side=tk.BOTTOM)
month.pack(side=tk.LEFT)
day.pack(side=tk.LEFT)
year.pack(side=tk.LEFT)

win.mainloop()

