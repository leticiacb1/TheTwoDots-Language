from .node import Node
from compiler.table import FunctionTable, SymbolTable

class FuncCall(Node):
    '''
    Chamada de Função.

               FuncCall
        (value = nome da função)
      /           |  |          \
    BExpression    ...       BExpression


    '''

    def __init__(self, value):
        super().__init__(value)
        self.function_table = FunctionTable

    def evaluate(self, symbol_table) -> (None, None):
        #                  function_node (FuncDec)
        #                 /          |           \
        #            VarDec         ...          Block
        #          (declaração)      |
        #               |        VarDec(args)
        #           identifier       |
        #                        identifier

        local_table = SymbolTable()
        # ---- Argumentos passados para a função no seu "call" ----
        function_name = self.value
        reviced_args  = self.children

        # ---- Consultando declaração da função e os tipos de argumentos esperados ----
        function_node, _type = self.function_table.getter(function_name)
        declaration, *expected_args, block = function_node.children

        # -- Mesma quantidade de argumentos passados e requeridos pela função: ----
        if(len(reviced_args) != len(expected_args)):
            raise Exception(f" [FUNCALL- EVALUATE] Incorrect number of arguments: expected {len(expected_args)} got {len(reviced_args)}")

        # ---- Varrendo argumentos passados e argumentos esperados ----
        for i in range(len(reviced_args)):

            expected_args[i].evaluate(local_table)
            expected_type = expected_args[i].value

            identifier   = expected_args[i].children[0]

            recived_value, recived_type = reviced_args[i].evaluate(symbol_table)

            if(recived_type != expected_type):
                raise Exception(f" [FUNCALL- EVALUATE] Incorrect arg type for {identifier.value} in {function_name} function. Expected type {expected_type} got {recived_type}")

            # Settar valor recebido do argumento
            local_table.setter(identifier.value, recived_value)

        # Executando o conteúdo da função
        result = block.evaluate(local_table)

        if(result and result != (None, None) and len(result) == 2):
            value , return_type = result

            if(return_type != _type):
                raise Exception(f" [FUNCALL- EVALUATE] Incorrect return type in {function_name} function. Expected type {_type} got {return_type}")

        return result







