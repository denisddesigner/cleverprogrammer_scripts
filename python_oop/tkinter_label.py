import tkinter as tk
# not being used - provides grey background to 'Banana' label
from tkinter import ttk

window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Banana")
alabel.grid(column= 0, row = 0)


window.mainloop()

