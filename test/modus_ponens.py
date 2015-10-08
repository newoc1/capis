from test.consequent import Consequent


class ModusPonens:

    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

    def infer_result(self, antecedent):
        if antecedent is self.antecedent:
            consequent = self.consequent
        else:
            consequent = False
        return consequent

