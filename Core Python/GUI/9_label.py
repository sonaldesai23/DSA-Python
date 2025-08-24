from tkinter import *

top = Tk()
top.geometry("300x200")

l1 = Label(top, text="Name")
l1.place(x=10, y=30)

l2 = Label(top, text="Password", fg="red", bg="yellow")
l2.place(x=10, y=60)

l3 = Label(top, text="Age", fg="blue", pady=10, bg="green")
l3.place(x=10, y=90)

top.mainloop()
'''
👉 The first program displays three labels (Name, Password, Age) with different styles and positions.
'''