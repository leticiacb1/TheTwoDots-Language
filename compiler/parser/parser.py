from compiler.tokenizer import Tokenizer
from compiler.constants import delimiters, number, operators, reserved_word, identifier , text , types, eof
from compiler.errors.parser import InvalidExpression
from compiler.errors.tokens import InvalidToken
from compiler.node import (IntVal, StrVal, VarDec, FuncDec, BinOp, UnOp, NoOp, Identifier, Assigment, Node, Println , Scanln, If , For, Block , Program , Return, FuncCall)


class Parser:
    tokenizer: object = Tokenizer('')

    @classmethod
    def change_atribute_value(cls, source):
        cls.tokenizer = Tokenizer(source)

    @staticmethod
    def parser_assigment() -> Node:

        tokens = Parser().tokenizer

        node_identifier = Identifier(value=tokens.next.value)
        tokens.select_next()

        if (tokens.next.type == operators._Type.EQUAL):

            tokens.select_next()

            bool_expression = Parser().parse_bool_expression()  # Mudo o assigment

            node_assigment = Assigment(value=operators._Type.EQUAL)
            node_assigment.add_child(node_identifier)  # Left
            node_assigment.add_child(bool_expression)  # Right

            return node_assigment

        elif(tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
            tokens.select_next()

            func_call_node = FuncCall(value = node_identifier.value)
            while(tokens.next.type != delimiters._Type.CLOSE_PARENTHESES):
                bool_expression = Parser().parse_bool_expression()
                func_call_node.add_child(bool_expression)

                if(tokens.next.type == delimiters._Type.COMMAN):
                    tokens.select_next()
                else:
                    break

            if(tokens.next.type == delimiters._Type.CLOSE_PARENTHESES):
                tokens.select_next()
            else:
                raise InvalidExpression(f"\n [STATEMENT] Expected close parentheses token type | Got {tokens.next}")

            return func_call_node
        else:
            raise InvalidExpression(f"\n [STATEMENT] Expected assigment token type | Got {tokens.next}")



    @staticmethod
    def parser_factor() -> Node:
        '''
        Verifica a existencia de operadores unários.
        '''
        tokens = Parser().tokenizer

        if (tokens.next.type == number._Type.INT):

            node = IntVal(value=tokens.next.value)
            tokens.select_next()

            return node

        elif (tokens.next.type == text._Type.VARIABLE_STR):
            node = StrVal(value=tokens.next.value)
            tokens.select_next()

            return node

        elif (tokens.next.type == identifier._Type.IDENTIFIER):
            node = Identifier(value=tokens.next.value)
            tokens.select_next()

            if(tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
                func_call_node = FuncCall(value=node.value)
                tokens.select_next()

                while(tokens.next.type != delimiters._Type.CLOSE_PARENTHESES):
                    bool_expression = Parser().parse_bool_expression()
                    func_call_node.add_child(bool_expression)

                    if(tokens.next.type == delimiters._Type.COMMAN):
                        tokens.select_next()
                    else:
                        break

                if (tokens.next.type == delimiters._Type.CLOSE_PARENTHESES):
                    tokens.select_next()
                    node = func_call_node
                else:
                    raise InvalidExpression(f"\n [FACTOR] Expected close parentheses token type | Got {tokens.next}")

            return node

        elif (tokens.next.type == operators._Type.PLUS):

            node = UnOp(value=operators._Type.PLUS)
            tokens.select_next()
            child = Parser().parser_factor()

            node.add_child(child)

            return node

        elif (tokens.next.type == operators._Type.MINUS):

            node = UnOp(value=operators._Type.MINUS)
            tokens.select_next()
            child = Parser().parser_factor()

            node.add_child(child)

            return node

        elif (tokens.next.type == operators._Type.NOT):
            node = UnOp(value=operators._Type.NOT)
            tokens.select_next()
            child = Parser().parser_factor()

            node.add_child(child)

            return node

        elif (tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
            tokens.select_next()
            node = Parser().parse_bool_expression()

            if (tokens.next.type == delimiters._Type.CLOSE_PARENTHESES):
                tokens.select_next()
                return node
            else:
                raise InvalidExpression(f"\n [FACTOR] Expected close parentheses type | Got {tokens.next}")

        elif(tokens.next.type == functions._Type.SCANLN):
            tokens.select_next()
            node = Scanln(value = functions._Type.SCANLN)

            if (tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
                tokens.select_next()
                if (tokens.next.type == delimiters._Type.CLOSE_PARENTHESES):
                    tokens.select_next()
                    return node
                else:
                    raise InvalidToken(f"\n [FACTOR] Expected close parentheses type | Got {tokens.next}")
            else:
                raise InvalidToken(f"\n [FACTOR] Expected open parentheses type | Got {tokens.next}")
        else:
            raise InvalidToken(f"\n [FACTOR] Token type recived : {tokens.next}")

    @staticmethod
    def parser_term() -> Node:
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loops de multiplicação e subtração.
        '''

        tokens = Parser().tokenizer

        left_node = Parser().parser_factor()

        while (tokens.next.type in [operators._Type.TIMES, operators._Type.BAR]):

            if (tokens.next.type == operators._Type.TIMES):
                op_node = BinOp(operators._Type.TIMES)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_factor()
                op_node.add_child(right_node)

                left_node = op_node

            elif (tokens.next.type == operators._Type.BAR):
                op_node = BinOp(operators._Type.BAR)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_factor()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n [TERM] Token type recived : {tokens.next.type}")

        return left_node

    @staticmethod
    def parser_expression() -> Node:
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loops de soma e subtração.
            Expressões binárias.
        '''
        tokens = Parser().tokenizer

        left_node = Parser().parser_term()

        while (tokens.next.type in [operators._Type.PLUS, operators._Type.MINUS, operators._Type.CONCAT]):

            if (tokens.next.type == operators._Type.PLUS):
                op_node = BinOp(operators._Type.PLUS)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_term()
                op_node.add_child(right_node)

                left_node = op_node

            elif (tokens.next.type == operators._Type.MINUS):
                op_node = BinOp(operators._Type.MINUS)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_term()
                op_node.add_child(right_node)

                left_node = op_node

            elif (tokens.next.type == operators._Type.CONCAT):
                op_node = BinOp(operators._Type.CONCAT)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_term()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n [EXPRESSION]Token type recived : {tokens.next.type}")

        return left_node

    @staticmethod
    def parser_rl_expressions() -> Node:
        tokens = Parser().tokenizer

        left_node = Parser().parser_expression()

        while (tokens.next.type in [operators._Type.BIGGER_THEN, operators._Type.EQUAL_COMP , operators._Type.LESS_THAN]):

            if (tokens.next.type == operators._Type.BIGGER_THEN):
                op_node = BinOp(operators._Type.BIGGER_THEN)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_expression()
                op_node.add_child(right_node)

                left_node = op_node

            elif (tokens.next.type == operators._Type.LESS_THAN):
                op_node = BinOp(operators._Type.LESS_THAN)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_expression()
                op_node.add_child(right_node)

                left_node = op_node

            elif (tokens.next.type == operators._Type.EQUAL_COMP):
                op_node = BinOp(operators._Type.EQUAL_COMP)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_expression()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n [EXPRESSION]Token type recived : {tokens.next.type}")

        return left_node


    @staticmethod
    def parser_bool_term() -> Node:
        tokens = Parser().tokenizer

        left_node = Parser().parser_rl_expressions()

        while (tokens.next.type == operators._Type.AND):

            if (tokens.next.type == operators._Type.AND):
                op_node = BinOp(operators._Type.AND)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_rl_expressions()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n [BOOL TERM EXPRESSION]Token type recived : {tokens.next.type}")

        return left_node

    @staticmethod
    def parse_bool_expression() -> Node:
        '''
            Analisa se a sintaxe está aderente a gramática.
            Loop de OR.
            Expressões binárias.
        '''
        tokens = Parser().tokenizer

        left_node = Parser().parser_bool_term()

        while (tokens.next.type == operators._Type.OR):

            if (tokens.next.type == operators._Type.OR):
                op_node = BinOp(operators._Type.OR)
                op_node.add_child(left_node)

                tokens.select_next()

                right_node = Parser().parser_bool_term()
                op_node.add_child(right_node)

                left_node = op_node

            else:
                raise InvalidToken(f"\n [BOOL EXPRESSION]Token type recived : {tokens.next.type}")

        return left_node

    @staticmethod
    def parser_statement() -> Node:

        tokens = Parser().tokenizer

        if (tokens.next.type == delimiters._Type.END_OF_LINE):
            tokens.select_next()
            node = NoOp(value='END_OF_LINE')

        elif (tokens.next.type == identifier._Type.IDENTIFIER):
            node = Parser().parser_assigment()

        elif (tokens.next.type == functions._Type.PRINTLN):
            tokens.select_next()

            if (tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
                tokens.select_next()

                bool_expression = Parser().parse_bool_expression() # bool_expression ?

                node_println = Println(value=functions._Type.PRINTLN)
                node_println.add_child(bool_expression)

                if (tokens.next.type != delimiters._Type.CLOSE_PARENTHESES):
                    raise InvalidExpression(f"\n [STATEMENT] Expected close parentheses type | Got {tokens.next}")
                tokens.select_next()

                node = node_println

            else:
                raise InvalidExpression(f"\n [STATEMENT] Expected open parentheses type | Got {tokens.next}")

        elif(tokens.next.type == functions._Type.IF):
            tokens.select_next()

            bool_expression = Parser().parse_bool_expression() # bool_expression ?
            block_if        = Parser().block()                 # Sem select next entre os dois?

            # Nó do tipo if :
            node_if = If(value=functions._Type.IF)
            node_if.add_child(bool_expression)
            node_if.add_child(block_if)

            if(tokens.next.type == functions._Type.ELSE): # Bloco else : 3 filhos
                tokens.select_next()
                block_else = Parser().block()
                node_if.add_child(block_else)

            node = node_if

        elif (tokens.next.type == functions._Type.FOR):
            tokens.select_next()
            init_state = Parser().parser_assigment()

            if(tokens.next.type == delimiters._Type.SEMICOLON):
                tokens.select_next()
                condition = Parser().parse_bool_expression()

                if (tokens.next.type == delimiters._Type.SEMICOLON):
                    tokens.select_next()
                    incremet = Parser().parser_assigment()
                    block    = Parser().block()

                    node_for = For(value = functions._Type.FOR)
                    node_for.add_child(init_state)
                    node_for.add_child(condition)
                    node_for.add_child(incremet)
                    node_for.add_child(block)

                    node = node_for

                else:
                    raise InvalidToken(f"\n [STATEMENT] Expected semicolon type | Got : {tokens.next.type}")
            else:
                raise InvalidToken(f"\n [STATEMENT] Expected semicolon type | Got : {tokens.next.type}")
        elif (tokens.next.type == functions._Type.VAR):
            # Var | identifier | type | = BExpression
            tokens.select_next()

            if (tokens.next.type == identifier._Type.IDENTIFIER):

                node_identifier = Identifier(value=tokens.next.value)
                tokens.select_next()

                # --------- Type ---------
                if (tokens.next.type == types.TYPE_INT or tokens.next.type == types.TYPE_STR):
                    _type = tokens.next.type

                    # Add children
                    var_dec_node = VarDec(value=_type)
                    var_dec_node.add_child(node_identifier)

                    # Caso tenha 2° filho:
                    tokens.select_next()
                    if (tokens.next.type == operators._Type.EQUAL):
                        tokens.select_next()
                        bool_expression = Parser().parse_bool_expression()
                        var_dec_node.add_child(bool_expression)

                    node = var_dec_node

                else:
                    raise InvalidExpression(f"\n [STATEMENT] Expected 'type' type | Got {tokens.next}")
            else:
                raise InvalidExpression(f"\n [STATEMENT] Expected identifier type | Got {tokens.next}")

        elif (tokens.next.type == functions._Type.RETURN):
            tokens.select_next()

            bool_expression = Parser().parse_bool_expression()
            node_return = Return(value='RETURN')
            node_return.add_child(bool_expression)

            node = node_return

        else:
            raise InvalidToken(f"\n [STATEMENT] Token type received : {tokens.next.type}")

        # Obriga consumo de \n após essas estruturas
        if(tokens.next.type != eof._Type.EOF):
            if (tokens.next.type == delimiters._Type.END_OF_LINE):
                tokens.select_next()
            else:
                raise InvalidToken(f"\n [STATEMENT] Expected END OF LINE after a statement , got: {tokens.next.type}")

        return node

    @staticmethod
    def block() -> Node:

        node_block = Block(value='BLOCK')
        tokens = Parser().tokenizer

        if (tokens.next.type == delimiters._Type.OPEN_KEY):
            tokens.select_next()

            if (tokens.next.type == delimiters._Type.END_OF_LINE):
                tokens.select_next()

                while(tokens.next.type != delimiters._Type.CLOSE_KEY):
                    state = Parser().parser_statement()
                    node_block.add_child(state)

                if(tokens.next.type == delimiters._Type.CLOSE_KEY):
                    tokens.select_next()
                else:
                    raise InvalidExpression(f"\n [BLOCK] Expected CLOSE KEY type | Got {tokens.next}")

                return node_block
            else:
                raise InvalidExpression(f"\n [BLOCK] Expected END OF LINE type | Got {tokens.next}")

    @staticmethod
    def parser_declaration() -> Node:
        args_list = []

        node_funcdec = FuncDec(value='FUNCDEC')
        tokens = Parser().tokenizer

        if (tokens.next.type == functions._Type.FUNC):
            tokens.select_next()

            if(tokens.next.type == identifier._Type.IDENTIFIER):
                function_name = Identifier(value=tokens.next.value)
                tokens.select_next()

                if (tokens.next.type == delimiters._Type.OPEN_PARENTHESES):
                    tokens.select_next()

                    while (tokens.next.type != delimiters._Type.CLOSE_PARENTHESES):

                        # ---- Add argumentos -----
                        if(tokens.next.type == identifier._Type.IDENTIFIER):
                            node_identifier = Identifier(value=tokens.next.value)
                            tokens.select_next()

                            if(tokens.next.type == types.TYPE_INT or tokens.next.type == types.TYPE_STR):
                                _type = tokens.next.type

                                arg = VarDec(value=_type)
                                arg.add_child(node_identifier)
                                args_list.append(arg)

                                tokens.select_next()

                                if (tokens.next.type == delimiters._Type.COMMAN):
                                    tokens.select_next()
                                else:
                                    break

                    if(tokens.next.type == delimiters._Type.CLOSE_PARENTHESES):
                        tokens.select_next()
                    else:
                        raise InvalidExpression(f"\n [DECLARATION] Expected close parentheses type | Got {tokens.next}")

                    if (tokens.next.type == types.TYPE_INT or tokens.next.type == types.TYPE_STR):

                        node_definition = VarDec(value=tokens.next.type)
                        node_definition.add_child(function_name)

                        tokens.select_next()
                        node_block = Parser().block()

                        if (tokens.next.type == delimiters._Type.END_OF_LINE):
                            tokens.select_next() # Consome \n

                            # Add definição da função como filho:
                            node_funcdec.add_child(node_definition)

                            # Add argumentos
                            for arg in args_list:
                                node_funcdec.add_child(arg)

                            # Add bloco de execução da função
                            node_funcdec.add_child(node_block)

                            return node_funcdec
                    else:
                        raise InvalidExpression(f"\n [DECLARE] Expected END OF LINE type | Got {tokens.next}")
        else:
            raise InvalidExpression(f"\n [DECLARE] Expected FUNCDEC type | Got {tokens.next}")

    @staticmethod
    def program() -> Node:

        node_program = Program(value='PROGRAM')
        tokens = Parser().tokenizer

        while (tokens.next.type != "EOF"):
            declaration = Parser().parser_declaration()

            # Consumo um \n no final
            if (tokens.next.type == delimiters._Type.END_OF_LINE):
                tokens.select_next()

            node_program.add_child(declaration)

        tokens.select_next()

        # Add função principal do programa:
        main_function = FuncCall(value='main')
        node_program.add_child(main_function)
        return node_program

    @staticmethod
    def run(code):

        # Instancia tokenizer e seleciona primeiro Token
        Parser().change_atribute_value(code)
        Parser().tokenizer.select_next()

        # Resultado da expressão analisada
        tree = Parser().program()

        # Verifica se o último token é do tipo "EOF"
        if (Parser().tokenizer.next.type != "EOF"):
            raise InvalidExpression(f"\n [RUN] Expected EOF type | Got {Parser().tokenizer.next}")

        return tree