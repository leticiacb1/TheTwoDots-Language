declare x:integer = 1
declare y:string

if : ( x > 2 ) {
    stdout : "Hello World"
}

loop : (!2)  {
    x = stdin()
    declare b: integer = 2
}


x = 2
declare w : integer = 1
declare a : string = "Testando"

create main () : integer = {
    return 1
}

y = invoke : main()

create ok ( integer x) : integer = {
    return 1
}

invoke : ok(x)