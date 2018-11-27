#coding: utf-8
divident = int(input("Indica un nombre:"))
divisor = int(input("Indica un segon nombre:"))
quocient = (divident/divisor)
residu = quocient-abs(int(quocient))
if (residu == 0 ):
    print("La divisió és exacte.")
else: 
    if (residu != 0 ):
        print("La divisió no és exacte.")
