class Thumbnail:

    def __init__(self, data):
        """
        Creates a new instance of type Thumbnail
        :param data: The data of the Thumbnail
        """
        # type: dict -> None
        self.web = data['web']
        self.web_large = data['web_large']
        self.mobile = data['mobile']
        self.tablet = data['tablet']

    def get_web_url(self):
        return self.web

    def get_web_large_url(self):
        return self.web_large

    def get_mobile_url(self):
        return self.mobile

    def get_tablet_url(self):
        return self.tablet
