import Tkinter as Tk
import tkFont
from abstract_tkinter_canvas_object import AbstractTkinterCanvasObject
from model.components.text import Text


class TkinterCanvasText(AbstractTkinterCanvasObject):

    def __init__(self, font, canvas):
        """
        Creates a new instance of the class TkinterTextAlertBox
        :param font: The font of the text
        :param canvas: The canvas of the window
        """
        # type: (tkFont.Font, Tk.Canvas) -> None
        AbstractTkinterCanvasObject.__init__(self, canvas, Text())
        self.font = font
        self.tags = {}
        self.canvas_id = self.canvas.create_text(self.component.get_pos()[0],
                                                 self.component.get_pos()[1],
                                                 text=self.component.get_text(self.tags),
                                                 font=self.font)

    def show(self):
        self.canvas.itemconfigure(self.canvas_id, text=self.component.get_text(self.tags))
        self.canvas.itemconfigure(self.canvas_id, font=self.font)
        self.canvas.coords(self.canvas_id, self.component.get_pos()[0], self.component.get_pos()[1])

    def set_font_size(self, f_size):
        font = self.font.split(' ')
        new_font = font[0] + " " + str(f_size)
        for i in range(2, len(font)):
            new_font += " " + font[i]

        self.font = new_font

    def get_font_size(self):
        return int(self.font.split(' ')[1])

    def get_canvas_component_id(self):
        return self.canvas_id

    def add_tag(self, tag, tag_value):
        self.tags[tag] = tag_value

    def remove_tag(self, tag):
        del self.tags[tag]

    def reset_tags(self):
        self.tags = {}