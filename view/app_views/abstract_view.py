import abc
from view.configuration_views.components.canvas_objects.abstract_tkinter_canvas_object import AbstractTkinterCanvasObject
from model.observer_pattern.thread_observe import ThreadObserver


class AbstractAppView(ThreadObserver):

    def __init__(self, follower_alert, subscriber_alert):
        ThreadObserver.__init__(self)
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
