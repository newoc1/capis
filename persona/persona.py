class Persona:
    MAX_NUMBER_OF_REACTIONS = 80

    def __init__(self, name, alignment, subject, action_handlers):
        self.name = name
        self.alignment = alignment
        self.observers = []
        self.subjects = {subject.name: subject}
        self.action_handlers = action_handlers

    def add_observer(self, observer):
        if not observer.owner:
            observer.owner = self
            self.observers.append(observer)
        else:
            raise 'Tried to add an observer that already has an owner'

    def add_subject(self, subject):
        if not subject.owner:
            subject.owner = self
            self.subjects[subject.name] = subject
        else:
            raise 'Tried to add a subject that already has an owner'

    def get_subject(self, subject_name):
        if subject_name not in self.subjects:
            return None
        else:
            return self.subjects[subject_name]

    def get_observed_subject(self, subject_name):
        return next(observer.subject for observer in self.observers if observer.subject.name == subject_name)

    def react(self, action):
        print('%s reacting' % self.name)
        reaction = self.action_handlers[0].handle(action)
        if action.number_of_reactions < self.MAX_NUMBER_OF_REACTIONS:
            action.number_of_reactions += 1
            reaction.react(action, self)
            
    def execute(self, action, subject):
        action.execute(subject, self)
