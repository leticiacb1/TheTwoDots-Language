%{
#include <stdio.h>
#include <string.h>

#include "twodots.tab.h"

void invalidtoken();
%}

%option yylineno
%option noyywrap

numero		[1-9][0-9]*
alpha       \"([^\\\"]|\\.)*\"
identifier  [A-z_][A-z0-9_]*

%%

[\t ]+          {printf("\n [LEX] ESPACO \n");}/* Ignore spaces and tabs */

{numero}        {yylval = atof(yytext); printf("\n [LEX] Number =  %d\n", yylval); return NUMBER;}

"+"             {printf("\n [LEX] PLUS =  %s\n", yytext); return PLUS;}
"-"             {printf("\n [LEX] MINUS =  %s\n", yytext); return MINUS;}
"/"             {printf("\n [LEX] DIV =  %s\n", yytext); return DIV;}
"*"             {printf("\n [LEX] MULT =  %s\n", yytext); return MULT;}
"="             {printf("\n [LEX] EQUAL =  %s\n", yytext); return EQUAL;}

">"             {printf("\n [LEX] GT =  %s\n", yytext); return LOG_GT;}
"<"             {printf("\n [LEX] LT =  %s\n", yytext); return LOG_LT;}
"=="            {printf("\n [LEX] LG_EQUAL =  %s\n", yytext); return LOG_EQ;}

"and"           {printf("\n [LEX] AND =  %s\n", yytext); return LOG_AND;}
"or"            {printf("\n [LEX] OR =  %s\n", yytext); return LOG_OR;}
"!"             {printf("\n [LEX] NOT =  %s\n", yytext); return LOG_NOT;}

"declare"       {printf("\n [LEX] DECLARE =  %s\n", yytext); return DECLARE;}
"integer"       {printf("\n [LEX] INT =  %s\n", yytext); return INT;}
"string"        {printf("\n [LEX] STR =  %s\n", yytext); return STR;}

"create"        {printf("\n [LEX] CREATE =  %s\n", yytext); return CREATE;}
"invoke"        {printf("\n [LEX] INVOKE =  %s\n", yytext); return INVOKE;}
"return"        {printf("\n [LEX] RETURN =  %s\n", yytext); return RETURN;}

"if"            {printf("\n [LEX] IF =  %s\n", yytext); return IF;}
"else"          {printf("\n [LEX] ELSE =  %s\n", yytext); return ELSE;}
"loop"          {printf("\n [LEX] LOOP =  %s\n", yytext); return LOOP;}
"stdout"        {printf("\n [LEX] PRINT =  %s\n", yytext); return STDOUT;}
"stdin"         {printf("\n [LEX] INPUT =  %s\n", yytext); return STDIN;}

"{"             {printf("\n [LEX] DELIMITER =  %s\n", yytext); return OPENING_BRACKET;}
"}"             {printf("\n [LEX] DELIMITER =  %s\n", yytext); return CLOSING_BRACKET;}
"("             {printf("\n [LEX] DELIMITER =  %s\n", yytext); return OPENING_PARENTHESIS;}
")"             {printf("\n [LEX] DELIMITER =  %s\n", yytext); return CLOSING_PARENTHESIS;}

":"             {printf("\n [LEX] DELIMITER =  %s\n", yytext); return TWO_DOTS;}
","             {printf("\n [LEX] DELIMITER =  %s\n", yytext); return COMMA;}

{identifier}    {printf("\n [LEX] IDENTIFIER =  %s\n", yytext); return IDENTIFIER;}
{alpha}         {printf("\n [LEX] ALPHA =  %s\n", yytext); return ALPHA;}

"#".*           {printf("\n [LEX] COMENTARIO \n");}    /* Ignore comentario */
"\n"            {printf("\n [LEX] END OF LINE", yytext); return END_OF_LINE;}
[|\n]		    return yytext[0];

.               {invalidtoken(); yyterminate();}

%%

void invalidtoken() {
    printf("Invalid token found!\n");
}