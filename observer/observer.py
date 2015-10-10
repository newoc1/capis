__author__ = 'melop'


class Observer:
    def __init__(self, name, alignment, actions):
        self.name = name
        self.alignment = alignment
        self.actions = actions

    def update_subject(self, subject_update_command):
        subject_update_command.update(self.subject)

    def set_subject(self, subject):
        self.subject = subject
