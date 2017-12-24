from abstract_text_alert_box import AbstractTextAlertBox


class ConsoleAlertBox(AbstractTextAlertBox):

    def __init__(self):
        AbstractTextAlertBox.__init__(self)

    def show(self, the_middle_string):
        print(self.prefix_text + the_middle_string + self.suffix_text)
