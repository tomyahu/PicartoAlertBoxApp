from constants.settings import canvas_width,canvas_height


class AbstractObject:

    def __init__(self):
        self.x = canvas_width/2
        self.y = canvas_height/2

    def get_pos(self):
        return self.x, self.y

    def set_pos(self, x, y):
        """
        Sets the position of the alertbox
        :param x: a float that represents the x coordinate of the alert box
        :param y: a float that represents the y coordinate of the alert box
        """
        # type: (float, float) -> None
        self.x = x
        self.y = y