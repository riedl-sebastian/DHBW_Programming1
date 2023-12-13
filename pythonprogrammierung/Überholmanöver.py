# Python second Week Discussion

# Überholaufgabe aus der Physik (Bewegung mit konstanter Beschleunigung/Bewegung mit konstanter Geschwindigkeit)


# Einzelne Funktionen definieren
def beikonst(): #Wenn beide mit konstanter Geschwindigkeit fahren, wird diese Funktion verwendet
    eingabe1 = input("Mit welcher Geschwindigkeit bewegt sich Körper a?")
    v1 = int(eingabe1)
    print()
    eingabe2 = input("Welcher Abstand liegt zum Zeitpunkt t=0 zwischen Körper a und Körper b vor?")
    x0 = int(eingabe2)
    print()
    eingabe3 = input("Mit welcher Geschwindigkeit bewegt sich Körper b?")
    v2 = int(eingabe3)
    print()
    # Berechnung Ort
    for t in range(0,1000000):
        x1 = v1 * t + x0
        x2 = v2 * t
        print(x1)
        print(x2)
        if x1 == x2:
            print("t = ", t,)
            print("Zum Zeitpunkt ",t,"Sekunden haben Körper a und b die selbe Strecke zurückgelegt!")
            # Berechnung Momentangeschwindigkeit
            print("Die Geschwindigkeit von Körper a liegt bei ", v1, " Metern pro Sekunde, da diese konstant ist.")
            print("Die Geschwindigkeit von Körper b liegt bei ", v2, " Metern pro Sekunde, da diese konstant ist.")

def bkonstcnicht(): #Wenn b sich mit konstanter Geschwindigkeit bewegt, aber c nicht, wird diese Funktion aufgerufen
    eingabe1 = input("Mit welcher Geschwindigkeit bewegt sich Körper a?")
    v1 = int(eingabe1)
    print()
    eingabe2 = input("Welcher Abstand liegt zum Zeitpunkt t=0 zwischen Körper a und Körper b vor?")
    x0 = int(eingabe2)
    print()
    eingabe3 = input("Mit welcher Beschleunigung beschleunigt Körper b?")
    a = int(eingabe3)
    print()
    eingabe4 = input("Was ist die Anfangsgeschwindigkeit von Körper b?")
    v2 = int(eingabe4)
    print()
    # Berechnung Ort
    for t in range(0,1000000):
        x1 = v1 * t + x0
        x2 = 0.5 * a * t * t + v2 * t
        if x1 == x2:
            print("t = ",t)
            print("Zum Zeitpunkt ",t,"Sekunden haben Körper a und b die selbe Strecke zurückgelegt!")
            # Berechnung Momentangeschwindigkeit
            vm = v2 + t * a
            print("Die Geschwindigkeit von Körper a liegt bei ", v1, " Metern pro Sekunde, da diese konstant ist.")
            print("Die Momentangeschwindigkeit von Körper b liegt zum Zeitpunkt", t, "s bei ", vm, "Metern pro Sekunde.")


def bnichtcnicht(): #Wenn sich beide nicht mit konstanter Geschwindigkeit bewegen, wird diese Funktion aufgerufen
    eingabe1 = input("Mit welcher Beschleunigung beschleunigt Körper a?")
    a1 = int(eingabe1)
    print()
    eingabe2 = input("Was ist die Anfangsgeschwindigkeit von Körper a?")
    v1 = int(eingabe2)
    print()
    eingabe3 = input("Welcher Abstand liegt zum Zeitpunkt t=0 zwischen Körper a und Körper b vor?")
    x0 = int(eingabe3)
    print()
    eingabe4 = input("Mit welcher Beschleunigung beschleunigt Körper b?")
    a2 = int(eingabe4)
    print()
    eingabe5 = input("Was ist die Anfangsgeschwindigkeit von Körper b?")
    v2 = int(eingabe5)
    print()
    # Berechnung Ort
    for t in range(0,1000000):
        x1 = 0.5 * a1 * t * t + v2 * t + x0
        x2 = 0.5 * a2 * t * t + v2 * t
        if x1 == x2:
            print("t = ",t)
            print("Zum Zeitpunkt ",t,"Sekunden haben Körper a und b die selbe Strecke zurückgelegt!")
            # Berechnung Momentangeschwindigkeit
            vm1 = v1 + a1 * t
            vm2 = v2 + a2 * t
            print("Die Momentangeschwindigkeit von Körper a liegt zum Zeitpunkt", t, "s bei ", vm1, "Metern pro Sekunde.")
            print("Die Momentangeschwindigkeit von Körper b liegt zum Zeitpunkt", t, "s bei ", vm2, "Metern pro Sekunde.")

def bnichtckonst(): #Wenn b sich nicht mit konstanter Gewschwindigkeit bewegt aber c schon, wird diese Funktion aufgerufen
    eingabe1 = input("Mit welcher Beschleunigung beschleunigt Körper a?")
    a1 = int(eingabe1)
    print()
    eingabe2 = input("Was ist die Anfangsgeschwindigkeit von Körper a?")
    v1 = int(eingabe2)
    print()
    eingabe3 = input("Welcher Abstand liegt zum Zeitpunkt t=0 zwischen Körper a und Körper b vor?")
    x0 = int(eingabe3)
    print()
    eingabe4 = input("Mit welcher Geschwindigkeit bewegt sich Körper b?")
    v2 = int(eingabe4)
    print()
    # Berechnungt Ort
    for t in range(0,1000000):
        x1 = 0.5 * a1 * t * t + v1 * t + x0
        x2 = v2 * t
        if x1 == x2:
            print("t = ",t)
            print("Zum Zeitpunkt ",t,"Sekunden haben Körper a und b die selbe Strecke zurückgelegt!")
            # Berechnung Momentangeschwindigkeit
            vm = v1 + t * a1
            print("Die Momentangeschwindigkeit von Körper a liegt zum Zeitpunkt", t, "s bei ", vm, "Metern pro Sekunde.")
            print("Da die Geschwindigkeit von Körper b konstant ist, liegt diese immer noch bei ", v2, ".")

# Auswahl der passenden Funktion
b = input("Wie bewegt sich das erste Fahrzeug? ")
print()
c = input("Wie bewegt sich das zweite Fahrzeug?")
print()
print("--------------------------------------------------------------------------------------------------")
print()

if b == 'Mit konstanter Geschwindigkeit' and c == 'Mit konstanter Geschwindigkeit':
    beikonst()
elif b == 'Mit konstanter Geschwindigkeit' and c == 'Mit konstanter Beschleunigung':
    bkonstcnicht()
elif b == 'Mit konstanter Beschleunigung' and c == 'Mit konstanter Beschleunigung':
    bnichtcnicht()
elif b == 'Mit konstanter Beschleunigung' and c == 'Mit konstanter Geschwindigkeit':
    binichtckonst()
else:
    print("Falsche Eingabe")
