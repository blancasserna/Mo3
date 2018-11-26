# coding:utf-8

for primer_rang in range(0, 100):
    print("Volta nº" , primer_rang + 1)
    if (primer_rang % 100) == (100-1):
        print("Premeu qualsevol tecla per continuar")
        for segon_rang in range(100, 200):
                print("Volta nº" , segon_rang + 1)
                if (segon_rang % 200) == (200-1):
                    print("Premeu qualsevol tecla per continuar")
                    for tercer_rang in range(200, 300):
                        print("Volta nº" , tercer_rang + 1)
                        if (tercer_rang % 300) == (300-1):
                            print("Premeu qualsevol tecla per continuar")
                            for quart_rang in range(300, 365):
                                    print("Volta nº" , quart_rang + 1)
                            
   
for num_dia in range(0, 365):
    print("Volta nº" , num_dia + 1)
    if ((num_dia % 100) == (100-1)):
        print("Premeu qualsevol tecla per continuar")

