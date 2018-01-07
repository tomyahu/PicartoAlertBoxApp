import Tkinter as tk # Python 2
import time
from math import sin

class counter:

    def __init__(self):
        self.counter = 0

    def get_counter(self):
        self.counter+=1
        return self.counter

root = tk.Tk()
# The image must be stored to Tk or it will be garbage collected.
root.image = [tk.PhotoImage(file='cool-transparent-gif-333.gif',format = 'gif -index %i' %(i)) for i in range(9)]

c = counter()

def update(ind):
    frame = root.image[ind]
    ind = (ind + 1)%9
    label.configure(image=frame)
    root.after(100, update, ind)


label = tk.Label(root, image=root.image[7], bg='white')
root.geometry("+250+250")


root.wm_attributes("-transparentcolor", "white")
label.pack()
root.after(0, update, 0)
label.mainloop()