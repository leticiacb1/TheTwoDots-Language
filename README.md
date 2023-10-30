## 🐙 The TwoDots Language

Bem-vindo ao emocionante mundo da programação simplificada e intuitiva com a linguagem "TwoDots". 

Como o nome sugere, esta linguagem utiliza extensivamente o caractere ":" para melhorar a legibilidade e a eficiência do seu código. O "TwoDots" foi desenvolvido com o objetivo de tornar a codificação mais acessível e compreensível, especialmente para iniciantes na programação.

Linguagem que se inspira em várias linguagens de programação amplamente conhecidas, buscando incorporar as melhores características de cada uma, enquanto mantém um foco na simplicidade e legibilidade do código. 

Algumas linguagens que foram utilizadas de inspiração : Python , JavaScript , Java , C/C++/C#.

Possíveis linguagens a serem mescladas e trazerem improvementes para a presente linguagem : Whitespace , brainfuck.

## 📌️ Examples of structures

#### Variable and Constants

```python
# Declarando variável
declare x : integer = 2
declare y : string = "y"
declare z : integer

# Declarando constante
constant DELTA : double = 0.1

```
#### Math operations
```python

declare x : integer = 2

x = x + 2 

```

#### Create and use function

```python

# Criando uma função

create function_name ( args ) : integer = {
  stdout : " Nothing here "
  return 0 
}

# Usando função
invoke : function_name()

# Pegando retorno da função
declare x : integer
x = invoke : function_name( args )

```

#### Conditional Block
```python

if : ( x == 2) {
  # If block
  stdout : " X é igual a 2" 
} : {
  # Else block
  stdout : "X não é igual a 2"
} 

```

#### Loops

```python

declare i : integer = 0

loop : ( i < 5) = {
  i  = i + 1
}

```

#### Build-in function

```python

stdout  # Output
stdin   # Input do teclado

```

## 🎯️ EBNF
