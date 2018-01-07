from observe import Observable, Observer
import threading


class ThreadObsevable(Observable, threading.Thread):

    def __init__(self):
        Observable.__init__(self)
        threading.Thread.__init__(self)


class ThreadObserver(Observer, threading.Thread):

    def __init__(self):
        Observer.__init__(self)
        threading.Thread.__init__(self)
