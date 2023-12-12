create main() : integer = {
    # Declarando variáveis
    declare x : integer = 2
    declare y : string = "y"

    declare w : integer
    declare z : integer

    z = 10 *1 --2 /2    # z = 11

    w = stdin()
    stdout : " Valor de w : "
    stdout : w

    if : ( z == 11 ) {
      # Bloco if
      stdout : " Z é igual a 11"
    }
}