from abstract_view import AbstractView


class PygameView(AbstractView):

    def __init__(self, follower_alert, subscriber_alert):
        AbstractView.__init__(self, follower_alert, subscriber_alert)

    def show_new_follower(self, new_follower):
        self.follower_alert_box.show()

    def show_new_subscriber(self, new_subscriber):
        self.subscriber_alert_box.show()
