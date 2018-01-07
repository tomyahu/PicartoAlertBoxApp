from abstract_object import AbstractObject


class Image(AbstractObject):

    def __init__(self, path):
        AbstractObject.__init__(self)
        self.path = path

    def get_path(self):
        return self.path
