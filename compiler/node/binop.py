from .node import Node
from compiler.constants import operators
from compiler.constants import types
from compiler.errors.types import IncompatibleTypes, InvalidType

class BinOp(Node):
    '''
    Operações binárias. Contém dois filhos

    True e False agora representado de forma numérica : true(1) , false(0)
    '''

    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table) -> (int, int | str):
        if (self.value == operators._Type.PLUS):
            value1 , type1 =  self.children[0].evaluate(symbol_table)
            value2 , type2 =  self.children[1].evaluate(symbol_table)

            if( (type1 == types.TYPE_INT) and (type2 == types.TYPE_INT) ):
                return value1 + value2, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in + operation : {type1} + {type2}")

        if (self.value == operators._Type.MINUS):
            value1 , type1 = self.children[0].evaluate(symbol_table)
            value2 , type2 = self.children[1].evaluate(symbol_table)


            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                return value1 - value2, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in - operation : {type1} - {type2}")

        if (self.value == operators._Type.BAR):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                return value1//value2, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in / operation : {type1} / {type2}")

        if (self.value == operators._Type.TIMES):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                return value1 * value2, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in * operation : {type1} * {type2}")

        if (self.value == operators._Type.OR):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                if(value1 or value2):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in OR operation : {type1} or {type2}")

        if (self.value == operators._Type.AND):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if ((type1 == types.TYPE_INT) and (type2 == types.TYPE_INT)):
                if(value1 and value2):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in AND operation : {type1} and {type2}")

        if (self.value == operators._Type.BIGGER_THEN):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if (type1 == type2):
                if(value1 > value2):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in > operation : {type1} > {type2}")

        if (self.value == operators._Type.LESS_THAN):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if (type1 == type2):
                if (value1 < value2):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in < operation : {type1} < {type2}")

        if (self.value == operators._Type.EQUAL_COMP):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            if (type1 == type2):
                if (value1 == value2):
                    return 1, types.TYPE_INT
                return 0, types.TYPE_INT

            raise IncompatibleTypes(f" [Binop - Evaluate] Incompatible Types find in == operation : {type1} == {type2}")

        if(self.value == operators._Type.CONCAT):
            value1, type1 = self.children[0].evaluate(symbol_table)
            value2, type2 = self.children[1].evaluate(symbol_table)

            return str(value1) + str(value2) , types.TYPE_STR

        raise InvalidType(f" [Binop - Evaluate] Invalid Type find : {self.value}")
