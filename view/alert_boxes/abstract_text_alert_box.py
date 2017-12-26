import abc


class AbstractTextAlertBox:

    def __init__(self):
        """
        Creates a new instance of the class AbstractTextAlertBox
        """
        # type: () -> None
        self.prefix_text = ''
        self.suffix_text = ' just followed!'

    @abc.abstractmethod
    def show(self, the_middle_string):
        """
        Shows the text in the alert box
        :param the_middle_string:
        """
        # type: str -> None
        pass

    def set_prefix_text(self, new_prefix):
        self.prefix_text = new_prefix

    def set_suffix_text(self, new_suffix):
        self.suffix_text = new_suffix
