# John Frisbee GUI Project

import tkinter as tk
from tkinter import *


def main():
    # main window
    root = tk.Tk()

    # First widget - label; displays static text or images
    label = tk.Label(root, text='This is a label!')  # displays the text for the label
    label.pack()

    # Second widget
    button = tk.Button(root, text='This is a button!')
    button.pack()

    # Third widget
    master = Tk()
    Label(master, text='Enter something here: ').grid(row=0)
    entry_one = Entry(master)
    entry_one.grid(row=0, column=1)

    # start GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
