__author__ = 'Owen'


class SymbolParser:

    def hello(self, decomposeString):
        if len(decomposeString) == 1:
            print(decomposeString)
            print("Finished recursion")
        else:
            print(decomposeString[0])
            self.hello(decomposeString[1:])