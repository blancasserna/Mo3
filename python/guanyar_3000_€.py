# coding: utf-8
loteria = input("Indica si te ha tocado la loteria:")
if (loteria == "si"):
    print("Guanyaré 3000 euros al mes")
else:
    milloneti = input("Et cases amb un/a milloneti?:")
    edat = int(input("Indique su edad:"))
    casat = input("Indica si estas casat/a:")
    problema_cor = input("Indica si tens problemes de cor:")
    if (edat >= 80) and (problemas_cor == "si") and (casat == "si"):
        print("Guanyaré 3000 euros al mes")
    else:
        nota_MO1 = int(input("Indica la teva nota del Mo1:"))
        nota_MO2 = int(input("Indica la teva nota del Mo2:"))
        nota_MO3 = int(input("Indica la teva nota del Mo3:"))
        nota_MO5 = int(input("Indica la teva nota del Mo5:"))
	if ((nota_MO1 >=9 and (nota_MO2 >=10) and (nota_MO3 >=8) and (nota_MO5 >=6 and nota_MO5 <= 8)):
	    print("Guanyaré 3000 euros al mes!")
	else:
	    mitja = (nota_MO1*0.3)+(nota_MO2*0.4)+(nota_MO3*0.25)+(nota_MO5*0.05)
	    if (mitja >=8):
	        print("Guanyaré 3000 euros al mes!")
	    else:
	        print("No guanyaré 3000 euros al mes.")




