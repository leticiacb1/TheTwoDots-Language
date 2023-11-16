%{

/* Imports */
#include <iostream>
#include <cctype>
using namespace std;

/* Function Declaration */
int yylex(void);
void yyerror(char *c);

%}

/* ------- Tokens ------- */

/* Separators */
%token TWO_POINTS

/* Arithmetic Operations */
%token PLUS MINUS MULT DIV EQUAL

/* Logical Operations */
%token LOG_GT LOG_LT LOG_EQ LOG_NOT

/* Delimiters */
%token OPENING_PARENTHESIS CLOSING_PARENTHESIS
%token OPENING_BRACKET CLOSING_BRACKET

/* Reserved Word */
%token DECLARE
%token STR INT
%token INVOKE CREATE
%token IF ELSE LOOP STDOUT STDIN

%%

/* ------- Rules ------- */

fact: DIGIT
    ;


%%

/* ------- Functions ------- */

void yyerror(char *c) {
    printf("Erro: %s\n", c);
}

int main() {
    yyparse();
    return 0;
}