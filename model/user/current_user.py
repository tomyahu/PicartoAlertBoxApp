from ..tools import jsonManager as jsonM
from ..channel.channel import Channel
from user import RegularUser


class CurrentUser:

    def __init__(self):
        """
        Creates an instace of the type Current User
        """
        # type: () -> None
        data = jsonM.get_from_url('https://api.picarto.tv/v1/user')
        self.channel = Channel(data['channel_details'])
        self.email = data['email']
        self.creation_date = data['creation_date']
        self.private_key = data['private_key']
        self.nsfw_enabled = data['nsfw_enabled']
        self.nsfw_app = data['nsfw_app']
        self.follows = list()

        for follow in data['following']:
            self.follows.append(RegularUser(follow))

        self.followers = list()

        for follower in data['followers']:
            self.followers.append(RegularUser(follower))

        self.subscriptions = list()

        for subscription in data['subscriptions']:
            self.subscriptions.append(RegularUser(subscription))

        self.subscribers = list()

        for subscriber in data['subscribers']:
            self.subscribers.append(RegularUser(subscriber))

    def get_email(self):
        return self.email

    def get_channel(self):
        return self.channel

    def get_creation_date(self):
        return self.creation_date

    def get_private_key(self):
        return self.private_key

    def is_nsfw_enabled(self):
        return self.nsfw_enabled

    def is_using_nsfw_app(self):
        return self.nsfw_app

    def get_follows(self):
        return self.follows

    def get_followers(self):
        return self.followers

    def get_subscriptions(self):
        return self.subscriptions

    def get_subscribers(self):
        return self.subscribers
