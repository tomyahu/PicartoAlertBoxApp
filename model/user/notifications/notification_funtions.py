from notifications import Notification
from model.tools import jsonManager as jsonM


def get_notifications():
    """
    Gets the list of notifications of the current user
    :return: The list of notifications of the current user
    """
    # type: () -> list()
    notifications = list()
    data = jsonM.get_from_url('https://api.picarto.tv/v1/user/notifications')

    if data is not None:
        for notification in data:
            notifications.append(Notification(notification))

    return notifications


def filter_notifications_by_type(notification_list, a_type):
    """
    Returns a list with the notifications of the list notification_list filtered by the type a_type
    :param notification_list: A list of notifications
    :param a_type: A string to filter
    :return: A list with the notifications of the list notification_list filtered by the type a_type
    """
    # type: (list(), str) -> list()
    new_notifications = list()

    for notification in notification_list:
        if notification.get_type() == a_type:
            new_notifications.append(notification)

    return new_notifications
