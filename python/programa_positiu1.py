#coding: utf-8
"""Joc de proves
Entrada     Sortida
3           positiu
-2          no positiu
0           positiu"""

nombre = int(input("Indica un nombre qualsevol:"))
if (nombre >= 0):
    print("És un nombre positiu.")
else:
    if (nombre < 0):
        print("No és un nombre positiu.")
