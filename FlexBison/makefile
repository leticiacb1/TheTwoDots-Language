# Compiler and Flags
CC = gcc
CFLAGS = -Wall

# Executable Output
TARGET = twodots
INPUT_FILE = input.td

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
	$(FLEX) -d $(LEX_FILE)

# ------ Bison ------
twodots.tab.c twodots.tab.h: $(BISON_FILE)
	$(BISON) -d $(BISON_FILE)

execute:
	./$(TARGET) < $(INPUT_FILE)

# ------ Clean  ------
clean:
	rm -f $(TARGET) lex.yy.c twodots.tab.c twodots.tab.h