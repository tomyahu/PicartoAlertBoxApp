from canvas_objects import *

class Layer:

    def __init__(self, configuration_view, root):
        self.config_view = configuration_view
        self.root = root

    def show_config_view(self):
        self.config_view.show()
