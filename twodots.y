%{
#include <stdio.h>

int yylex(void);
void yyerror(char *c);
%}

/* Special Tokens */
%token NUMBER
%token IDENTIFIER

/* Arithmetic Operations */
%token PLUS MINUS MULT DIV EQUAL

/* Logical Operations */
%token LOG_GT LOG_LT LOG_EQ LOG_NOT LOG_AND LOG_OR

/* Delimiters */
%token OPENING_PARENTHESIS CLOSING_PARENTHESIS
%token OPENING_BRACKET CLOSING_BRACKET
%token TWO_DOTS COMMA END_OF_LINE

/* Reserved Word */
%token DECLARE
%token INT
%token INVOKE CREATE RETURN
%token IF ELSE LOOP STDOUT STDIN CONCAT

/* Priority */
%left PLUS MINUS
%left MULT DIV
%left LOG_NOT

%nonassoc UMINUS
%nonassoc UPLUS

%start PROGRAM

%%

types: INT;

function_declaration: CREATE IDENTIFIER '(' arguments_expected ')' TWO_DOTS types EQUAL BLOCK;

arguments_expected: IDENTIFIER types COMMA arguments_expected
                  | IDENTIFIER types
                  ;

print: STDOUT TWO_DOTS BOOL_EXPRESSION

while: LOOP TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS EQUAL BLOCK;

conditional: IF TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS BLOCK
           | IF TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS BLOCK TWO_DOTS BLOCK
           ;

declare_variable: DECLARE IDENTIFIER TWO_DOTS types
                | DECLARE IDENTIFIER TWO_DOTS types EQUAL BOOL_EXPRESSION
                ;

return_function_value: RETURN BOOL_EXPRESSION

assigment: IDENTIFIER EQUAL BOOL_EXPRESSION
         | IDENTIFIER OPENING_PARENTHESIS arguments CLOSING_PARENTHESIS
         ;

arguments: BOOL_EXPRESSION COMMA arguments
         | BOOL_EXPRESSION
         ;

statement_list : STATEMENT
               | statement_list STATEMENT
               ;

rel_operator: LOG_EQ
            | LOG_GT
            | LOG_LT
            ;

exp_operator: PLUS
            | MINUS
            | CONCAT
            ;

term_operator: MULT
             | DIV
             ;

unary_operation: PLUS
               | MINUS
               | LOG_NOT
               ;

PROGRAM: STATEMENT;

STATEMENT: assigment END_OF_LINE
         | print END_OF_LINE
         | conditional END_OF_LINE
         | while END_OF_LINE
         | declare_variable END_OF_LINE
         | function_declaration END_OF_LINE
         | return_function_value END_OF_LINE
         | END_OF_LINE;

BLOCK: OPENING_BRACKET END_OF_LINE statement_list CLOSING_BRACKET;

BOOL_EXPRESSION: BOOL_TERM LOG_OR BOOL_EXPRESSION
               | BOOL_TERM
               ;

BOOL_TERM: RL_EXPRESSION LOG_AND BOOL_TERM
         | RL_EXPRESSION
         ;

RL_EXPRESSION: EXPRESSION rel_operator RL_EXPRESSION
             | EXPRESSION
             ;

EXPRESSION: TERM exp_operator EXPRESSION
          | TERM
          ;

TERM: FACTOR term_operator TERM
    | FACTOR
    ;

FACTOR: NUMBER
      | IDENTIFIER OPENING_PARENTHESIS arguments CLOSING_PARENTHESIS
      | unary_operation FACTOR
      | OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS
      | STDIN OPENING_PARENTHESIS CLOSING_PARENTHESIS
      ;

%%

/*  Functions */

void yyerror(char *c) {
    printf("Erro: %s\n", c);
}

int main() {
    yyparse();
    return 0;
}