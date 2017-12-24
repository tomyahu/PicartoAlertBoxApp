class Languaje:

    def __init__(self, data):
        """
        Creates a new instance of type Languaje
        :param data: The data of the Languaje
        """
        # type: dict -> None
        self.id = data['id']
        self.country = data['name']

    def get_id(self):
        return self.id

    def get_country(self):
        return self.country
