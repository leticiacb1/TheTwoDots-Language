%{
#include <stdio.h>

int yylex(void);
void yyerror(char *c);
%}

/* Special Tokens */
%token NUMBER STRING
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
%token STR INT
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

PROGRAM: DECLARATION;

DECLARATION: CREATE IDENTIFIER '(' expected_arguments ')' TWO_DOTS types EQUAL BLOCK;

arguments_expected: IDENTIFIER types COMMA arguments
                  | IDENTIFIER types
                  ;

types: STR
     | INT
     ;

STATEMENT: assigment
         | print
         | conditional
         | while
         | declare_variable
         | RETURN BOOL_EXPRESSION
         ;

print: STDOUT TWO_DOTS BOOL_EXPRESSION

while: LOOP TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS EQUAL BLOCK;

conditional: IF TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS BLOCK
           | IF TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS BLOCK TWO_DOTS BLOCK
           ;

declare_variable: DECLARE IDENTIFIER TWO_DOTS types
                | DECLARE IDENTIFIER TWO_DOTS types EQUAL BOOL_EXPRESSION
                ;

assigment: IDENTIFIER EQUAL BOOL_EXPRESSION
         | IDENTIFIER OPENING_PARENTHESIS arguments CLOSING_PARENTHESIS
         ;

arguments: BOOL_EXPRESSION COMMA arguments
         | BOOL_EXPRESSION
         ;

BLOCK: OPENING_BRACKET END_OF_LINE statement_list CLOSING_BRACKET;

statement_list : STATEMENT
               | statement_list STATEMENT
               ;

BOOL_EXPRESSION: BOOL_TERM LOG_OR BOOL_EXPRESSION
               | BOOL_TERM
               ;

BOOL_TERM: RL_EXPRESSION LOG_AND BOOL_TERM
         | RL_EXPRESSION
         ;

rel_operator: LOG_EQ
            | LOG_GT
            | LOG_LT
            ;

RL_EXPRESSION: EXPRESSION rel_operator RL_EXPRESSION
             | EXPRESSION
             ;

exp_operator: PLUS
            | MINUS
            | CONCAT
            ;

EXPRESSION: TERM exp_operator EXPRESSION
          | TERM
          ;

term_operator: MULT
             | DIV
             ;

TERM: FACTOR term_operator TERM
    | FACTOR
    ;

unary_operation: PLUS
               | MINUS
               | LOG_NOT
               ;

FACTOR: NUMBER
      | STRING
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