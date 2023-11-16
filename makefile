# Compiler and Flags
CC = gcc
CFLAGS = -Wall

# Executable Output
TARGET = twodots

# Source files
LEX_FILE = twodots.l
BISON_FILE = twodots.y

# Flex and Bison
FLEX = flex
BISON = bison

# ------ Build ------
all: $(TARGET)

$(TARGET): lex.yy.c twodots.tab.c
    $(CC) $(CFLAGS) -o $(TARGET) lex.yy.c twodots.tab.c


# ------ Flex ------
lex.yy.c: $(LEX_FILE) twodots.tab.h
	$(FLEX) $(LEX_FILE)

# ------ Bison ------
parser.tab.c parser.tab.h: $(BISON_FILE)
    $(BISON) -d $(BISON_FILE)

# ------ Clean  ------
clean:
    rm -f $(TARGET) lex.yy.c twodots.tab.c twodots.tab.h
