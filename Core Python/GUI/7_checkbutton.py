from tkinter import *

top = Tk()
top.geometry("300x200")

cb1 = Checkbutton(top, text="Red", fg="red")
cb1.pack()

cb2 = Checkbutton(top, text="Green", fg="green", activebackground="yellow")
cb2.pack()

cb3 = Checkbutton(top, text="Blue", fg="blue", bg="orange", width=10)
cb3.pack()

top.mainloop()

'''
✅ This will create three checkbuttons:

Red text (normal checkbutton)

Green text (background turns yellow when active/pressed)

Blue text with orange background and fixed width
'''