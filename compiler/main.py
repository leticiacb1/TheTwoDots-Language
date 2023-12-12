
from compiler.parser import Parser
from compiler.prepro import PrePro
from compiler.table.symbol_table import SymbolTable
from compiler.constants import delimiters

import sys

def load_file(filename) -> list[str]:
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print(f"\n [ERROR] Usage: python3 main.py <filename> | Got {sys.argv} \n")
        sys.exit(1)

    filename = (sys.argv)[1:]
    source_code_lines = load_file(filename[0])

    # Retira comentários
    code = PrePro().pre_pro(source_code_lines) + delimiters._Type.END_OF_LINE

    # Instancia tabela de simbolos
    table = SymbolTable()

    # Resolve a arvore
    tree = Parser().run(code)
    result = tree.evaluate(table)
