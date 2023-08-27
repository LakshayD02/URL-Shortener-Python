# In this project of URL Shortener, I have used two  modules - `Tkinter Module and PyShortener Module`.
#In Python, Tkinter module is preinstalled but we have to install Pyshortener Module using PIP Command.

#Importing Pyshorteners

import pyshorteners
from tkinter import *                 #Here * means that we are importing everything from tkinter modules

window = Tk()
window.geometry("800x500")            #Providing Width and Height to the window, we use Geometry function
window.configure(bg="black")          #Configure function is used to change the window background colour

#Creating a Button Function
def click():
    url = input1.get()
    short = pyshorteners.Shortener().tinyurl.short(url)
    
    input2.insert(END,short)

Label(window, text="Enter the URL Link", font="sans-serif 20 bold", bg="black", foreground="white").pack(fill="x", pady=30)          # Creating User Label

#Creating a Input Box for user

input1 = Entry(window, font="10", bd=3, width=60)
input1.pack(pady=20)

#Creating Button

Button(window, text="Click Here", font="cambria 15 bold", bg="black",foreground="white", width="10", command= click).pack(pady=20)

#Creating Another Input for copying the URL

input2 = Entry(window, font="sans-serif 18 bold", bg="lightblue", width=30, bd=0)
input2.pack(pady=20)
mainloop()