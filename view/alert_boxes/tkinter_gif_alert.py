import Tkinter as Tk
import tkFont
from abstract_text_alert_box import AbstractTextAlertBox


class TkinterGifAlertBox(AbstractTextAlertBox):

    def __init__(self, canvas, a_gif_path):
        """
        Creates a new instance of the class TkinterTextAlertBox
        :param font: The font of the text
        :param canvas: The canvas of the window
        """
        # type: (tkFont.Font, Tk.Canvas) -> None

        AbstractTextAlertBox.__init__(self)
        self.x = 0
        self.y = 0
        self.im_counter = 0
        self.canvas = canvas
        self.frame_num = self.get_gif_frames(a_gif_path) - 1
        self.gif = [Tk.PhotoImage(file=a_gif_path, format='gif -index %i' % (i)) for i in range(self.frame_num)]
        self.canvas_id = self.canvas.create_image(self.x, self.y, anchor=Tk.CENTER, image = self.gif[0])

    def show(self):
        self.canvas.delete(self.canvas_id)
        self.canvas_id = self.canvas.create_image(self.x, self.y, anchor=Tk.CENTER, image = self.gif[self.im_counter])

    def set_pos(self, x, y):
        """
        Sets the position of the alertbox
        :param x: a float that represents the x coordinate of the alert box
        :param y: a float that represents the y coordinate of the alert box
        """
        # type: (float, float) -> None
        self.x = x
        self.y = y

    def update_gif_frame(self):
        self.im_counter = (self.im_counter + 1) % self.frame_num
        self.show()

    def set_canvas(self, new_canvas):
        self.canvas = new_canvas

    def get_pos(self):
        return self.x, self.y

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
