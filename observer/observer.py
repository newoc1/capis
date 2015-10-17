class Observer:
    def __init__(self, name, alignment, subject_handler=None):
        self.name = name
        self.alignment = alignment
        self.subject = None
        self.subject_handler = subject_handler

    def update_subject(self, subject_update_command):
        subject_update_command.update(self.subject)

    def receive_update(self, action):
        self.subject_handler(self, action)
