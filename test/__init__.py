from test.symbol_parser import SymbolParser
from test.modus_ponens import ModusPonens
from test.antecedent import Antecedent
from test.consequent import Consequent

something = SymbolParser()
something.hello('bat')
something.hello('from fedora!')

it_is_raining = Antecedent("It\'s raining")
bad_antecedent = Antecedent("Bad anted")
it_is_pouring = Consequent("It is pouring")
modus_ponens_A = ModusPonens(it_is_raining,it_is_pouring)

consequent = modus_ponens_A.infer_result(bad_antecedent)
if consequent:
    consequent.describe()
