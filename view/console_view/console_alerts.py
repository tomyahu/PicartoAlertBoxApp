from view.configuration_views.components.canvas_objects.abstract_tkinter_canvas_object import AbstractTkinterCanvasObject


class ConsoleAlerts():

    def __init__(self):
        self.prefix = ''
        self.suffix = ' just followed!!'

    def show(self, name):
        print(self.prefix + name + self.suffix)
