from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("300x200")

def fun():
    messagebox.showinfo("Hello", "Blue button clicked!")

btn1 = Button(top, text="Red", bg="red", fg="white", width=10)
btn1.pack(side=LEFT)

btn2 = Button(top, text="Green", bg="green", fg="white", width=10, height=3)
btn2.pack(side=TOP)

btn3 = Button(top, text="Blue", bg="blue", fg="white", padx=10, pady=10, command=fun)
btn3.pack(side=BOTTOM)

top.mainloop()

'''
✅ This will create:

A Red button (aligned left)

A Green button (aligned top)

A Blue button (aligned bottom) → when clicked, shows a popup: “Hello, Blue button clicked!”
'''