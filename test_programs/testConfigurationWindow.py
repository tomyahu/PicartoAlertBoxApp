import Tkinter as tk
from constants.settings import canvas_height,canvas_width

test_user = 'test123'

def add_text_layer():
    pass

def add_image_layer():
    pass

def add_gif_layer():
    pass

root = tk.Tk()
root.title("New AlertBox")

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=0, rowspan=5)

layer_label = tk.Label(root, text="Layers")
layer_label.grid(row=0, column = 1)

listbox = tk.Listbox(root)
listbox.grid(row = 1, column = 1, ipady= 125)

button_text = tk.Button(root,
                   text="Add Text",
                   command=add_text_layer)
button_image = tk.Button(root,
                   text="Add Image",
                   command=add_image_layer)
button_gif = tk.Button(root,
                   text="Add Gif",
                   command=add_image_layer)

button_text.grid(row=2, column = 1, sticky = tk.S, ipadx=30)
button_image.grid(row=3, column = 1, sticky = tk.S, ipadx=24)
button_gif.grid(row=4, column = 1, sticky = tk.S, ipadx=33)


root.mainloop()
