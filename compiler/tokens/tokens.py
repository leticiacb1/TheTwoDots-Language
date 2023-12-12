from compiler.constants import delimiters, operators, reserved_word, specials, types

class Token:
    '''            
        Define caracters da cadeia de string passada.
    '''

    def __init__ (self, type : str , value : int | str):
        self.type = type
        self.value = value

    def _delimiter_token(self) -> str :
        match self.type:
            case delimiters._Type.OPEN_PARENTHESES:
                return f" [TOKEN] ( '{self.type}' , 'OPEN_PARENTHESES')\n"
            case delimiters._Type.CLOSE_PARENTHESES:
                return f" [TOKEN] ( '{self.type}' , 'CLOSE_PARENTHESES')\n"
            case delimiters._Type.OPEN_KEY:
                return f" [TOKEN] ( '{self.type}' , 'OPEN_KEY')\n"
            case delimiters._Type.CLOSE_KEY:
                return f" [TOKEN] ( '{self.type}' , 'CLOSE_KEY')\n"
            case delimiters._Type.TWO_DOTS:
                return f" [TOKEN] ( '{self.type}' , 'TWO_DOTS')\n"
            case delimiters._Type.COMMA:
                return f" [TOKEN] ( '{self.type}' , 'COMMA')\n"
            case delimiters._Type.END_OF_LINE:
                return f" [TOKEN] ( '{self.type}' , 'END_OF_LINE')\n"
            case delimiters._Type.QUOTATION_MARKS:
                return f" [TOKEN] ( '{self.type}' , 'QUOTATION_MARKS')\n"
    def _operator_token(self) -> str :

        match self.type:
            case operators._Type.PLUS:
                return f" [TOKEN] ( '{self.type}' , 'PLUS')\n"
            case operators._Type.MINUS:
                return f" [TOKEN] ( '{self.type}' , 'MINUS')\n"
            case operators._Type.MULT:
                return f" [TOKEN] ( '{self.type}' , 'MULT')\n"
            case operators._Type.DIV:
                return f" [TOKEN] ( '{self.type}' , 'DIV')\n"
            case operators._Type.EQUAL:
                return f" [TOKEN] ( '{self.type}' , 'EQUAL')\n"
            case operators._Type.EQUAL_COMP:
                return f" [TOKEN] ( '{self.type}' , 'EQUAL_COMP')\n"
            case operators._Type.BIGGER_THEN:
                return f" [TOKEN] ( '{self.type}' , 'BIGGER_THEN')\n"
            case operators._Type.LESS_THAN:
                return f" [TOKEN] ( '{self.type}' , 'LESS_THAN')\n"
            case operators._Type.AND:
                return f" [TOKEN] ( '{self.type}' , 'AND')\n"
            case operators._Type.OR:
                return f" [TOKEN] ( '{self.type}' , 'OR')\n"
            case operators._Type.NOT:
                return f" [TOKEN] ( '{self.type}' , 'NOT')\n"
            case operators._Type.CONCAT:
                return f" [TOKEN] ( '{self.type}' , 'CONCAT')\n"

    def _reserved_token(self) -> str:
        return f" [TOKEN] ('{self.type}' , 'RESERVED')\n"

    def _specials_token(self) -> str:
        match self.type:
            case specials._Type.EOF:
                return f" [TOKEN] ('EOF' , EOF)\n"
            case specials._Type.IDENTIFIER:
                return f" [TOKEN] ('{self.value}' , IDENTIFIER)\n"
            case specials._Type.VARIABLE_STR:
                return f" [TOKEN] ('{self.value}' , VARIABLE_STR)\n"
            case specials._Type.INVALID:
                return f" [TOKEN] ('{self.value}' , INVALID)\n"

    def _types_token(self) -> str:
        return f" [TOKEN] ('{self.type}' , 'TYPE')\n"

    def __str__(self) -> str:

        if self.type in [delimiters._Type.OPEN_PARENTHESES, delimiters._Type.CLOSE_PARENTHESES,
                         delimiters._Type.OPEN_KEY, delimiters._Type.CLOSE_KEY, delimiters._Type.COMMA,
                         delimiters._Type.TWO_DOTS, delimiters._Type.END_OF_LINE, delimiters._Type.QUOTATION_MARKS
                         ]:

            return self._delimiter_token()

        if self.type in [operators._Type.PLUS, operators._Type.MINUS , operators._Type.MULT, operators._Type.DIV,
                         operators._Type.EQUAL,
                         operators._Type.EQUAL_COMP, operators._Type.BIGGER_THEN, operators._Type.LESS_THAN,
                         operators._Type.AND, operators._Type.OR , operators._Type.NOT,
                         operators._Type.CONCAT
                         ]:
            return self._operator_token()


        if self.type in [reserved_word._Type.IF, reserved_word._Type.FOR,
                         reserved_word._Type.STDOUT, reserved_word._Type.STDIN,
                         reserved_word._Type.DECLARE, reserved_word._Type.CREATE, reserved_word._Type.INVOKE,
                         reserved_word._Type.RETURN]:
            return self._reserved_token()

        if self.type in [specials._Type.EOF, specials._Type.IDENTIFIER,
                         specials._Type.VARIABLE_STR, specials._Type.INVALID]:
            return self._specials_token()

        if self.type in [types._Type.INT , types._Type.STR]:
            return self._types_token()