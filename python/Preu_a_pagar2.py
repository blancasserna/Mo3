jubilat = input("Indica si estas jubilat/da:")
sexe = input("Indica el teu sexe:")
cabell = input("Indica el teu color de cabell:")
if (jubilat == "no") and (sexe == "dona") and (cabell == "ros") :
  print ("No pagues")
if (sexe == "home") and (jubilat == "si") :
  print ("Pagues 1 euro")
else:
  print ("No pagues 1 euro")
if (jubilat == "si") :
  print ("Gratis")
else:
  print ("No es gratis")
