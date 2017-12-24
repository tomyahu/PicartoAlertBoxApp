class AbstractUser:

    def __init__(self, data):
        """
        Creates a new instance of type AbstractUser
        :param data: The data of the User
        """
        # type: dict -> None
        self.id = data['user_id']
        self.name = data['name']
        self.online = data['online']

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def is_online(self):
        return self.online


class RegularUser(AbstractUser):

    def __init__(self, data):
        """
        Creates a new instance of type RegularUser
        :param data: The data of the RegularUser
        """
        # type: dict -> None
        AbstractUser.__init__(self, data)
        self.avatar_url = data['avatar']

    def get_avatar_url(self):
        return self.avatar_url


class MultistreamUser(AbstractUser):

    def __init__(self, data):
        """
        Creates a new instance of type MultistreamUser
        :param data: The data of the MultistreamUser
        """
        # type: dict -> None
        AbstractUser.__init__(self, data)
        self.adult = data['adult']

    def is_adult(self):
        return self.adult
