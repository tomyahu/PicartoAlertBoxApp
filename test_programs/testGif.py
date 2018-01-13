import Tkinter as tk
from constants.settings import canvas_height,canvas_width
from view.configuration_views.components.canvas_objects.tkinter_canvas_gif import TkinterCanvasGif


root = tk.Tk()
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=0)

img_obj = TkinterCanvasGif(canvas, "cool-transparent-gif-333.gif")

current_object_id = img_obj.get_canvas_component_id()

def move_thing(event):
    img_obj.set_pos(event.x, event.y)

def update_gif():
    img_obj.show()
    root.after(10, update_gif)


canvas.bind("<B1-Motion>", move_thing)
root.after(0, update_gif)
tk.mainloop()