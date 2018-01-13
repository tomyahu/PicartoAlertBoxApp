import abc
import Tkinter as Tk
from .components.canvas_objects.abstract_tkinter_canvas_object import AbstractTkinterCanvasObject
from model.components.abstract_object import AbstractObject


class TkinterAbstractObjectOptions:

    def __init__(self, root, canvas, canvas_object):
        # type: (Tk.Tk, Tk.Canvas, AbstractTkinterCanvasObject) -> None
        self.root = root
        self.canvas = canvas
        self.canvas_obj = canvas_object

        self.position_x_label_text = Tk.StringVar()
        self.position_x_label_text.set("X: " + str(self.canvas_obj.get_pos()[0]))

        self.position_y_label_text = Tk.StringVar()
        self.position_y_label_text.set("Y: " + str(self.canvas_obj.get_pos()[1]))

        self.show_position_options()

    def move_object(self, event):
        self.canvas_obj.set_pos(event.x, event.y)

    def update(self):
        self.canvas_obj.show()

    def show(self):
        self.update_position_options()

    def show_position_options(self):
        Tk.Label(self.root, textvariable=self.position_x_label_text).grid(row=5, column=0, sticky=Tk.W)
        Tk.Label(self.root, textvariable=self.position_y_label_text).grid(row=6, column=0, sticky=Tk.W)

        position_entry_x = Tk.Entry(self.root)
        position_entry_y = Tk.Entry(self.root)

        position_entry_x.grid(row=5, column=1, sticky=Tk.W)
        position_entry_y.grid(row=6, column=1, sticky=Tk.W)

        Tk.Button(self.root, text='Set Position',
                  command=lambda: self.set_pos(position_entry_x.get(), position_entry_y.get())).grid(row=7,
                                                                                                     column=0,
                                                                                                     columnspan=2)

    def update_position_options(self):
        self.position_x_label_text.set("X: " + str(self.canvas_obj.get_pos()[0]))
        self.position_y_label_text.set("Y: " + str(self.canvas_obj.get_pos()[1]))

    def grid_text_labels(self):
        Tk.Label(self.root, textvariable=self.position_x_label_text).grid(row=5, column=0, sticky=Tk.W)
        Tk.Label(self.root, textvariable=self.position_y_label_text).grid(row=6, column=0, sticky=Tk.W)

    def set_pos(self,x,y):
        if x.isdigit() and y.isdigit():
            self.canvas_obj.set_pos(x,y)

    def grid_all(self):
        self.grid_text_labels()
