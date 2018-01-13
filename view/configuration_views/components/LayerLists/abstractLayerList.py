import abc


class AbstractLayerList:

    @abc.abstractmethod
    def curselection(self):
        pass

    @abc.abstractmethod
    def insert(self):
        pass

    @abc.abstractmethod
    def show(self, row=0, column=0):
        pass
