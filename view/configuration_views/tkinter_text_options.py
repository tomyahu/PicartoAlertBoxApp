from view.configuration_views.components.canvas_objects.tkinter_canvas_text import TkinterCanvasText
from constants.fonts import *
from .tkinter_abstract_obj_options import TkinterAbstractObjectOptions
import Tkinter as Tk


class TkinterTextOptions(TkinterAbstractObjectOptions):

    def __init__(self, root, canvas):
        # type: (Tk.Tk, Tk.Canvas) -> None
        TkinterAbstractObjectOptions.__init__(self, root, canvas, TkinterCanvasText(helv, canvas))

    def show(self):
        self.update_position_options()

    def set_font(self, new_font):
        self.canvas_obj.set_font(new_font)

    def get_font(self):
        return self.canvas_obj.get_font()

    def set_font_size(self, new_size):
        self.canvas_obj.set_font_size(new_size)

    def get_font_size(self):
        return self.canvas_obj.get_font_size()
