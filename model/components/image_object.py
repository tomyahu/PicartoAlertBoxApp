from abstract_object import AbstractObject


class ImageObject(AbstractObject):

    def __init__(self, path):
        AbstractObject.__init__(self)
        self.path = path

    def get_path(self):
        return self.path

    def image_type(self):
        split_path = self.path.split('.')
        return split_path[len(split_path) - 1]
