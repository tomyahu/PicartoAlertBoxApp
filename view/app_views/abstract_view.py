import abc
from view.configuration_views.components.canvas_objects.abstract_tkinter_canvas_object import AbstractTkinterCanvasObject


class AbstractAppView():

    def __init__(self, follower_alert, subscriber_alert):
        """
        Creates a new instance of the class AbstractView
        :param follower_alert: The alert box which is going to display when a new user follows
        :param subscriber_alert: The alert box which is going to display when a new user subscribes
        """
        # type: (AbstractTkinterCanvasObject, AbstractTkinterCanvasObject) -> None
        self.follower_alert_box = follower_alert
        self.subscriber_alert_box = subscriber_alert

    @abc.abstractmethod
    def show_new_follower(self, new_follower):
        """
        Displays the new follower alert box on screen.
        :param new_follower: The new follower
        """
        # type: (dict()) -> object
        pass

    @abc.abstractmethod
    def show_new_subscriber(self, new_subscriber):
        """
        Displays the new subscriber alert box on screen.
        :param new_subscriber: The new subscriber
        """
        # type: (dict()) -> object
        pass

    def get_follower_alert_box(self):
        return self.follower_alert_box

    def get_subscriber_alert_box(self):
        return self.subscriber_alert_box
