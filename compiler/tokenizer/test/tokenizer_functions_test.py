'''
Rode todos os teste utilizando:
    python3 -m pytest file.py
'''

from compiler.tokenizer.src.tokenizer import Tokenizer
from compiler.constants import specials, types, operators , delimiters, reserved_word
import unittest

class TestFunctionsTokenizer(unittest.TestCase):
    def test_if_else_function(self):
        '''
            Testa função if/else
        '''

        source_code = '''
                        if : ( x == 2) = {
                        } : {
                        } 
                      '''

        tokenizer = Tokenizer(source_code)
        tokenizer.select_next()
        tokenizer.select_next()

        assert tokenizer.next.type == reserved_word._Type.IF
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.TWO_DOTS
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.OPEN_PARENTHESES
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.IDENTIFIER
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.EQUAL_COMP
        tokenizer.select_next()

        assert tokenizer.next.type == types._Type.INT
        assert tokenizer.next.value == 2
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.CLOSE_PARENTHESES
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.EQUAL
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.OPEN_KEY
        tokenizer.select_next()
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.CLOSE_KEY
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.TWO_DOTS
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.OPEN_KEY
        tokenizer.select_next()
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.CLOSE_KEY
        tokenizer.select_next()
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.EOF

    def test_for_function(self):
        '''
            Testa função for
        '''

        source_code = ''' 
                          loop : ( i < 5) = {
                          }
                      '''

        tokenizer = Tokenizer(source_code)
        tokenizer.select_next()

        tokenizer.select_next()

        assert tokenizer.next.type == reserved_word._Type.FOR
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.TWO_DOTS
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.OPEN_PARENTHESES
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.IDENTIFIER
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.LESS_THAN
        tokenizer.select_next()

        assert tokenizer.next.type == types._Type.INT
        assert tokenizer.next.value == 5
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.CLOSE_PARENTHESES
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.EQUAL
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.OPEN_KEY
        tokenizer.select_next()
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.CLOSE_KEY
        tokenizer.select_next()
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.EOF

    def test_stdin_stdout_function(self):
        '''
            Testa função stdin/stdout
        '''

        source_code = ''' stdout : x
                          y = stdin()
                      '''
        tokenizer = Tokenizer(source_code)
        tokenizer.select_next()

        assert tokenizer.next.type == reserved_word._Type.STDOUT
        tokenizer.select_next()

        assert tokenizer.next.type == delimiters._Type.TWO_DOTS
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.IDENTIFIER
        assert tokenizer.next.value == 'x'
        tokenizer.select_next()
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.IDENTIFIER
        assert tokenizer.next.value == 'y'
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.EQUAL
        tokenizer.select_next()

        assert tokenizer.next.type == reserved_word._Type.STDIN
        tokenizer.select_next()
        tokenizer.select_next()
        tokenizer.select_next()
        tokenizer.select_next()

        assert tokenizer.next.type == specials._Type.EOF