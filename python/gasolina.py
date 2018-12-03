# coding:utf-8
print("1.Super: Normal: 1.5euros o Turbo: 1.55euros")
print("2.Sin plomo: Normal:1.6euros o Con aditivos (sabor naranja): 1.65euros")
print("3.Diesel: Normal: 1.7euros o Fast&Furius: 1.75euros")
gasolina = input("Que gasolina quiere?")
tipo = input("Indique el tipo que quiere:")
litros = int(input("Indique cuantos litros quiere:"))
if (gasolina == "super" and tipo == "normal"):
    tipo_1 = litros * 1.5
    print("En total seran" ,tipo_1, "€.")
else:
    if (gasolina == "super" and tipo == "turbo"):
        tipo_2 = litros * 1.55
        print("En total seran" ,tipo_2, "€.")
    else:
        if (gasolina == "sense plom" and tipo == "normal"):
            tipo_3 = litros * 1.6
            print("En total seran" ,tipo_3)
        else:
            if (gasolina == "sense plom" and tipo == "amb aditius"):
                tipo_4 = litros * 1.65
                print("En total seran" ,tipo_4, "€.")
            else:
                if (gasolina == "diesel" and tipo == "normal"):
                    tipo_5 = litros * 1.7
                    print("En total seran" ,tipo_5, "€.")
                else:
                    if (gasolina == "diesel" and tipo == "fast&furius"):
                        tipo_6 = litros * 1.75
                        print("En total seran" ,tipo_6, "€.")
