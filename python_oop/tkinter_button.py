import tkinter as tk

window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Banana")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="Apple")
blabel.grid(column=1, row=0)

clabel = tk.Label(text="Orange")
clabel.grid(column=2, row=0)

button = tk.Button(text="5")
button.grid(column=0)

button2 = tk.Button(text="10")
button2.grid(column=1, row=1)

button3 = tk.Button(text="15")
button3.grid(column=2, row=1)

window.mainloop()



