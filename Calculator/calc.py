from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Calculator").grid(column=1, row=0)
ttk.Button(frm, text="1", command=root.destroy).grid(column=5, row=10,)
root.mainloop()