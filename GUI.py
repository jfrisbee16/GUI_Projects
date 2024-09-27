# John Frisbee GUI Project

import tkinter as tk
from tkinter import *


def main():
    # main window
    root = tk.Tk()

    # label; displays static text or images
    # label = tk.Label(root, text='This is a label!')  # displays the text for the label
    # label.pack()

    # button - self explanatory
    # button = tk.Button(root, text='Click on this button!')
    # button.pack()

    # entry; allows input into a field
    # master = Tk()
    # Label(master, text='Enter something here: ').grid(row=0)
    # entry_one = Entry(master)
    # entry_one.grid(row=0, column=1)

    # check button; inputs a check field, multiple select available
    # master = Tk()
    # var1 = IntVar()
    # Checkbutton(master, text='option 1', variable=var1).grid(row=0, sticky=W)
    # mainloop()

    # Radio Button; offers multiple choices, only one allowed to be selected
    # root = Tk()
    # v = IntVar()
    # Radiobutton(root, text='A', variable=v, value=1).pack(anchor=W)
    # Radiobutton(root, text='B', variable=v, value=2).pack(anchor=W)
    # mainloop()

    # Listbox; offers a list of options to choose from
    # top = Tk()
    # Lb = Listbox(top)
    # Lb.insert(1, 'Credit Card')
    # Lb.insert(2, 'Debit Card')
    # Lb.insert(3, 'Cash')
    # Lb.pack()
    # top.mainloop()

    # scrollbar
    # root = Tk()
    # scrollbar = Scrollbar(root)
    # scrollbar.pack(side=RIGHT, fill=Y)
    # mylist = Listbox(root, yscrollcommand=scrollbar.set)
    #
    # for line in range(100):
    #     mylist.insert(END, 'line number: ' + str(line))
    #
    # mylist.pack(side=LEFT, fill=BOTH)
    # scrollbar.config(command=mylist.yview)
    # mainloop()

    # start GUI event loop
    root.mainloop()



if __name__ == "__main__":
    main()
