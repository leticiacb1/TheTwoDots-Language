'''
Rode todos os teste utilizando:
    python3 -m pytest file.py
'''

from compiler.tokenizer.src.tokenizer import Tokenizer
from compiler.constants import specials, types, operators , delimiters, reserved_word
import unittest

class TestDeclarationTokenizer(unittest.TestCase):
    def test_variables_declaration(self):
        '''
            Test variable declaration
        '''

        source_code = 'declare x : integer'

        tokenizer = Tokenizer(source_code)
        tokenizer.select_next()

        assert tokenizer.next.type == reserved_word._Type.DECLARE
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.IDENTIFIER
        assert tokenizer.next.value == 'x'
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.TWO_DOTS
        tokenizer.select_next()

        assert tokenizer.next.type == types._Type.INT
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.EOF

    def test_function_declaration(self):
        '''
            Test function declaration
        '''

        source_code = ''' create hello_world ( arg1 , arg2 ) : string = {
                            return "hello"
                          }
                      '''

        tokenizer = Tokenizer(source_code)
        tokenizer.select_next()

        assert tokenizer.next.type == reserved_word._Type.CREATE
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.IDENTIFIER
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.OPEN_PARENTHESES
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.IDENTIFIER
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.COMMA
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.IDENTIFIER
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.CLOSE_PARENTHESES
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.TWO_DOTS
        tokenizer.select_next()

        assert tokenizer.next.type == types._Type.STR
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.EQUAL
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.OPEN_KEY
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.END_OF_LINE
        tokenizer.select_next()

        assert tokenizer.next.type == reserved_word._Type.RETURN
        tokenizer.select_next()

        assert tokenizer.next.type  == specials._Type.VARIABLE_STR
        assert tokenizer.next.value == "hello"
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.END_OF_LINE
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.CLOSE_KEY
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.END_OF_LINE
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.EOF