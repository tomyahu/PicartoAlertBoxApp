class Notification:

    def __init__(self, data):
        """
        Creates a new instance of the type Notification
        :param data: The data of the Notification
        """
        # type: dict -> None
        self.data = data
        self.channel = data['channel']
        self.type = data['type']
        self.read = not data['unread']
        self.url = data['uri']
        self.icon = data['hasIcon']

    def get_channel(self):
        return self.channel

    def get_type(self):
        return self.type

    def get_url(self):
        return self.url

    def is_read(self):
        return self.read

    def get_dictionary(self):
        return self.data

    def has_icon(self):
        return self.icon

    def __eq__(self, other):
        """
        Checks if two notifications are the same
        :param other: The notification to compare to
        :return: True if the Notifications are the same and False if not
        """
        # type: Notification -> Notification
        same_channel = self.get_channel() == other.get_channel()
        same_type = self.get_type() == other.get_type()
        return same_channel and same_type
