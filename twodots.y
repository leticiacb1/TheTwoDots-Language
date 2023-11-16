/* Imports */
%{
#include <stdio.h>

/* Function Declaration */
int yylex(void);
void yyerror(char *c);

%}

/* ------- Tokens ------- */

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
%token TWO_DOTS

/* Reserved Word */
%token DECLARE
%token STR INT
%token INVOKE CREATE RETURN
%token IF ELSE LOOP STDOUT STDIN

/* ------- Priority -------

    Lowest priority
          |
    Highest priority
*/
%left PLUS MINUS
%left MULT DIV
%left LOG_NOT

%nonassoc UMINUS
%nonassoc UPLUS

%start program

%%

/* ------- Rules ------- */

/* PROGRAM */
PROGRAM : DECLARATION
        | PROGRAM DECLARATION



%%

/* ------- Functions ------- */

void yyerror(char *c) {
    printf("Erro: %s\n", c);
}

int main() {
    yyparse();
    return 0;
}