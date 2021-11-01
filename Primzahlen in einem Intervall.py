########################
#                      #
#      Primzahlen      #
#   T.Hoppe Nov 2021   #
#                      #
#                      #
########################

import math
import time
import matplotlib.pyplot as plt
from sympy import primepi


def eratosthenes(end):
    end = end + 1
    primzahlliste = [True] * end
    primzahlliste[0] = False
    primzahlliste[1] = False

    for i in range(2, int(math.sqrt(end)) + 1):
        j = i * i
        while j < end:
            primzahlliste[j] = False
            j = j + i
    return [x for x in range(end) if primzahlliste[x] == True]


def primzahlzwillinge(end):
    all_prim = eratosthenes(end)
    twins = []
    for i in range(0, len(all_prim) - 1):
        if all_prim[i + 1] - all_prim[i] == 2:
            twins.append(all_prim[i])
            twins.append(all_prim[i + 1])
    return twins


def eingabeendwert():
    while True:
        try:
            end = int(input("Bitte den Endwert eingeben: "))
            if end <= 1:
                print("\nEndwert mindestens 2...\n")
                continue
            break
        except ValueError:
            print("\nBitte die Zahl im richtigen Format als ganze Zahl eingeben...\n")
    return end


def ausgabeauswertung(sz, sd, z, e, sw, inter):
    ez = time.time()
    d = ez - sz

    print()
    print("Berechnung gestartet am               :", sd)
    print("Berechnung beendet am                 :", time.strftime("%d.%m.%Y um %H:%M:%S"))
    print("Größe des zu untersuchenden Intervalls:", e + 1 - sw, "von", sw, "bis", e)
    if inter is True:
        print("Anzahl in diesem Intervall            :", z)
        print("Anteil in diesem Intervall            :", round((z / (e - 1) * 100), 2), "%")

    if d >= 3600:
        print("Dauer der Berechnung                  :", round(d / 3600, 2), "Stunden")

    if 3600 > d >= 60:
        print("Dauer der Berechnung                  :", round(d / 60, 2), "Minuten")

    if d < 60:
        print("Dauer der Berechnung                  :", round(d, 2), "Sekunden")

    input("\nWeiter mit jeder beliebigen Taste...")
    return


while True:
    print("\nMenü:")
    print("-----")
    print("(1) Ausgabe von Primzahlen in einem definierten Intervall")
    print("(2) Das Sieb des Eratosthenes")
    print("(3) Die Primzahlfunktion")
    print("(4) Die Primzahlzwillinge")
    print("(0) Ende\n")
    auswahl = input("Deine Wahl: ")

    if auswahl == "1":

        print("\nAusgabe von Primzahlen in einem definierten Intervall")
        print("-----------------------------------------------------\n")

        while True:
            try:
                anfang = int(input("Bitte den Startwert eingeben: "))
                ende = int(input("Bitte den Endwert eingeben:   "))
                if anfang < 2 or ende < anfang:
                    print("\nStartwert mindestens 2, Endwert größer als Startwert...\n")
                    continue
                break
            except ValueError:
                print("\nBitte die Zahlen im richtigen Format als ganze Zahlen eingeben...\n")

        print()
        zaehler = 0
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")

        for number in range(anfang, ende + 1):
            for div in range(2, number):
                if number % div == 0:
                    break
            else:
                zaehler = zaehler + 1
                print("Primzahl", zaehler, "=", number)

        ausgabeauswertung(startzeit, startdatum, zaehler, ende, anfang, True)

    elif auswahl == "2":

        print("\nDas Sieb des Eratosthenes")
        print("-------------------------\n")

        ende = eingabeendwert()
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")
        print(eratosthenes(ende))
        zaehler = (len(eratosthenes(ende)))
        ausgabeauswertung(startzeit, startdatum, zaehler, ende, 2, True)

    elif auswahl == "3":

        print("\nDie Primzahlfunktion")
        print("--------------------\n")

        zaehler = 0
        ende = eingabeendwert()
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")

        print()

        primlist = []
        for zaehler in range(2, ende + 1):
            primlist.append(primepi(zaehler))

        print(primlist)

        endzeit = time.time()
        dauer = endzeit - startzeit

        ausgabeauswertung(startzeit, startdatum, zaehler, ende, 2, False)

        plt.title("Primzahlfunktion von 2 bis " + str(ende))
        plt.scatter(list(range(2, ende + 1)), primlist)
        plt.grid(True)
        plt.axis()
        plt.ylabel("Wert der Primzahlfunktion")
        plt.xlabel("Untersuchtes Intervall")
        plt.show()

    elif auswahl == "4":

        print("\nDie Primzahlzwillinge")
        print("---------------------\n")

        ende = eingabeendwert()
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")
        zwillinge = (primzahlzwillinge(ende))
        print(zwillinge)
        zaehler = int(len(primzahlzwillinge(ende)) / 2)

        ausgabeauswertung(startzeit, startdatum, zaehler, ende, 2, True)

        plt.title("Primzahlzwillinge bis " + str(ende))
        plt.plot(primzahlzwillinge(ende), "o")
        plt.grid(True)
        plt.xticks([])
        plt.xlabel("Anzahl : " + str(zaehler))
        plt.show()

    elif auswahl == "0":

        print("\nDas Programm wird beendet...")
        break

    else:

        print("\nFalsche Eingabe. Bitte wiederholen...")
