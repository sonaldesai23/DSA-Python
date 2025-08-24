from tkinter import *

top = Tk()
top.geometry("200x100")

radio = IntVar()

rb1 = Radiobutton(top, text="Red", variable=radio, value=1)
rb1.pack()

rb2 = Radiobutton(top, text="Green", variable=radio, value=2)
rb2.pack()

rb3 = Radiobutton(top, text="Blue", variable=radio, value=3)
rb3.pack()

top.mainloop()
