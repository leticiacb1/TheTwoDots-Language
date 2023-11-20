%{

#include <stdio.h>
#include <string.h>
#include "twodots.tab.h"

void invalidtoken();

%}

%option noyywrap

/* Auxiliary Tokens definition */

%%

\n            {return END_OF_LINE;}

"declare"       {return DECLARE;}
"integer"       {return INT;}

"create"        {return CREATE;}
"invoke"        {return INVOKE;}
"return"        {return RETURN;}

"if"            {return IF;}
"else"          {return ELSE;}
"loop"          {return LOOP;}
"stdout"        {return STDOUT;}
"stdin"         {return STDIN;}
"concat"        {return CONCAT;}

"and"           {return LOG_AND;}
"or"            {return LOG_OR;}
"!"             {return LOG_NOT;}

"+"             {return PLUS;}
"-"             {return MINUS;}
"/"             {return DIV;}
"*"             {return MULT;}
"="             {return EQUAL;}

">"             {return LOG_GT;}
"<"             {return LOG_LT;}
"=="            {return LOG_EQ;}

"{"             {return OPENING_BRACKET;}
"}"             {return CLOSING_BRACKET;}
"("             {return OPENING_PARENTHESIS;}
")"             {return CLOSING_PARENTHESIS;}

":"             {return TWO_DOTS;}
","             {return COMMA;}

[1-9][0-9]*     {return NUMBER;}
[A-z_][A-z0-9_]*    {return IDENTIFIER;}

[ \t]           /* Ignore spaces and tabs */

.               {invalidtoken(); yyterminate();}

%%

void invalidtoken() {
    printf("Invalid token found!\n");
}