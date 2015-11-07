class CommandActionHandler:
    def __init__(self, command_name, reaction, action_handler):
        self.command_name = command_name
        self.reaction = reaction
        self.action_handler = action_handler

    def handle(self, action):
        if self.command_name == action.command_name:
            return self.reaction
        else:
            return self.action_handler.handle(action)
