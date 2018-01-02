class ConsoleAlerts():

    def __init__(self):
        self.prefix = ''
        self.suffix = ' just followed!!'

    def set_suffix_text(self, some_text):
        self.suffix = some_text

    def show(self, name):
        print(self.prefix + name + self.suffix)
