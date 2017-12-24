import abc
from view.alert_boxes.abstract_text_alert_box import AbstractTextAlertBox


class AbstractView(metaclass=abc.ABCMeta):

    def __init__(self, follower_alert, subscriber_alert):
        """
        Creates a new instance of the class AbstractView
        :param follower_alert: The alert box which is going to display when a new user follows
        :param subscriber_alert: The alert box which is going to display when a new user subscribes
        """
        # type: (AbstractTextAlertBox, AbstractTextAlertBox) -> None
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
