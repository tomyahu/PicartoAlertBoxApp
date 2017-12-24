from input.input_manager import InputManager
from notification_manager import NotificationManager
from view.abstract_view import AbstractView


class AppController:

    def __init__(self, a_view):
        """
        Creates a new instance of an App controller
        :param a_view:
        """
        # type: AbstractView -> None
        self.input_managers = list()
        self.notification_manager = NotificationManager()
        self.view = a_view

    def add_input_manager(self, an_input_manager):
        """
        Adds an input manager to the list of input managers
        :param an_input_manager:
        """
        # type: InputManager -> None
        self.input_managers.append(an_input_manager)

    def update_notifications(self):
        """
        Updates the current notifications
        """
        # type: () -> None
        self.notification_manager.check_notifications()

    def has_new_followers(self):
        """
        Returns True if the user has new followers and False if not
        :return: True if the user has new followers and False if not
        """
        # type: () -> bool
        return self.notification_manager.has_followers_left()

    def has_new_subscribers(self):
        """
        Returns True if the user has new subscribers and False if not
        :return: True if the user has new subscribers and False if not
        """
        # type: () -> bool
        return self.notification_manager.has_subscribers_left()

    def show_follower_alert_box(self):
        """
        Shows the follower alert box.
        """
        # type: () -> None
        try:
            new_follower = self.notification_manager.add_follower_to_file()
            self.view.show_new_follower(new_follower)
        except IndexError:
            print('There is no new follower to show.')

    def show_subscriber_alert_box(self):
        """
        Shows the follower alert box.
        """
        # type: () -> None
        try:
            new_subscriber = self.notification_manager.add_subscriber_to_file()
            self.view.show_new_subscriber(new_subscriber)
        except IndexError:
            print('There is no new subscriber to show.')
