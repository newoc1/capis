class Subject:
    def __init__(self, name, environment_item):
        self.name = name
        self.environment_item = environment_item
        self.observers = []
        self.owner = None

    def register_observer(self, observer):
        self.observers.append(observer)
        observer.subject = self

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
            observer.subject = None

    def notify_observers(self, action):
        if len(self.observers) == 0:
            print('no observers')
        for observer in self.observers:
            observer.receive_update(action)
