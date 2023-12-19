#!python3

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""
#1,2,4,6,12,52,365

import tkinter as tk
from tkinter import ttk
import random
from tkinter.constants import END

win = tk.Tk()
win.title('Interest Calculator')
win.attributes('-topmost',True)

def intCalc(event):
    try:
        p=principal.get()
        p=float(p)

        r=float(IntRate.get())
        r=r/100

        n=CompPeriods.get()
        n=float(n)
        
        t=Years.get()
        t=float(t)
        #p(1+r/n)^(n*t) 
        A=p*(1+r/n)**(n*t)
        A=round(A,2)
        answer.delete(0,END)
        answer.insert(0,A)

    except:
        answer.delete(0,END)
        answer.insert(0,'Invalid')



Instructions=tk.Label(text='Enter Valid Values, press "=" to calculate')
principal=tk.Entry(width=10)
principalL=tk.Label(width=20,text="Initial Amount($)")
IntRate=tk.Entry(width=10)
IntRateL=tk.Label(width=20,text="Interest Rate(%)")
CompPeriods=ttk.Combobox(width=7,values=[1,2,4,6,12,52,365])
CompPeriods.set(1)
CompPeriodsL=tk.Label(width=20,text="# of Compounding Periods")
Years=tk.Entry(width=10)
YearsL=tk.Label(win,text='Time(Years)')
button=tk.Button(win,width=10,text='=')
answer=tk.Entry(win,width=10)

button.bind("<Button>",intCalc)


Instructions.grid(column=1,row=1,columnspan=2)
principalL.grid(column=1,row=2)
principal.grid(column=2,row=2)
IntRateL.grid(column=1,row=3)
IntRate.grid(column=2,row=3)
CompPeriodsL.grid(column=1,row=4)
CompPeriods.grid(column=2,row=4)
YearsL.grid(column=1,row=5)
Years.grid(column=2,row=5)
button.grid(column=1,row=6)
answer.grid(column=2,row=6)


win.mainloop()