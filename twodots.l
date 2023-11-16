%{

#include <stdio.h>
#include <string.h>
#include "twodots.tab.h"

void invalidtoken();

%}

%option noyywrap

/* Auxiliary Tokens definition */

numbers             [1-9][0-9]*
identifier          [A-Za-z_][A-Za-z0-9_]*

%%

[ \t\n]         ; /* Ignore spaces and tabs */

"declare"       {return (DECLARE);}

"string"        {return (STR);}
"integer"       {return (INT);}

"create"        {return (CREATE);}
"invoke"        {return (INVOKE);}
"return"        {return (RETURN);}

"if"            {return (IF);}
"else"          {return (ELSE);}
"loop"          {return (LOOP);}
"stdout"        {return (STDOUT);}
"stdin"         {return (STDIN);}

"and"           {return (LOG_AND);}
"or"            {return (LOG_OR);}
"!"             {return (LOG_NOT);}

"+"             {return (PLUS);}
"-"             {return (MINUS);}
"/"             {return (DIV);}
"*"             {return (MULT);}
"="             {return (EQUAL);}

">"             {return (LOG_GT);}
"<"             {return (LOG_LT);}
"=="            {return (LOG_EQ);}

"{"             {return (OPENING_BRACKET);}
"}"             {return (CLOSING_BRACKET);}
"("             {return (OPENING_PARENTHESIS);}
")"             {return (CLOSING_PARENTHESIS);}
":"             {return (TWO_DOTS);}

{numbers}       {return (NUMBER);}
{identifier}    {return (IDENTIFIER);}

.               {invalidtoken(); yyterminate();}

%%

void invalidtoken() {
    printf("Invalid token found!\n");
}
