class DescriptionPanel:

    def __init__(self, data):
        """
        Creates a new instace of type Description Panel
        :param data: The data of the Description Panel
        """
        # type: dict -> None
        self.title = data['title']
        self.body = data['body']
        self.image = data['image']
        self.image_link = data['image_link']
        self.button_text = data['button_text']
        self.button_link = data['button_link']
        self.position = data['position']

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_image_url(self):
        return self.image

    def get_image_link(self):
        return self.image_link

    def get_button_text(self):
        return self.button_text

    def get_button_link(self):
        return self.button_link

    def get_position(self):
        return self.position
