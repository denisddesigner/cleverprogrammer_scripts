import tkinter as tk

def doorbell(event):
	print("You rang the doorbell!")

def greeting(event):
	print("Please come in!!")


window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Door")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="House Owner")
blabel.grid(column=1, row = 0)

button = tk.Button(window, text="Doorbell")
button.grid(column=0)

button2 = tk.Button(window, text="Greeting")
button2.grid(column=1, row=1)


button.bind("<Button-1>", doorbell)
button2.bind("<Button-1>", greeting)

window.mainloop()

