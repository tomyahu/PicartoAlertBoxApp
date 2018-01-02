from view.app_views.abstract_view import AbstractAppView


class ConsoleAppView(AbstractAppView):

    def __init__(self, follower_alert, subscriber_alert):
        AbstractAppView.__init__(self, follower_alert, subscriber_alert)

    def show_new_follower(self, new_follower):
        self.follower_alert_box.show(new_follower.get_channel())

    def show_new_subscriber(self, new_subscriber):
        self.subscriber_alert_box.show(new_subscriber.get_channel())
