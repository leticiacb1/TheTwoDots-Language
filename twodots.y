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
         | /* VAZIO */
         ;

/* ---------
    BLOCK
    --------- */
BLOCK: OPENING_BRACKET END_OF_LINE statement_list CLOSING_BRACKET


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
      |
      ;

/* --------------------------------------------
                    Auxiliar
    -------------------------------------------- */

/* ----- Auxiliar statement list ----- */
statement_list : STATEMENT
               | statement_list STATEMENT

/* ----- Variable ----- */
types : INT;
declare_variable: DECLARE IDENTIFIER TWO_DOTS types
                | DECLARE IDENTIFIER TWO_DOTS types EQUAL BOOL_EXPRESSION
                ;

/* ----- Print ----- */
print: STDOUT TWO_DOTS BOOL_EXPRESSION;

/* ----- Conditional ----- */
conditional: IF TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS BLOCK
           | IF TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS BLOCK TWO_DOTS BLOCK
           ;

/* ----- Loop ----- */
while: LOOP TWO_DOTS OPENING_PARENTHESIS BOOL_EXPRESSION CLOSING_PARENTHESIS EQUAL BLOCK;

/* ----- Assigment ----- */
assigment: IDENTIFIER EQUAL BOOL_EXPRESSION;

/* ----- Function ----- */
function_declaration: CREATE IDENTIFIER OPENING_PARENTHESIS expected_function_arguments CLOSING_PARENTHESIS TWO_DOTS types EQUAL BLOCK;
function_call : INVOKE TWO_DOTS IDENTIFIER OPENING_PARENTHESIS invoke_function_arguments CLOSING_PARENTHESIS;

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