create main() : integer = {
    declare i : integer = 0

    stdout : "Valores de i no loop :\n"

    loop : ( i < 5) = {
      i  = i + 1

      stdout : i
      stdout : " "
    }
}