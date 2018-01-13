import Tkinter as Tk
import tkFont
from abstract_tkinter_canvas_object import AbstractTkinterCanvasObject
from model.components.gif_object import GifObject


class TkinterCanvasGif(AbstractTkinterCanvasObject):

    def __init__(self, canvas, a_gif_path):
        AbstractTkinterCanvasObject.__init__(self, canvas, GifObject(a_gif_path))

        self.im_counter = 0
        self.frame_num = self.get_gif_frames() - 1
        self.time = 0

        self.tkinter_gif = [Tk.PhotoImage(file=self.component.get_path(),
                                          format='gif -index %i' % (i)) for i in range(self.frame_num)]

        self.canvas_id = self.canvas.create_image(self.component.get_pos()[0],
                                                  self.component.get_pos()[1],
                                                  anchor=Tk.CENTER,
                                                  image=self.tkinter_gif[self.im_counter])

    def show(self):
        self.update_gif_frame()
        self.canvas.itemconfigure(self.canvas_id, image=self.tkinter_gif[self.im_counter])
        self.canvas.coords(self.canvas_id, self.component.get_pos()[0], self.component.get_pos()[1])

    def update_gif_frame(self):
        self.time = (self.time + self.component.get_fps()) % 100
        if self.time < self.component.get_fps():
            self.im_counter = (self.im_counter + 1) % self.frame_num

    def get_gif_frames(self):
        return self.component.get_frames()

    def get_canvas_component_id(self):
        return self.canvas_id
