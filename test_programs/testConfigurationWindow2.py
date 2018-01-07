import Tkinter as tk
from constants.settings import canvas_height,canvas_width
from view.configuration_views.tkinter_configuration_view import TkinterConfigurationView

root = tk.Tk()
root.title("AlertBox App")

view = TkinterConfigurationView(root)
view.show()

root.mainloop()
