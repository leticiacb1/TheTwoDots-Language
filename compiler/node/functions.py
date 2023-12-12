from .node import Node
from compiler.constants import types
from compiler.errors.types import InvalidType

class Println(Node):
    '''
    Função println (Golang).
    Possui um filho.

     println
        |
    Expresion

    [IN]  println(Expression)
    [OUT] Expresion_result

    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> None:
        expression_result , _type = self.children[0].evaluate(symbol_table)
        print(expression_result)

class If(Node):
    '''
    Função if (Golang).
    Possui 2 or 3 filhos (quando possuimos um else).

                 ________ If__________
               /          |           \
    bool_expression     Block_if      Block_else
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> None:

        conditional = self.children[0]
        block_if    = self.children[1]

        if(conditional.evaluate(symbol_table)[0]):
            block_if.evaluate(symbol_table)
        elif(len(self.children) > 2):
            #Bloco else
            self.children[2].evaluate(symbol_table)

class For(Node):
    '''
    Função for (Golang).
    Possui 4 filhos.

                 ________ For ________________
               /          |           \       \
    Init state     condition      increment    block
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> None:

        condition  = self.children[0]
        block      = self.children[1]

        while condition.evaluate(symbol_table)[0]:
            block.evaluate(symbol_table)


class Scanln(Node):
    '''
    Função Scanln (Golan
    Não possui filhos.
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, str):
        number = input()

        # Número
        if(number.isnumeric()):
            return int(number), types._Type.INT

        raise InvalidType(f" [SCANLN - EVALUATE] Only the integer type is accepted in the Scanln function. Tried type: {type(number)}")
