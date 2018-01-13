import Tkinter as Tk
from abstractLayerList import AbstractLayerList


class ListBoxLayerList(Tk.Listbox, AbstractLayerList):

    def __init__(self, root):
        Tk.Listbox.__init__(self, root)

    def show(self, row, column):
        self.grid(row=row, column=column, ipady=125)
