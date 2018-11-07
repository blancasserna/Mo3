# coding: utf-8
any_actual = int(input("Indica l'any actual:"))
any_qualsevol = int(input("Indica un any qualsevol:"))
if (any_actual == any_qualsevol):
    print("És el mateix any!")
else:
    res = (any_actual) - (any_qualsevol)
    if (any_actual > any_qualsevol):
        print("Desde l'any", any_qualsevol,"han passat", res,"anys!")
    else:
        res = (any_qualsevol) - (any_actual)
        if (any_qualsevol > any_actual):
            print("Per arrivar a l'any", any_qualsevol,"falten", res,"anys!")
