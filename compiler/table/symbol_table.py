from compiler.errors.symbol_table import ExistingKey

class SymbolTable:
    '''
    Formato  :
                Nome da variavel  |     Value    |   Type
                --------------------------------------------
                      x                   3          Int

    self.table = {
        "x" : (3  , int),
    }

    table = { var : (value , type)}

    O tipo pode ser "INT" ou "STRING" .
    '''
    def __init__(self):
        self.table = {}

    def getter(self, identifier) -> (int, str):
        return self.table[identifier][0], self.table[identifier][1]

    def create(self, identifier: str, _type: str) -> None:
        if(identifier not in self.table.keys()):
            self.table[identifier] = (None, _type)
        else:
            raise ExistingKey(f" [SYMBOL TABLE - CREATE] The passed key [{identifier}] has already been declared.")

    def setter(self, identifier, value) -> None:
        self.table[identifier] = (value, self.table[identifier][1])
