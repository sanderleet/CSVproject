#basic GUI

from tkinter import *
from tkinter import filedialog

from CSV_Reader import *


class Basic_GUI(Frame):
    """A gui app with three buttons"""

    def __init__(self, master):
        """Initialize the frame"""
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 0
        self.create_menu()

    def create_menu(self):
        """Create menu buttons """
        self.master.title("Simple menu")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_command(label="Open", command=self.onOpen)

    def onExit(self):
        self.quit()

    def open_a_file_to_matrix(self, filename):
        an_array = return_matrix_from_csv(filename)
        for row_index, row in enumerate(an_array):
            for item_index, item in enumerate(row):
                self.Matrice_label = Label(self)
                self.Matrice_label["text"] = "{items}".format(items=item)
                self.Matrice_label.grid(row=row_index, column=item_index + MATRIX_LABEL_POSITION)

    def onOpen(self):
        filename = (filedialog.askopenfilename())
        self.open_a_file_to_matrix(filename)


root = Tk()
root.title("BasicGUI")
root.geometry("400x400")
MENU = 0
MATRIX_LABEL_POSITION = 1
app = Basic_GUI(root)


root.mainloop()
