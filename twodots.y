%{
#include <stdio.h>

int yylex(void);
int yyparse(void);
void yyerror(const char *);
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
%token IF ELSE LOOP STDOUT STDIN

%left PLUS MINUS
%left MULT DIV
%nonassoc UMINUS

%start PROGRAM

%%

PROGRAM: STATEMENT  END_OF_LINE PROGRAM
       | STATEMENT  END_OF_LINE
       | STATEMENT
       ;

statement_list : STATEMENT
               | statement_list STATEMENT

BLOCK: OPENING_BRACKET END_OF_LINE statement_list CLOSING_BRACKET
types : INT;

declare_variable: DECLARE IDENTIFIER TWO_DOTS types;
print: STDOUT TWO_DOTS BOOL_EXPRESSION;
conditional: IF TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS BLOCK
           | IF TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS BLOCK TWO_DOTS BLOCK
           ;
while: LOOP TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS EQUAL BLOCK;
assigment: IDENTIFIER EQUAL BOOL_EXPRESSION;

function_declaration: CREATE IDENTIFIER OPENING_PARENTHESIS  CLOSING_PARENTHESIS TWO_DOTS types EQUAL BLOCK;
function_call : INVOKE TWO_DOTS IDENTIFIER OPENING_PARENTHESIS  CLOSING_PARENTHESIS;

STATEMENT: declare_variable
         | conditional
         | print
         | while
         | assigment
         | function_declaration
         | function_call
         | /* VAZIO */
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

FACTOR: NUMBER
      |
      ;

%%

int main()
{
	yyparse();
}

void yyerror(const char *s) {
    extern int yylineno;
    extern char *yytext;

    /* mensagem de erro exibe o símbolo que causou erro e o número da linha */
    printf("\nErro (%s): símbolo \"%s\" (linha %d)\n", s, yytext, yylineno);
}