# Criando uma função
create soma ( x : integer , y : integer ) : integer = {
  stdout : "\n Valor de x : "
  stdout : x

  stdout : "\n Valor de y : "
  stdout : y

  return x + y
}

# Usando a função
declare x : integer = 2;
declare y : integer = 4;

declare z = invoke : soma(x,y)

stdout : "\n Valor de z : "
stdout : z