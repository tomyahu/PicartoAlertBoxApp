import Tkinter as Tk
import tkFont
from abstract_tkinter_canvas_object import AbstractTkinterCanvasObject
from model.components.image import Image


class TkinterCanvasImage(AbstractTkinterCanvasObject):

    def __init__(self, canvas, an_image_path):
        """
        Creates a new instance of TkinterCanvasImage
        :param canvas: The canvas in which to display the image
        :param an_image_path: The path of the image
        """
        # type: (Tk.Canvas, str) -> None
        AbstractTkinterCanvasObject.__init__(self, canvas, Image(an_image_path))
        self.image = Tk.PhotoImage(file=an_image_path)

        self.canvas_id = self.canvas.create_image(self.component.get_pos()[0], self.component.get_pos()[1], anchor=Tk.CENTER, image = self.image)

    def show(self):
        self.canvas.coords(self.canvas_id, self.component.get_pos()[0], self.component.get_pos()[1])

    def get_canvas_component_id(self):
        return self.canvas_id
