from canvas_objects import *
from ..tkinter_abstract_obj_options import TkinterAbstractObjectOptions
import Tkinter as Tk


class Layer:

    def __init__(self, object_options, root, name):
        # type: (TkinterAbstractObjectOptions, Tk.Tk, str) -> None
        self.obj_options = object_options
        self.root = root
        self.name = name
        self.selected = False
        self.obj_options.update()

    def get_object_options(self):
        return self.obj_options

    def show_config_view(self):
        self.obj_options.show()
        self.obj_options.grid_all()

    def move_object(self):
        self.obj_options.move_object()

    def update(self):
        self.obj_options.update()

    def get_name(self):
        return self.name

    def rename(self, new_name):
        self.name = new_name

    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

    def is_selected(self):
        return self.selected