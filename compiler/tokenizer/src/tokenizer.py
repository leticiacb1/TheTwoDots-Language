import re
from compiler.constants import delimiters, operators, reserved_word, specials, types
from compiler.tokens import Token

class Tokenizer:
    '''
        Responsável por capturar um token (átomo) do texto-fonte
    '''

    def __init__ (self, source : str):
        self.source = source 
        self.position = 0 
        self.next = Token("", 0)

        self.reserved_words = {
            'declare' : {'type': reserved_word._Type.DECLARE, 'value': reserved_word._Value.RESERVED},
            'create'  : {'type': reserved_word._Type.CREATE, 'value': reserved_word._Value.RESERVED},
            'invoke'  : {'type': reserved_word._Type.INVOKE, 'value': reserved_word._Value.RESERVED},
            'return'  : {'type': reserved_word._Type.RETURN, 'value': reserved_word._Value.RESERVED},
            'if': {'type': reserved_word._Type.IF, 'value': reserved_word._Value.RESERVED},
            'loop': {'type': reserved_word._Type.FOR, 'value': reserved_word._Value.RESERVED},
            'stdout': {'type': reserved_word._Type.STDOUT, 'value': reserved_word._Value.RESERVED},
            'stdin': {'type': reserved_word._Type.STDIN, 'value': reserved_word._Value.RESERVED},
            'integer': {'type': types._Type.INT, 'value': types._Value.TYPES},
            'string': {'type': types._Type.STR, 'value': types._Value.TYPES}
        }
    def _get_number_token(self):
        value_str = ''
        while (self.position < len(self.source) and self.source[self.position].isdigit()):
            value_str += self.source[self.position]
            self.position += 1

        return Token(type = types._Type.INT , value= int(value_str))

    def _get_operator_token(self):
        if(self.source[self.position+1] == operators._Type.EQUAL):
            self.position += 1
            return Token(type= operators._Type.EQUAL_COMP, value=operators._Value.OPERATORS)
        else:
            return Token(type=self.source[self.position], value=operators._Value.OPERATORS)

    def _get_delimiter_token(self):
        return Token(type=self.source[self.position], value= delimiters._Value.DELIMITER)

    def _get_str_variable_token(self):
        value_str = ''

        self.position += 1
        while (self.source[self.position] != delimiters._Type.QUOTATION_MARKS):
            value_str += self.source[self.position]
            self.position += 1
        return Token(type=specials._Type.VARIABLE_STR, value=value_str)

    def _get_word_token(self):
        value_str = ''

        while (self.position < len(self.source)
               and
               (re.search(r'[a-zA-Z0-9_]+', self.source[self.position]))
              ):

            value_str += self.source[self.position]
            self.position += 1

        if value_str in self.reserved_words.keys():
            # Function
            return Token(type=self.reserved_words[value_str]['type'],
                         value=self.reserved_words[value_str]['value'])
        else:
            # Identififer
            return Token(type=specials._Type.IDENTIFIER, value=value_str)

    def _get_invalid_token(self):
        return Token(type=specials._Type.INVALID, value=specials._Value.SPECIALS)
    def select_next(self) -> None:
        '''
            Atualiza a variável next com o próximo token passado
        '''
        
        while(True):

            if(self.position >= len(self.source)):
            
                if(self.next.type != specials._Type.EOF):
                    self.next = Token(type = specials._Type.EOF , value = specials._Value.SPECIALS)
                break

            else:
                if(self.source[self.position].isdigit()):
                    self.next = self._get_number_token()
                    break

                elif(self.source[self.position] in [operators._Type.PLUS, operators._Type.MINUS, operators._Type.MULT, operators._Type.DIV,
                                                    operators._Type.BIGGER_THEN, operators._Type.LESS_THAN, operators._Type.NOT,
                                                    operators._Type.CONCAT,
                                                    operators._Type.EQUAL]):
                    self.next = self._get_operator_token()
                    self.position += 1
                    break
                elif(self.source[self.position] in [delimiters._Type.OPEN_PARENTHESES, delimiters._Type.CLOSE_PARENTHESES,
                                                    delimiters._Type.OPEN_KEY, delimiters._Type.CLOSE_KEY,
                                                    delimiters._Type.COMMA, delimiters._Type.TWO_DOTS, delimiters._Type.END_OF_LINE]):
                    self.next = self._get_delimiter_token()
                    self.position += 1
                    break
                elif(self.source[self.position] == delimiters._Type.QUOTATION_MARKS):
                    self.next = self._get_str_variable_token()
                    self.position += 1
                    break
                elif(self.source[self.position].isalpha()):
                    self.next = self._get_word_token()
                    break
                elif(self.source[self.position].isspace()):
                    self.position +=1
                else:
                    self.next = self._get_invalid_token()
                    self.position += 1
                    break 
