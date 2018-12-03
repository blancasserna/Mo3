# Versió 1
""" Llegeix un nombre del teclat si el nombre és:
- Par
- Negatiu
- Entre -10 i 40 """

#coding: utf-8
num_teclat = int(input(""))
if ((num_teclat % 2 == 0) and (num_teclat > -11) and (num_teclat < 0)):
    print(num_teclat)
else:
    print("No es pot llegir.")

# Versió 2
""" Lee un número del teclado
Si es:
-par
-entre -10 y 40
-negativo """

#coding: utf-8
num_teclat = int(input("Escriu un número del teclat:"))
if (num_teclat % 2 == 0):
    print(,num_teclat, "és un nombre par")
else:
    if (num_teclat > -10 and num_teclat < 40):
        print(,num_teclat, "està entre el -10 i el 40")
    else:
        if (num_teclat < 0):
            print(,num_teclat, "és negatiu")
