from model.observer_pattern.thread_observe import Observable
from notification_manager import NotificationManager
from view.app_views.app_view import AbstractAppView


class NotificationComunicator(Observable):

    def __init__(self, notification_manager):
        # type: (NotificationManager) -> None
        self.notification_manager = notification_manager

    def run(self):

        view_thread = AbstractAppView()

        while True:
            self.notification_manager.check_notifications()

            if self.notification_manager.has_followers_left():
                the_follower = self.notification_manager.add_follower_to_file()

