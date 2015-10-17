class PublicAction:
    def __init__(self, command_name, alignment, invoker, method_call, arguments_to_method=None):
        if type(method_call) is not str:
            raise Exception('method_call must be a string')
        self.command_name = command_name
        self.alignment = alignment
        self.invoker = invoker
        self.method_call = method_call
        self.arguments_to_method = arguments_to_method

    def update(self, subject):
        print("Calling %s" % self.command_name)
        method = getattr(subject.environment_item, self.method_call)
        if not method:
            raise Exception("Method %s does not exist" % self.method_call)
        if self.arguments_to_method:
            method(self.arguments_to_method)
        else:
            method()
        subject.notify_observers(self)
