import Tkinter as Tk
import tkFont
from abstract_text_alert_box import AbstractTextAlertBox


class TkinterImageAlertBox(AbstractTextAlertBox):

    def __init__(self, canvas, an_image):
        """
        Creates a new instance of the class TkinterTextAlertBox
        :param font: The font of the text
        :param canvas: The canvas of the window
        """
        # type: (tkFont.Font, Tk.Canvas) -> None

        AbstractTextAlertBox.__init__(self)
        self.x = 0
        self.y = 0
        self.canvas = canvas
        self.image = an_image
        self.canvas_id = self.canvas.create_image(self.x, self.y, anchor=Tk.CENTER, image = an_image)

    def show(self):
        self.canvas.delete(self.canvas_id)
        self.canvas_id = self.canvas.create_image(self.x, self.y, anchor=Tk.CENTER, image = self.image)

    def set_pos(self, x, y):
        """
        Sets the position of the alertbox
        :param x: a float that represents the x coordinate of the alert box
        :param y: a float that represents the y coordinate of the alert box
        """
        # type: (float, float) -> None
        self.x = x
        self.y = y

    def set_canvas(self, new_canvas):
        self.canvas = new_canvas

    def get_pos(self):
        return self.x, self.y

    def get_canvas_component_id(self):
        return self.canvas_id
