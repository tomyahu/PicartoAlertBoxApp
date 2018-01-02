import abc
import pygame


pygame.init()

# Pygame input sources
mouse = pygame.mouse


class InputManager():

    def __init__(self):
        pass

    @abc.abstractmethod
    def check_input(self):
        pass

    @abc.abstractmethod
    def do_action(self, controller):
        pass


class LeftMouseInputManager(InputManager):

    def __init__(self):
        InputManager.__init__(self)

    def check_input(self):
        return mouse.get_pressed()[0]

    def do_action(self, controller):
        pass
