from .node import Node
from compiler.constants.delimiters import _Type

class Block(Node):
    '''
    Pode possuir n filhos.
    Seus filhos são retorno do block Statement.

     __________Block______________
    /           |        ...      \
statement   statement          statement

    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        for child in self.children:
            if child.value != 'END_OF_LINE':
                result = child.evaluate(symbol_table)
            else:
                child.evaluate(symbol_table)

            if child.value == 'RETURN':
                return result

        return result
