import Tkinter as Tk
from constants.settings import canvas_height,canvas_width
from .components.layer import Layer
from .tkinter_text_options import TkinterTextOptions
from functools import partial


class TkinterConfigurationView:

    def __init__(self, root):
        self.root = root
        self.canvas = Tk.Canvas(self.root, width=canvas_width, height=canvas_height)
        self.layer_list = Tk.Listbox(self.root)
        self.layers = []

    def show(self):
        # Canvas
        self.canvas.grid(row=0, rowspan=5)

        # Layers
        Tk.Label(self.root, text="Layers").grid(row=0, column = 1)
        self.layer_list.grid(row = 1, column = 1, ipady= 125)
        self.show_add_layer_buttons()
        self.show_current_layer_options()
        self.canvas.bind("<B1-Motion>", self.move_current_layer_object)

    def show_add_layer_buttons(self):

        button_text = Tk.Button(self.root,
                                text="Add Text",
                                command=lambda:self.add_text_layer())

        button_image = Tk.Button(self.root,
                                 text="Add Image",
                                 command=add_image_layer)

        button_gif = Tk.Button(self.root,
                               text="Add Gif",
                               command=add_image_layer)

        button_text.grid(row=2, column=1, sticky=Tk.S, ipadx=30)
        button_image.grid(row=3, column=1, sticky=Tk.S, ipadx=24)
        button_gif.grid(row=4, column=1, sticky=Tk.S, ipadx=33)

    def show_current_layer_options(self):
        layer_pos = self.layer_list.curselection()

        if (len(layer_pos) > 0):
            self.layers[layer_pos[0]].show_config_view()

        self.root.after(10, lambda:self.show_current_layer_options())

    def move_current_layer_object(self, event):
        layer_pos = self.layer_list.curselection()

        if (len(layer_pos) > 0):
            self.layers[layer_pos[0]].get_object_options().move_object(event)

    def add_text_layer(self):
        self.layers += [Layer(TkinterTextOptions(self.root, self.canvas), self.root, "Text Layer " + str(len(self.layers)))]
        self.layer_list.insert(len(self.layers) - 1, self.layers[len(self.layers) - 1].get_name())

    def rename_layer(self, new_name):
        layer_pos = self.layer_list.curselection()
        self.layers[layer_pos[0]].rename(new_name)
        self.layer_list.insert(layer_pos, new_name)

def add_image_layer(configuration_view):
    pass

def add_gif_layer(configuration_view):
    pass
