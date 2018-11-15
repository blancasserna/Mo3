#coding: utf-8
num1 = int(input("Indica un nombre:"))
num2 = int(input("Indica un segon nombre:"))
num3 = int(input("Indica un tercer nombre:"))
if (num1 < num2 and num3 < num2):
    print(num2)
else:
    if(num1 < num3 and num2 < num3):
        print(num3)
    else:
        print(num1)        
