from abstract_view import AbstractView


class ConsoleView(AbstractView):

    def __init__(self, follower_alert, subscriber_alert):
        AbstractView.__init__(self, follower_alert, subscriber_alert)

    def show_new_follower(self, new_follower):
        self.follower_alert_box.show(new_follower.get_channel())

    def show_new_subscriber(self, new_subscriber):
        self.subscriber_alert_box.show(new_subscriber.get_channel())
