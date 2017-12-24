import pygame
from abstract_text_alert_box import AbstractTextAlertBox


class PygameAlertBox(AbstractTextAlertBox):

    def __init__(self, screen, font, color):
        """
        Creates a new instance of the class PygameAlertBox
        :param screen: The surface in which the alert box is going to be displayed
        :param font: The font of the text of this alert box
        :param color: The color of the text of this alert box
        """
        # type: (pygame.display, pygame.font, tuple) -> None
        AbstractTextAlertBox.__init__(self)
        self.x = 0
        self.y = 0
        self.screen = screen
        self.font = font
        self.color = color

    def show(self, the_middle_string):
        screen_text = self.font.render(self.prefix_text + the_middle_string + self.suffix_text, True, self.color)
        self.screen.blit(screen_text, [self.x, self.y])

    def set_pos(self, x, y):
        """
        Sets the position of the alertbox
        :param x: a float that represents the x coordinate of the alert box
        :param y: a float that represents the y coordinate of the alert box
        """
        # type: (float, float) -> None
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y
