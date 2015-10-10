__author__ = 'melop'


class Subject:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)
        observer.set_subject(self)

    def unregister_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
            observer.set_subject(None)

    def notify_observers(self):
        if len(self.observers) == 0:
            print('no observers')
        for observer in self.observers:
            observer.receive_update(self)
