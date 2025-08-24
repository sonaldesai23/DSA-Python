from tkinter import *

top = Tk()
top.geometry("300x200")

entry0 = Entry(top, width=30)
entry0.place(x=50, y=40)

entry1 = Entry(top, bg="yellow")
entry1.place(x=50, y=70)

entry2 = Entry(top, fg="red", show="*")
entry2.place(x=50, y=100)

top.mainloop()

'''
✅ This creates three text fields:

A normal Entry (width 30)

An Entry with yellow background

A password-like Entry (red text, masked with *)
'''