from view.configuration_views.components.canvas_objects.tkinter_canvas_image import TkinterCanvasImage
from .tkinter_abstract_obj_options import TkinterAbstractObjectOptions
import Tkinter as Tk


class TkinterImageOptions(TkinterAbstractObjectOptions):

    def __init__(self, root, canvas, path):
        # type: (Tk.Tk, Tk.Canvas) -> None
        TkinterAbstractObjectOptions.__init__(self, root, canvas, TkinterCanvasImage(canvas, path))

    def show(self):
        Tk.Label(self.root, text="X: " + str(self.canvas_obj.get_pos()[0])).grid(row=5, column=0)
        Tk.Label(self.root, text="Y: " + str(self.canvas_obj.get_pos()[1])).grid(row=6, column=0)
