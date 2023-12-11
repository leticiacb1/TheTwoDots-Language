%{
#include <stdio.h>

int yylex(void);
int yyparse(void);
void yyerror(const char *);
%}

/* Special Tokens */
%token NUMBER ALPHA
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
%token INT STR BOOL
%token INVOKE CREATE RETURN
%token IF ELSE LOOP STDOUT STDIN

%left PLUS MINUS
%left MULT DIV
%nonassoc UMINUS

%start PROGRAM

%%

/* ---------
    PROGRAM
    --------- */
PROGRAM: STATEMENT  END_OF_LINE PROGRAM
       | STATEMENT  END_OF_LINE
       | STATEMENT
       ;

/* ---------
    STATEMENT
    --------- */
STATEMENT: declare_variable
         | conditional
         | print
         | while
         | assigment
         | function_declaration
         | function_call
         | BOOL_EXPRESSION
         | /* VAZIO */
         ;

/* ---------
    BLOCK
    --------- */
BLOCK: OPENING_BRACKET END_OF_LINE statement_list CLOSING_BRACKET;
FUNCTION_BLOCK: OPENING_BRACKET END_OF_LINE statement_list function_return END_OF_LINE CLOSING_BRACKET;

/* -----------------
    BOOL_EXPRESSION
   ----------------- */
BOOL_EXPRESSION: BOOL_TERM LOG_OR BOOL_EXPRESSION
               | BOOL_TERM
               ;
/* -----------
    BOOL_TERM
   ----------- */
BOOL_TERM: RL_EXPRESSION LOG_AND BOOL_TERM
         | RL_EXPRESSION
         ;

/* ----------------
    RL_EXPRESSION
   ---------------- */
RL_EXPRESSION: EXPRESSION rel_operator RL_EXPRESSION
             | EXPRESSION
             ;

/* -----------
    EXPRESSION
   ----------- */
EXPRESSION: TERM exp_operator EXPRESSION
          | TERM
          ;

/* --------
    TERM
   -------- */
TERM: FACTOR term_operator TERM
    | FACTOR
    ;

/* --------
    FACTOR
   -------- */
FACTOR: NUMBER
      | ALPHA
      | IDENTIFIER
      | function_call
      | unary_operation FACTOR
      | OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS
      | input
      ;

/* --------------------------------------------
                    Auxiliar
    -------------------------------------------- */

/* ----- Auxiliar statement list ----- */
statement_list : STATEMENT
               | statement_list END_OF_LINE STATEMENT
               | statement_list END_OF_LINE STATEMENT END_OF_LINE
               ;

/* ----- Variable ----- */
types : INT
      | STR
      | BOOL
      ;

declare_variable: DECLARE IDENTIFIER TWO_DOTS types
                | DECLARE IDENTIFIER TWO_DOTS types EQUAL BOOL_EXPRESSION
                ;

/* ----- Print ----- */
print: STDOUT TWO_DOTS BOOL_EXPRESSION;

/* ----- Input ----- */
input: STDIN OPENING_PARENTHESIS CLOSING_PARENTHESIS

/* ----- Conditional ----- */
conditional: IF TWO_DOTS  BOOL_EXPRESSION  BLOCK
           | IF TWO_DOTS  BOOL_EXPRESSION  BLOCK TWO_DOTS BLOCK
           ;

/* ----- Loop ----- */
while: LOOP TWO_DOTS  BOOL_EXPRESSION BLOCK;

/* ----- Assigment ----- */
assigment: IDENTIFIER EQUAL BOOL_EXPRESSION;

/* ----- Function ----- */
function_declaration: CREATE IDENTIFIER OPENING_PARENTHESIS expected_function_arguments CLOSING_PARENTHESIS TWO_DOTS types EQUAL FUNCTION_BLOCK;
function_call: INVOKE TWO_DOTS IDENTIFIER OPENING_PARENTHESIS invoke_function_arguments CLOSING_PARENTHESIS;
function_return: RETURN BOOL_EXPRESSION;

expected_function_arguments: types IDENTIFIER  COMMA expected_function_arguments
                           | types IDENTIFIER
                           | /* SEM ARGUMENTO */
                           ;

invoke_function_arguments: IDENTIFIER COMMA invoke_function_arguments
                         | IDENTIFIER
                         | /* SEM ARGUMENTO */
                         ;

/* ----- Operators ----- */

exp_operator: PLUS
            | MINUS
            ;

term_operator: MULT
             | DIV
             ;

rel_operator: LOG_EQ
            | LOG_GT
            | LOG_LT
            ;

unary_operation: PLUS
               | MINUS
               | LOG_NOT
               ;

%%

int main()
{
	yyparse();
}

void yyerror(const char *s) {
    extern int yylineno;
    extern char *yytext;

    printf("\n [ ERROR ] (%s): token \"%s\" (line %d)\n", s, yytext, yylineno);
}