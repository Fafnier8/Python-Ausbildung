import math

# Berechnung von Widerstand, Elektrischer Leistung und Elektrischer Arbeit mit Fehlerbehandlung (Aufgabe 8b))

try:

    U = float(input("Geben Sie die Spannung in Volt ein: \n"))
    I = float(input("Geben Sie die Stromstärke in Ampere ein: \n"))
    t = float(input("Geben Sie die Zeit in Sekunden an in der die Arbeit geleistet wird: \n"))

    R = U / I

    P = U * I

    W = P * t


    print("Der elektrische Widerstand beträgt: {0:.2f} Ohm".format(R))

    print("Die elektrische Leistung beträgt: {0:.2f} Watt".format(P))

    print("Die elektrische Arbeit, die in {0} s geleistet wurde, beträgt: {1:.2f} Ws".format(t, W))


except Exception as e:
    print("Es ist der folgende Fehler aufgetreten: \n" + e.args[0])


#  Berechnung der Zeit in Minuten bei Eingabe von Datenmenge in MB und Datenübertragungsrate in kbit/s 


