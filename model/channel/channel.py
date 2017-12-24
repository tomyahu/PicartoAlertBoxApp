from ..tools import jsonManager as jsonM
from components.descriptionPanel import DescriptionPanel
from components.languaje import Languaje
from components.thumbnail import Thumbnail
from ..user.user import MultistreamUser
from ..tools.constants import preurl


class Channel:

    def __init__(self, data):
        """
        Creates a new instance of a channel
        :param data: The data of the channel
        """
        # type: dict -> None
        self.name = data['name']
        self.user_id = data['user_id']
        self.avatar = data['avatar']
        self.online = data['online']
        self.viewers = data['viewers']
        self.total_views = data['viewers_total']
        self.thumbnails = Thumbnail(data['thumbnails'])

        self.followers = data['followers']
        self.subscribers = data['subscribers']
        self.adult = data['adult']
        self.category = data['category']
        self.account_type = data['account_type']
        self.commissions = data['commissions']
        self.title = data['title']
        self.description_panels = list()

        for panel in data['description_panels']:
            self.description_panels.append(DescriptionPanel(panel))

        self.private = data['private']
        self.gaming = data['gaming']
        self.guestChat = data['guest_chat']
        self.last_live = data['last_live']
        self.tags = list()

        for tag in data['tags']:
            self.tags.append(tag)

        self.multistream = list()

        for user in data['multistream']:
            self.multistream.append(MultistreamUser(user))

        self.languajes = list()

        for languaje in data['languajes']:
            self.languajes.append(Languaje(languaje))

    # Getters
    def get_name(self):
        return self.name

    def get_id(self):
        return self.user_id

    def get_viewer_amount(self):
        return self.viewers

    def get_total_views(self):
        return self.total_views

    def follower_number(self):
        return self.followers

    def get_subscribers(self):
        return self.subscribers

    def get_title(self):
        return self.title

    def get_category(self):
        return self.category

    def get_tags(self):
        return self.tags

    def get_languajes(self):
        return self.languajes

    def get_account_type(self):
        return self.account_type

    def get_description_panels(self):
        return self.description_panels

    def get_multistream_users(self):
        return self.multistream

    def is_online(self):
        return self.online

    def is_adult(self):
        return self.adult

    def is_acepting_commissions(self):
        return self.commissions

    def is_private(self):
        return self.private

    def is_gaming(self):
        return self.gaming

    def can_guests_chat(self):
        return self.guestChat


def get_channel_from_id(user_id):
    """
    Creates a channel object from a given id
    :param user_id: The id of the channel
    :return: The channel corresponding to the id
    """
    # type: int -> Channel
    data = jsonM.get_from_url(preurl + '/channel/id/' + str(user_id))
    return Channel(data)


def get_channel_from_name(name):
    """
    Creates a channel object from a given name
    :param name: The name of the user's channel
    :return: The Channle corresponding to the name given
    """
    # type: str -> Channel
    data = jsonM.get_from_url(preurl + '/channel/name/' + name)
    return Channel(data)
