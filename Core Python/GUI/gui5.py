from tkinter import *
from tkinter import messagebox

def submit_action():
    name_value = c1.get()
    regno_value = c2.get()
    messagebox.showinfo("Submitted Data", f"Name: {name_value}\nRegd No: {regno_value}")

parent = Tk()
parent.title("Students")
parent.geometry("300x200")

name = Label(parent, text="Name :")
name.place(x=50, y=50)

c1 = Entry(parent)
c1.place(x=120, y=50)

regno = Label(parent, text="Regd No :")
regno.place(x=50, y=100)

c2 = Entry(parent)
c2.place(x=120, y=100)

btn = Button(parent, text="Submit", command=submit_action)
btn.place(x=120, y=150)

parent.mainloop()

'''
Now when you run this and press Submit, a message box will pop up showing the entered Name and Regd No.
'''