from .abstract_object import AbstractObject


class TextObject(AbstractObject):
    """
    An object that represents Text
    """

    def __init__(self):
        """
        Creates a new instance of a Text Object
        """
        # type: () -> None
        AbstractObject.__init__(self)
        self.content = "{name} just followed!!"

    def get_text(self, tags):
        """
        Returns the text with the corresponding tags changed for their values
        :param tags: A dictionary with the tags to replace
        :return: A string with the text with the corresponding tags changed for their values
        """
        # type: dict -> str
        final_text = self.content

        for key in tags.keys():
            split_content = content.split(key)
            final_text = split_content[0]

            for i in range(1, len(split_content)):
                final_text += tags[key]
                final_text += split_content[i]

        return final_text

    def set_text(self, text):
        # type: (str) -> None
        self.content = text
