__author__ = 'melop'


class Consequent:

    def __init__(self, consequence_description):
        self.consequence_description = consequence_description

    def describe(self):
        print(self.consequence_description)