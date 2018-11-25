# coding:utf-8

for primer_rang in range(0, 100):
    print("Volta nº" , primer_rang + 1)
    print("Premeu qualsevol tecla per continuar")
    for segon_rang in range(100, 200):
        print("Volta nº" , segon_rang + 1)
        print("Premeu qualsevol tecla per continuar")
        for tercer_rang in range(200, 300):
            print("Volta nº" , tercer_rang + 1)
            print("Premeu qualsevol tecla per continuar")
            for quart_rang in range(300, 365):
                print("Volta nº" , quart_rang + 1)
                print("Premeu qualsevol tecla per continuar")
    if (num_dia % 365) == (350-1):
        print("*")
