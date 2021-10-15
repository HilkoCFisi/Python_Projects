import secrets
groß = "QWERTZUIOPASDFGHJKLYXCVBNM"
klein = "qwertzuiopasdfghjklyxcvbnm"
zahl = "1234567890"
sonder = "!§$%&=?@"
neu = "y"
while neu == "y":
    pw = ""
    length = int(input("Wie viele Zeichen soll das Passwort haben? "))
    for _ in range(length):
        pw = pw+secrets.choice(groß + klein + str(zahl) + sonder)
    print(pw)
    speichern = input("Passwort speichern? Ja = y | Nein = n | Eingabe: ")
    if speichern == "y":
        datei = open('0001.txt', 'w')
        datei.write(pw)
        break
    elif speichern == "n":   
        neu = input("Neues Passwort generieren? Ja = y | Nein = n | Eingabe: ")
    else: print("Ungültige Eingabe")
input("Drücke Enter zum schleßen.")

