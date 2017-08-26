import tkinter as tk 
from tkinter import PhotoImage
import webbrowser

URL = "http://cleverprogrammer.com"

def open_hm(event):
  webbrowser.open_new_tab("https://thehappymindset.com/")

def open_cpb(event):
  webbrowser.open_new_tab(URL + "/blog")

def open_cp(event):
  webbrowser.open_new_tab(URL)
  
window = tk.Tk()
window.geometry("750x250")
window.configure(background="black")
  
p1 = PhotoImage(file='image.gif')
  
P1 = tk.Label(height=150, width=120, image = p1)
P1.grid(column=15, row=4)

alabel = tk.Label(text="Bookmarks Toolbar", bg='black', fg = 'orange')
alabel.grid(column=15, row=0)

button = tk.Button(window, text="Cleverprogrammer Blog")
button.grid(column=0, row=1)

button2 = tk.Button(window, text="Cleverprogrammer")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="thehappymindset")
button3.grid(column=2, row=1)


button.bind("<Button-1>", open_cpb)
button2.bind("<Button-1>", open_cp)
button3.bind("<Button-1>", open_hm)

window.mainloop()