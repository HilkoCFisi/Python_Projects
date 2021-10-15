import time
from winsound import Beep
Tacktzahl = input("Wie viele Tackte hat das Lied? ")
Schlagzahl = input("Wie viele Schläge hat ein Tackt? ")
bpm = input("Wie viel BPM hat das Lied? ")
frequencyhigh = 700
frequency = 500
duration = 1000/(int(bpm)/60)
Tackt = 1

while Tackt <int(Tacktzahl) +1:
    Schlag = 1
    print("Tackt: " , Tackt)
    while Schlag <int(Schlagzahl) + 1:
        print("\tSchlag: " , Schlag)
        if Schlag == 1:
            Beep( frequencyhigh, int(duration) )
        else:
            Beep( frequency, int(duration))
        Schlag = Schlag + 1
        #time.sleep(float(duration/1000)) #I'm not sure, if i should delete this line. Could cause the Program to run half as fast, as it should.
    Tackt = Tackt + 1
input("Enter zum Beenden")