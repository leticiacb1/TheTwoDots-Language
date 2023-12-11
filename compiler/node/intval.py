from .node import Node
from compiler.constants import types

class IntVal(Node):
    '''
    Valor inteiro. Não possui filhos.
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, str):
        return self.value, types.TYPE_INT
