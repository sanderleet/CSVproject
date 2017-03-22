
"""An application for viewing and manipulating .csv files
    BasicGui is to open and view files in a  window.
    CSV_reader Has the functionality to manipulate comma separated value files.
    Since there are only guidelines on how to create .csv files, there are many different ways the files
    behave. This Application can only handle files with a comma "," as a delimiter.
    """
from tkinter import *
from Basic_GUI import *

def main():
    root = Tk()
    root.title("BasicGUI")
    root.geometry("400x400")
    Basic_GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()