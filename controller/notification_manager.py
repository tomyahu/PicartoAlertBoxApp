from model.user.notifications.notification_funtions import *
from model.tools.jsonManager import get_from_file, write_on_file

notification_path = './notifications'


class NotificationManager:

    def __init__(self):
        """
        Creates a new instance of the clas NotificationManager
        """
        # type: () -> None
        self.follows = []
        self.subs = []

    @staticmethod
    def get_past_notifications():
        """
        Returns a dictionary with the past notifications
        :return: A dictionary with the past notifications
        """
        # type: () -> dict()
        return get_from_file(notification_path)

    def update_notification_file(self):
        """
        Updates the notification file.
        """
        # type: () -> None
        data = self.get_past_notifications()
        data['followers'] += self.follows
        data['subscribers'] += self.subs

        write_on_file(data, notification_path)

    def check_notifications(self):
        """
        Check the user's notifications from the internet
        """
        # type: () -> None
        data = get_notifications()
        self.follows = filter_notifications_by_type(data, 'follow')
        self.subs = filter_notifications_by_type(data, 'subscribe')

        self.eliminate_repeated_follows()
        self.eliminate_repeated_subscribers()

    def eliminate_repeated_follows(self):
        """
        Eliminates the followers stored in the notification file from self.follows
        """
        # type: () -> None
        data = self.get_past_notifications()
        new_follows = []

        boolean = True
        for follow in self.follows:
            for past_follow in data['followers']:
                boolean = boolean and (follow.get_channel() != past_follow['channel'])
            if boolean:
                new_follows.append(follow)

        self.follows = new_follows

    def eliminate_repeated_subscribers(self):
        """
        Eliminates the subscribers stored in the notification file from self.subs
        """
        # type: () -> None
        data = self.get_past_notifications()
        new_subs = []

        boolean = True
        for sub in self.subs:
            for past_sub in data['subscribers']:
                boolean = boolean and (sub.get_channel() != past_sub['channel'])
            if boolean:
                new_subs.append(sub)

        self.subs = new_subs

    def has_followers_left(self):
        # type: () -> bool
        return len(self.follows) != 0

    def has_subscribers_left(self):
        # type: () -> bool
        return len(self.subs) != 0

    def add_follower_to_file(self):
        """
        Adds the last follower of self.follows to the file and returns it
        :return: The last follower of self.follows
        """
        # type: () -> dict()
        the_follower = self.follows[len(self.follows) - 1]
        self.follows = self.follows[:len(self.follows) - 1]

        data = self.get_past_notifications()
        data['followers'].append(the_follower.get_dictionary())

        write_on_file(data, notification_path)

        return the_follower

    def add_subscriber_to_file(self):
        """
        Adds the last suscriber of self.subs to the file and returns it
        :return: The last suscriber of self.subs
        """
        # type: () -> dict()
        the_subscriber = self.subs[len(self.subs) - 1]
        self.subs = self.subs[:len(self.subs) - 1]

        data = self.get_past_notifications()
        data['subscribers'].append(the_subscriber.get_dictionary())

        write_on_file(data, notification_path)

        return the_subscriber

    @staticmethod
    def empty_notification_file():
        """
        Cleans the notification file
        """
        # type: () -> None
        empty_array = []
        data = dict()

        data['followers'] = empty_array
        data['subscribers'] = empty_array

        write_on_file(data, notification_path)
