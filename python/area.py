#coding: utf-8
lletra = input("Indica de quina figura vols calcular l'àrea:")
if ( lletra == "T" ):
    base = float(input("Indica la base del triangle:"))
    altura = float(input("Indica l'alçada del triangle:"))
    area_triangle = (base * altura)/2
    print("L'àrea del triangle és" ,area_triangle)
else:
    if ( lletra == "C"):
        radi = float(input("Indica el radi del cercle:"))
        area_cercle = (radi * radi * 3.1415)
        print("L'àrea del cercle és" ,area_cercle)
