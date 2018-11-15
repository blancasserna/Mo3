#coding: utf-8
num1 = int(input("Indica un nombre:"))
num2 = int(input("Indica un segon nombre:"))
num3 = int(input("Indica un tercer nombre:"))
num4 = int(input("Indica un quart nombre:"))
if (num2 < num1 and num3 < num1 and num4 < num1):
    print(num1)
else:
    if (num1 < num2 and num3 < num2 and num4 < num2):
        print(num2)
    else:
        if (num1 < num3 and num2 < num3 and num4 < num3):
            print(num3)
        else:
            if (num1 < num4 and num2 < num4 and num3 < num4):
                print(num4)
