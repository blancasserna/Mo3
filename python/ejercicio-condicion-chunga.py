#coding: utf-8
num_teclat = int(input(""))
if ((num_teclat % 2 == 0) and (num_teclat > -11) and (num_teclat < 0)):
    print(num_teclat)
else:
    print("No es pot llegir.")

    
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
