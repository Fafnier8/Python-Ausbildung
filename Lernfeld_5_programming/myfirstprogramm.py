import math


try:

    U = float(input("Geben Sie die Spannung in Volt ein: \n"))
    I = float(input("Geben Sie die Stromstärke in Ampere ein: \n"))

    R = U / I


    print("Der elektrische Widerstand beträgt: {0:.2f} Ohm".format(R))


except Exception as e:
    print("Es ist der folgende Fehler aufgetreten: \n" + e.args[0])


