create main() : integer = {
    declare i : integer = 0

    declare j : string = "Valores de i no loop :"
    stdout : j

    loop : ( i < 5) {
      i  = i + 1

      stdout : i
    }
}