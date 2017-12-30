import Tkinter as Tk
import tkFont
from abstract_tkinter_canvas_object import AbstractTkinterCanvasObject


class TkinterCanvasText(AbstractTkinterCanvasObject):

    def __init__(self, font, canvas):
        """
        Creates a new instance of the class TkinterTextAlertBox
        :param font: The font of the text
        :param canvas: The canvas of the window
        """
        # type: (tkFont.Font, Tk.Canvas) -> None
        AbstractTkinterCanvasObject.__init__(self, canvas)
        self.text = '(name) just followed!'
        self.font = font
        self.canvas_id = self.canvas.create_text(self.x, self.y, text=self.text, font=font)

    def show(self, name):
        self.canvas.delete(self.canvas_id)
        complete_text = self.set_tag(self.text, 'name', name)
        self.canvas_id = self.canvas.create_text(self.x,
                                                 self.y, text=complete_text, font=self.font)

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

    def set_tag(self, text, tag, tag_value):
        text_parts = text.split('('+ tag +')')
        new_text = text_parts[0]

        for i in range(1, len(text_parts)):
            new_text += tag_value
            new_text += text_parts[i]

        return new_text
