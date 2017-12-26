import Tkinter as Tk
import tkFont
from abstract_text_alert_box import AbstractTextAlertBox


class TkinterTextAlertBox(AbstractTextAlertBox):

    def __init__(self, font, canvas):
        """
        Creates a new instance of the class TkinterTextAlertBox
        :param font: The font of the text
        :param canvas: The canvas of the window
        """
        # type: (tkFont.Font, Tk.Canvas) -> None

        AbstractTextAlertBox.__init__(self)
        self.x = 0
        self.y = 0
        self.font = font
        self.canvas = canvas
        self.canvas_id = self.canvas.create_text(self.x, self.y, text=(self.prefix_text + self.suffix_text), font=font)

    def show(self, the_middle_string):
        self.canvas.delete(self.canvas_id)
        self.canvas_id = self.canvas.create_text(self.x,
            self.y, text=(self.prefix_text + the_middle_string + self.suffix_text), font=self.font)

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

    def set_font_size(self, f_size):
        font = self.font.split(' ')
        new_font = font[0] + " " + str(f_size)
        for attr in range(2, len(font)):
            new_font += " " + attr

        self.font = new_font

    def get_font_size(self):
        return int(self.font.split(' ')[1])

    def get_pos(self):
        return self.x, self.y

    def get_canvas_component_id(self):
        return self.canvas_id
