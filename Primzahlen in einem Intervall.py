########################
#                      #
#      Primzahlen      #
#   T.Hoppe Nov 2021   #
#        Github        #
#                      #
########################

import math
import time
import matplotlib.pyplot as plt
from sympy import primepi


def eratosthenes(end):
    is_prime = [False] * 2 + [True] * (end - 1)
    for n in range(int(end**0.5 + 1.5)):  # stop at ``sqrt(end)``
        if is_prime[n]:
            for i in range(n*n, end+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def atkins(end):
    results = [2, 3, 5]
    sieve = [False] * (end + 1)
    factor = int(math.sqrt(end)) + 1
    for i in range(1, factor):
        for j in range(1, factor):
            n = 4 * i ** 2 + j ** 2
            if (n <= end) and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * i ** 2 + j ** 2
            if (n <= end) and (n % 12 == 7):
                sieve[n] = not sieve[n]
            if i > j:
                n = 3 * i ** 2 - j ** 2
                if (n <= end) and (n % 12 == 11):
                    sieve[n] = not sieve[n]
    for index in range(5, factor):
        if sieve[index]:
            for jndex in range(index ** 2, end, index ** 2):
                sieve[jndex] = False
    for index in range(7, end):
        if sieve[index]:
            results.append(index)
    return results


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
    print("(3) Das Sieb von Atkins")
    print("(4) Die Primzahlfunktion")
    print("(5) Die Primzahlzwillinge")
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
        ausgabe = eratosthenes(ende)
        zaehler = (len(ausgabe))
        print("\n", ausgabe)
        ausgabeauswertung(startzeit, startdatum, zaehler, ende, 2, True)

    elif auswahl == "3":

        print("\nDas Sieb von Atkins")
        print("-------------------------\n")

        ende = eingabeendwert()
        startzeit = time.time()
        startdatum = time.strftime("%d.%m.%Y um %H:%M:%S")
        ausgabe = atkins(ende)
        zaehler = (len(ausgabe))
        print("\n", ausgabe)
        ausgabeauswertung(startzeit, startdatum, zaehler, ende, 2, True)

    elif auswahl == "4":

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

    elif auswahl == "5":

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
