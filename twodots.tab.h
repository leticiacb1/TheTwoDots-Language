/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_TWODOTS_TAB_H_INCLUDED
# define YY_YY_TWODOTS_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    NUMBER = 258,                  /* NUMBER  */
    IDENTIFIER = 259,              /* IDENTIFIER  */
    PLUS = 260,                    /* PLUS  */
    MINUS = 261,                   /* MINUS  */
    MULT = 262,                    /* MULT  */
    DIV = 263,                     /* DIV  */
    EQUAL = 264,                   /* EQUAL  */
    LOG_GT = 265,                  /* LOG_GT  */
    LOG_LT = 266,                  /* LOG_LT  */
    LOG_EQ = 267,                  /* LOG_EQ  */
    LOG_NOT = 268,                 /* LOG_NOT  */
    LOG_AND = 269,                 /* LOG_AND  */
    LOG_OR = 270,                  /* LOG_OR  */
    OPENING_PARENTHESIS = 271,     /* OPENING_PARENTHESIS  */
    CLOSING_PARENTHESIS = 272,     /* CLOSING_PARENTHESIS  */
    OPENING_BRACKET = 273,         /* OPENING_BRACKET  */
    CLOSING_BRACKET = 274,         /* CLOSING_BRACKET  */
    TWO_DOTS = 275,                /* TWO_DOTS  */
    COMMA = 276,                   /* COMMA  */
    END_OF_LINE = 277,             /* END_OF_LINE  */
    DECLARE = 278,                 /* DECLARE  */
    INT = 279,                     /* INT  */
    INVOKE = 280,                  /* INVOKE  */
    CREATE = 281,                  /* CREATE  */
    RETURN = 282,                  /* RETURN  */
    IF = 283,                      /* IF  */
    ELSE = 284,                    /* ELSE  */
    LOOP = 285,                    /* LOOP  */
    STDOUT = 286,                  /* STDOUT  */
    STDIN = 287,                   /* STDIN  */
    CONCAT = 288,                  /* CONCAT  */
    UMINUS = 289,                  /* UMINUS  */
    UPLUS = 290                    /* UPLUS  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_TWODOTS_TAB_H_INCLUDED  */
