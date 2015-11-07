class InvokerReaction:
    def __init__(self, action, target_subject_name):
        self.action = action
        self.target_subject_name = target_subject_name

    def react(self, responsible_action, invoker):
        subject = responsible_action.invoker.get_subject(self.target_subject_name)
        if subject:
            self.action.execute(subject, invoker)
