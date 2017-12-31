import Tkinter as Tk
import tkFont
from abstract_tkinter_canvas_object import AbstractTkinterCanvasObject

fps = 24

class TkinterCanvasGif(AbstractTkinterCanvasObject):

    def __init__(self, canvas, a_gif_path):
        AbstractTkinterCanvasObject.__init__(self,canvas)

        self.im_counter = 0
        self.frame_num = self.get_gif_frames(a_gif_path) - 1
        self.time = 0

        self.gif = [Tk.PhotoImage(file=a_gif_path, format='gif -index %i' % (i)) for i in range(self.frame_num)]
        self.canvas_id = self.canvas.create_image(self.x, self.y, anchor=Tk.CENTER, image=self.gif[self.im_counter])

    def show(self):
        self.update_gif_frame()
        self.canvas.delete(self.canvas_id)
        self.canvas_id = self.canvas.create_image(self.x, self.y, anchor=Tk.CENTER, image=self.gif[self.im_counter])

    def update_gif_frame(self):
        self.time = (self.time + fps) % 100
        if self.time < fps:
            self.im_counter = (self.im_counter + 1) % self.frame_num

    def get_gif_frames(self, path):
        k = 0
        while True:
            try:
                [Tk.PhotoImage(file=path, format='gif -index %i' % (i)) for i in range(k)]
                k+=1
            except Tk.TclError:
                return k

    def get_canvas_component_id(self):
        return self.canvas_id
