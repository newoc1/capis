class Observer:
    def __init__(self):
        self.subject = None
        self.owner = None

    # Does not produce a reaction if the invoker of the
    # action was the Persona that owns it
    def receive_update(self, action):
        if not action.invoker == self.owner:
            self.owner.react(action)
