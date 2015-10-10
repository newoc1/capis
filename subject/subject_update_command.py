__author__ = 'melop'


class SubjectUpdateCommand:

    def __init__(self, name):
        self.name = name

    def update(self, subject):
        subject.name = self.name