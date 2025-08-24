from tkinter import *

top = Tk()
top.geometry("300x200")

l1 = Label(top, text="Price", bg="yellow", fg="red")
l1.pack()

scale = Scale(top, from_=100, to=1000, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

top.mainloop()
