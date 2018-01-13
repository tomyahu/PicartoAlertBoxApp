from abstract_object import AbstractObject
import Tkinter as Tk


class GifObject(AbstractObject):

    def __init__(self, path):
        AbstractObject.__init__(self)
        self.path = path
        self.fps = 24

    def set_fps(self, new_fps):
        self.fps = new_fps

    def get_fps(self):
        return self.fps

    def get_path(self):
        return self.path

    def get_frames(self):
        k = 0
        while True:
            try:
                [Tk.PhotoImage(file=self.path, format='gif -index %i' % (i)) for i in range(k)]
                k+=1
            except Tk.TclError:
                return k
