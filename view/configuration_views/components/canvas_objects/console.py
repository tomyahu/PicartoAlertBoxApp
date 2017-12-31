from abstract_tkinter_canvas_object import AbstractTkinterCanvasObject


class ConsoleAlertBox(AbstractTkinterCanvasObject):

    def __init__(self):
        AbstractTkinterCanvasObject.__init__(self)

    def show(self, name):
        print(self.prefix_text + name + self.suffix_text)
