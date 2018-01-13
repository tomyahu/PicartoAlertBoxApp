import Tkinter as Tk
from tkFileDialog import askopenfilename
from constants.settings import canvas_height,canvas_width
from .components.layer import Layer
from .components.LayerLists.ListBoxLayerList import ListBoxLayerList

from .tkinter_text_options import TkinterTextOptions
from .tkinter_image_options import TkinterImageOptions
from .tkinter_gif_options import TkinterGifOptions

class TkinterConfigurationView:

    def __init__(self, root):
        self.root = root
        self.canvas = Tk.Canvas(self.root, width=canvas_width, height=canvas_height)
        self.layer_list = ListBoxLayerList(root)
        self.layers = []

    def show(self):
        # Canvas
        self.canvas.grid(row=0, rowspan=5, columnspan=4)

        # Layers
        Tk.Label(self.root, text="Layers").grid(row=0, column = 4)
        self.layer_list.grid(row = 1, column = 4, ipady= 125)
        self.show_add_layer_buttons()
        self.show_current_layer_options()
        self.canvas.bind("<B1-Motion>", self.move_current_layer_object)
        self.update_components()

    def show_add_layer_buttons(self):

        button_text = Tk.Button(self.root,
                                text="Add Text",
                                command=lambda:self.add_text_layer())

        button_image = Tk.Button(self.root,
                                 text="Add Image",
                                 command=lambda:self.add_image_layer())

        button_gif = Tk.Button(self.root,
                               text="Add Gif",
                               command=lambda:self.add_gif_layer())

        button_text.grid(row=2, column=4, sticky=Tk.S, ipadx=30)
        button_image.grid(row=3, column=4, sticky=Tk.S, ipadx=24)
        button_gif.grid(row=4, column=4, sticky=Tk.S, ipadx=33)

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

    def add_image_layer(self):
        file_types = [
            ("Image Files", (
            "*.bmp", "*.dib", "*.gif", "*.jpg", "*.jpe", "*.jpeg", "*.pdf", "*.pgm", "*.png", "*.tif", "*.tiff",
            "*.xbm", "*.xpm"))
        ]
        path = askopenfilename(filetypes=file_types)
        if path:
            self.layers += [Layer(TkinterImageOptions(self.root, self.canvas, path), self.root, "Image Layer " + str(len(self.layers)))]
            self.layer_list.insert(len(self.layers) - 1, self.layers[len(self.layers) - 1].get_name())

    def add_gif_layer(self):
        file_types = [
            ("GIF", "*.gif")
        ]
        path = askopenfilename(filetypes=file_types)
        if path:
            self.layers += [Layer(TkinterGifOptions(self.root, self.canvas, path), self.root, "Gif Layer " + str(len(self.layers)))]
            self.layer_list.insert(len(self.layers) - 1, self.layers[len(self.layers) - 1].get_name())

    def rename_layer(self, new_name):
        layer_pos = self.layer_list.curselection()
        self.layers[layer_pos[0]].rename(new_name)
        self.layer_list.insert(layer_pos, new_name)

    def update_components(self):

        if(len(self.layer_list.curselection()) > 0):
            layer_pos = self.layer_list.curselection()[0]
            self.layers[layer_pos].update()
            self.layers[layer_pos].select()

        self.root.after(10, lambda: self.update_components())
