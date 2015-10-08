__author__ = 'Owen'


class SymbolParser:

    def hello(self, decompose_string):
        if len(decompose_string) == 1:
            print(decompose_string)
            print("Finished recursion")
        else:
            print(decompose_string[0])
            self.hello(decompose_string[1:])