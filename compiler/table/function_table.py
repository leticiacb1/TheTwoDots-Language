from compiler.errors.symbol_table import ExistingKey
from compiler.node import Node


class FunctionTable:
    '''
    Formato  :
                Nome da função |     Nó endereço da função    |   Type
                ---------------------------------------------------------------
                    main          Próprio nó FuncDec             (Int or str)

    '''

    table = {}

    @classmethod
    def getter(cls, name: str) -> (Node, str):
        return cls.table[name][0], cls.table[name][1]

    @classmethod
    def declare(cls, name: str, node: Node, _type: str) -> None:
        if name not in cls.table.keys():
            cls.table[name] = (node, _type)
        else:
            raise ExistingKey(f" [FUNCTION TABLE - CREATE] The function [{name}] has already been declared.")
