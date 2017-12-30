import abc


class AbstractTkinterCanvasObject:

    def __init__(self, canvas):
        """
        Creates a new instance of the class AbstractTextAlertBox
        """
        # type: () -> None
        self.x = 0
        self.y = 0
        self.canvas = canvas

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