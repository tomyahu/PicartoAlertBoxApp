from controller.app_controller import AppController
from view.console_view import ConsoleView
from view.alert_boxes.console import ConsoleAlertBox

follower_alert = ConsoleAlertBox()

subscriber_alert = ConsoleAlertBox()
subscriber_alert.set_suffix_text(' just subscribed!')

view = ConsoleView(follower_alert, subscriber_alert)

ctrl = AppController(view)

while True:

    ctrl.update_notifications()

    if(ctrl.has_new_followers()):
        ctrl.show_follower_alert_box()

    if(ctrl.has_new_subscribers()):
        ctrl.show_subscriber_alert_box()