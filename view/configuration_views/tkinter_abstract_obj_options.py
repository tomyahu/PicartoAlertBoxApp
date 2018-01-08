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

    def move_object(self, event):
        self.canvas_obj.set_pos(event.x, event.y)

    def update(self):
        self.canvas_obj.show()

    @abc.abstractmethod
    def show(self):
        pass
