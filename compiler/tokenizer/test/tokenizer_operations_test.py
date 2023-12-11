'''
Rode todos os teste utilizando:
    python3 -m pytest file.py
'''

from compiler.tokenizer.src.tokenizer import Tokenizer
from compiler.constants import specials, types, operators
import unittest

class TestOperationsTokenizer(unittest.TestCase):
    def test_operations(self):
        '''
            Test operations
        '''

        source_code = '4 + 2 - 1 -*+ 10 / 2'

        tokenizer = Tokenizer(source_code)
        tokenizer.select_next()

        assert tokenizer.next.value == 4
        assert tokenizer.next.type == types._Type.INT
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.PLUS
        tokenizer.select_next()

        assert tokenizer.next.value == 2
        assert tokenizer.next.type == types._Type.INT
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.MINUS
        tokenizer.select_next()

        assert tokenizer.next.value == 1
        assert tokenizer.next.type == types._Type.INT
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.MINUS
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.MULT
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.PLUS
        tokenizer.select_next()

        assert tokenizer.next.value == 10
        assert tokenizer.next.type == types._Type.INT
        tokenizer.select_next()

        assert tokenizer.next.type == operators._Type.DIV
        tokenizer.select_next()

        assert tokenizer.next.value == 2
        assert tokenizer.next.type == types._Type.INT
        tokenizer.select_next()


