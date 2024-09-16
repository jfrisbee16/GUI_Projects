# John Frisbee GUI Project

import tkinter as tk


def main():
    # main window
    root = tk.Tk()

    # First widget - label; displays static text or images
    label = tk.Label(root, text='This is a label!')  # displays the text for the label
    label.pack()

    # start GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
