%{
#include
#include "twoDots.h"
%}

%option noyywrap

/* ------- Auxiliary Tokens definition ------- */

numbers             [1-9][0-9]*
identifier          [A-z_][0-9A-z_]+

%%

/* ------- Return token types ------- */

{numbers}       {return (NUMBER);}
{identifier}    {return (IDENTIFIER);}

/* Arithmetic Operation */

"+"             {return (PLUS);}
"-"             {return (MINUS);}
"/"             {return (DIV);}
"*"             {return (MULT);}
"="             {return (EQUAL);}

/* Logical Operation */

"and"           {return (LOG_AND);}
"or"            {return (LOG_OR);}
"!"             {return (LOG_NOT);}

">"             {return (LOG_GT);}
"<"             {return (LOG_LT);}
"=="            {return (LOG_EQ);}

/* Delimiters */

"{"             {return (OPENING_BRACKET);}
"}"             {return (CLOSING_BRACKET);}
"("             {return (OPENING_PARENTHESIS);}
")"             {return (CLOSING_PARENTHESIS);}
":"             {return (TWO_DOTS);}

/* Reserved Word */

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

%%