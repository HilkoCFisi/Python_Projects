#Primzahlrechner
#Import
from ast import While
from time import time
#Variablen
eingabe = int(input('bis zu welcher Zahl soll berechnet werden? '))
zahl = 0
zeit1 = time()

#Schleife
while zahl < eingabe: 
    erg2 = zahl % 2
    erg3 = zahl % 3
    erg4 = zahl % 4
    erg5 = zahl % 5
    erg6 = zahl % 6
    erg7 = zahl % 7
    erg8 = zahl % 8
    erg9 = zahl % 9

    if erg2 > 0 and erg3 > 0 and erg4 > 0 and erg5 > 0 and erg6 > 0 and erg7 > 0 and erg8 > 0 and erg9 > 0:
        print(zahl)
        datei = open('prim.txt' , 'a')
        datei.write(str(zahl)+'\n')
    else: pass
    zahl = zahl +1
zeit2 = time()
dauer = zeit2 - zeit1
print(dauer, ' Sekunden')
datei = open('prim.txt', 'a')
datei.write(str(dauer)+' Sekunden'+'\n')
input('Beliebige Taste zum beenden')