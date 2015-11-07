class AlignmentActionHandler:
    def __init__(self, alignment, reaction, action_handler):
        self.alignment = alignment
        self.reaction = reaction
        self.action_handler = action_handler

    def handle(self, action):
        if action.alignment.meets_threshold(self.alignment):
            return self.reaction
        else:
            return self.action_handler.handle(action)
