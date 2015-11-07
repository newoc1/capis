class SubjectReaction:
    def __init__(self, action):
        self.action = action

    def react(self, responsible_action, invoker):
        self.action.execute(responsible_action.subject, invoker)
