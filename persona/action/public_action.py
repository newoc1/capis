class PublicAction:
    def __init__(self, command_name, alignment, method_call, arguments_to_method=None):
        if type(method_call) is not str:
            raise Exception('method_call must be a string')
        self.command_name = command_name
        self.alignment = alignment
        self.method_call = method_call
        self.invoker = None
        self.subject = None
        self.number_of_reactions = 0;
        self.arguments_to_method = arguments_to_method

    # Checks for the existence of the method_call in the subject's environment item
    # before calling the method on the subject's environment item and then notifying
    # the subject's observers
    def execute(self, subject, invoker):
        self.invoker = invoker
        self.subject = subject
        print("%s Calling %s" % (invoker.name, self.command_name))
        method = getattr(subject.environment_item, self.method_call)
        if not method:
            raise Exception("Method %s does not exist" % self.method_call)
        if self.arguments_to_method:
            method(self.arguments_to_method)
        else:
            method()
        subject.notify_observers(self)
