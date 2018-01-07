from abstract_view import AbstractAppView


class PygameAppView(AbstractAppView):

    def __init__(self, follower_alert, subscriber_alert):
        AbstractAppView.__init__(self, follower_alert, subscriber_alert)

    def show_new_follower(self, new_follower):
        self.follower_alert_box.show()

    def show_new_subscriber(self, new_subscriber):
        self.subscriber_alert_box.show()

    def run(self):
        '''
        #El notifManager deberia ser observable
        notificationManger = ThreadNotificationManager()
        
        notificationManager.addObserver(self)
        
        notificationManager.start()
        
        while( True ):
        
            while (notificationManager.not_changed())
                wait
            
            #cambiar esto a observable
            self.update(observable, notificationManager.get_info())
            broadcast(notificationManager)
        '''
        pass
