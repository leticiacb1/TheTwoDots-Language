from .node import Node
from compiler.errors.types import IncompatibleTypes

class VarDec(Node):
    '''
        Pode ter 1 ou 2 filhos:

        Exemplo:
            1 filho : var y int
            2 filhos : var x int = 2

          VarDec
        /       \
identifier      Caso possua BoolExpression
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> None:

        type1 = self.value
        symbol_table.create(self.children[0].value, type1)

        if(len(self.children) == 2):
            boolExpression, type2 = self.children[1].evaluate(symbol_table)

            if(type1 == type2):
                symbol_table.setter(self.children[0].value, boolExpression)
            else:
                raise IncompatibleTypes(f" [VARDEC - EVALUATE] Setting a value type [{type2}] inconsistent with the variable type [{type1}]")
