import tkinter as tk

window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Calculator GUI")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="")
blabel.grid(column=0, row=1)

clabel = tk.Label(text="")
clabel.grid(column=1, row=1)

clabel = tk.Label(text="")
clabel.grid(column=1, row=1)

button = tk.Button(text="1")
button.grid(column=1, row=2)

button2 = tk.Button(text="2")
button2.grid(column=2, row=2)

button3 = tk.Button(text="3")
button3.grid(column=3, row=2)

button4 = tk.Button(text="4")
button4.grid(column=1, row=3)

button5 = tk.Button(text="5")
button5.grid(column=2, row=3)

button6 = tk.Button(text="6")
button6.grid(column=3, row=3)

button7 = tk.Button(text="7")
button7.grid(column=1, row=4)

button8 = tk.Button(text="8")
button8.grid(column=2, row=4)

button9 = tk.Button(text="9")
button9.grid(column=3, row=4)

button0 = tk.Button(text="0")
button0.grid(column=2, row=5)

window.mainloop()

