#######################################################################
##                          Übungsprogramm                           ##
#######################################################################
ergebnis = False

while ergebnis == False:

    passwort = open('0001.txt' , 'r')
    zeile = passwort.readline()
    eingabe = input("Geben Sie Ihr Passwort ein: ")
    passwort.close()
    if eingabe == zeile:
        ergebnis = True
    else:
        print("Falsch!")
print("Richtig!")
input("Ende")