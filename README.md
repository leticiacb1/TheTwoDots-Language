## TheTwoDots Language

### Variable and Constants Declaration

```python
# Declarando variável
declare x : integer = 2
declare y : string = "y"
declare z : integer

# Declarando constante
constant DELTA : double = 0.1

```
### Math operations
```python

declare x : integer = 2

x = x + 2 

```

### Create function

```python
create function_name ( args ) : integer = {
  stdout : " Nothing here "
  return 0 
}

```

### Invoke function

```python
invoke : function_name( args )

# Take return value of a function

declare x : integer
x = invoke : function_name( args )

```

### Conditional Block
```python

if : ( x == 2) {
  # If block
  stdout : " X é igual a 2" 
} : {
  # Else block
  stdout : "X não é igual a 2"
} 

```

### Loops

```python

declare i : integer = 0

loop : ( i < 5) = {
  i  = i + 1
}

```

### Build-in function

```python

stdout  # Output
stdin   # Input do teclado

```
