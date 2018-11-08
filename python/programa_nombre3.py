#coding: utf-8
"""Joc de proves:
Entrada     Sortida
2  3        2  3
3  2        2  3
8 -6        -6 8
2  2        2  2 """

nombre1 = int(input("Indica un nombre:"))
nombre2 = int(input("Indica un altre nombre:"))
if (nombre1 < nombre2):
    print(nombre1,nombre2)
else:
    if (nombre1 > nombre2):
        print(nombre1,nombre2)
    else:
        if (nombre1 = nombre2):
            print(nombre1,nombre2)
