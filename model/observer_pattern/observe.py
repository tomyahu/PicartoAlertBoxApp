import abc


class Observable:

    def __init__(self):
        """
        Creates a new instance of Observer
        """
        # type: () -> None
        self.observers = []
        self.changed = False

    def add_observer(self, observer):
        # type: (Observer) -> None
        """
        Adds an observer to the list
        :param observer: The observer to be added to the list
        """
        self.observers.append(observer)

    def delete_observer(self, observer):
        """
        Deletes an observer from the list
        :param observer: The observer to be deleted from the list
        """
        # type: (Observer) -> None
        self.observers.remove(observer)

    def set_changed(self):
        self.changed = True

    def clear_changed(self):
        self.changed = False

    def is_changed(self):
        return self.changed

    def notify_observers(self, arg = None):
        """
        Notifies the observer if there has been any change
        :param arg: Information passed with the notification
        """
        # type: (object) -> None
        if self.changed:
            for observer in self.observers:
                observer.update(self, arg)

    def clear_observers(self):
        self.observers = []

    def count_observers(self):
        return len(self.observers)


class Observer:

    @abc.abstractmethod
    def update(self, observable, info):
        # type: (Observable, object) -> object
        """
        Updates the observed based on the object observed
        :param observable: The object observed
        :param info: The information passed by the object
        """
        pass