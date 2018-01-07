import Tkinter as tk
from constants.settings import canvas_height,canvas_width
from constants.fonts import *
from view.configuration_views.components.canvas_objects.tkinter_canvas_text import TkinterCanvasText

current_person = 'test123'

root = tk.Tk()
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=0)

text_obj = TkinterCanvasText(helv, canvas)

def move_thing(event):
    text_obj.set_pos(event.x, event.y)

def update_text():
    text_obj.show()
    root.after(10, update_text)

canvas.bind("<B1-Motion>", move_thing)
root.after(0, update_text)
tk.mainloop()