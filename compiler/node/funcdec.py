from .node import Node
from compiler.table import FunctionTable

class FuncDec(Node):
    '''
    Declaração de função.

    Possui n+2 filhos, onde n é o número de argumentos e os 2 filhos obrigatórios é a declaração da função e o seu bloco de execução.

    Exemplos:
     1 . Declaração com apenas 2 filhos : def main () { ... }                [2 filhos]
     2 . Declaração com mais de 2 filhos : def soma ( x int , y int) { ... } [4 filhos]

            -------------------FuncDec -------------------
           /             |       ...      |               \
       VarDec          Vardec            VardDec         Block
    (declaração)          |------ args ------|        (Ação da função)
         |
    identifier

    '''

    def __init__(self, value):
        super().__init__(value)
        self.function_table = FunctionTable

    def evaluate(self, symbol_table):
        '''
        Declara função
        '''
        node_declaration = self.children[0]
        function_name = node_declaration.children[0].value

        self.function_table.declare(function_name, self, node_declaration.value)
