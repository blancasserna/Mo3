#coding: utf-8
divident = int(input("Indica un nombre:"))
divisor = int(input("Indica un segon nombre:"))
if (divisor == 0) or (divident == 0):
    print("El divisor o divident no poden ser 0.")
else:
    quocient = (divident/divisor)
    residu = divident % divisor  
    if (residu == 0 ):
        print("La divisió és exacte.")
    else: 
        if (residu != 0 ):
            print("La divisió no és exacte.")    
