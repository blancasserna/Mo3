#coding: utf-8
"""Joc de proves
Entrada     Sortida
3           positiu
-2          no positiu
0           positiu"""
numero = int(input("Indica un número qualsevol:"))
if (numero >= 0):
    print("És un número positiu.")
else:
    if (numero < 0):
        print("No és un número positiu.")
