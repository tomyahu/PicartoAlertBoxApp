import abc
from model.components.abstract_object import AbstractObject
import Tkinter as Tk

class AbstractTkinterCanvasObject:

    def __init__(self, canvas, component):
        """
        Creates a new instance of the class AbstractTextAlertBox
        """
        # type: (Tk.Canvas ,AbstractObject) -> None
        self.component = component
        self.canvas = canvas
        self.canvas_id = 0

    def get_canvas_component_id(self):
        return self.canvas_id

    @abc.abstractmethod
    def show(self):
        pass

    def get_pos(self):
        return self.component.get_pos()

    def set_pos(self, x, y):
        self.component.set_pos(x, y)
