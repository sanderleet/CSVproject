#basic GUI

from tkinter import *

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
        """Create a button to show clicks"""

        self.button_open_file = Button(self)
        self.button_open_file["command"] =self.open_a_file()
        self.button_open_file["text"] = "Open"
        self.button_open_file.grid(column=MENU)


    def open_a_file(self):
        self.new_box = Tk()
        self.new_box.title("Open a File")
        self.new_box.geometry("200x85")
        self.new_box.button = Button()
        self.new_box.button["text"] = "hey"
        self.new_box.file_name = Entry(self)
        self.new_box.file_name.grid()
        self.new_box.button.grid()

    def open_a_file_to_matrix(self, filename):

        an_array = return_matrix_from_csv(filename)
        for row_index, row in enumerate(an_array):
            for item_index, item in enumerate(row):
                self.Matrice_label = Label(self)
                self.Matrice_label["text"] = "{items}".format(items=item)
                self.Matrice_label.grid(row=row_index, column=item_index + MATRIX_LABEL_POSITION)


root = Tk()
root.title("BasicGUI")
root.geometry("400x400")
MENU = 0
MATRIX_LABEL_POSITION = 1
app = Basic_GUI(root)


root.mainloop()
