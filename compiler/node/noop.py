from .node import Node

class NoOp(Node):
    '''
    Sem operação. Não contém filhos.
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> None:
        return None
