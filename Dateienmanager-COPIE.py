# Python-Projekt:: Dateien-Manager// Bestimmte Dateien aus einem Verzeichnis können
#über bestimmte Key-Words gefunden werden:
#----------------------------------------------------------------------------------------------------------------------------------------

import time
# Mit import time können mit Timern gearbeitet werden
# Ziel: Verschiedene Dateien können geöffnet werden, aber nur für einen bestimmten Zeitraum
# angesehen werden, aber auch über die speziellen Keywords gefunden werden!!

print()
print("                                 Dateiensuche                ")
print()
print("Dateien in dem speziellen Ordner können über Key-Words gefunden werden.")

#Eingabe
eingabe1 = input("Dateiname: ")
eingabe2 = input("Nach Buchstaben suchen: ")

#Suche
if (eingabe1 == 'Namensliste'):
    namensliste = open('namensliste.txt','r')
    inhalt = namensliste.read()
    print(inhalt)
    namensliste.close()
    if (eingabe2 == 'a' or eingabe2 =='A'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('A'):
                    print(zeile)
                    namensliste.close()
    elif (eingabe2 == 'b' or eingabe2 == 'B'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('B'):
                    print(zeile)
                    namensliste.close()
    elif (eingabe2 == 'c' or eingabe2 == 'C'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('C'):
                    print(zeile)
                    namensliste.close()
    elif (eingabe2 == 'd' or eingabe2 == 'D'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('D'):
                    print(zeile)
                    namensliste.close()
    elif (eingabe2 == 'e' or eingabe2 =='E'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('E'):
                    print(zeile)
                    namensliste.close()
    elif (eingabe2 == 'f' or eingabe2 == 'F'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('F'):
                    print(zeile)
                    namensliste.close()
    elif (eingabe2 == 'g' or eingabe2 == 'G'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('G'):
                    print(zeile)
                    namensliste.close()
    elif (eingabe2 == 'H' or eingabe2 == 'h'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('H'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'i' or eingabe2 == 'I'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('i'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'j' or eingabe2 == 'J'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('J'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'k' or eingabe2 == 'K'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('K'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'l' or eingabe2 == 'L'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('L'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'm' or eingabe2 == 'M'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('M'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'n' or eingabe2 == 'N'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('N'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'O' or eingabe2 == 'o'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('O'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'p' or eingabe2 == 'P'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('P'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'q' or eingabe2 == 'Q'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('Q'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'R' or eingabe2 == 'r'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('R'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'S' or eingabe2 == 's'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('S'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 't' or eingabe2 == 'T'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('T'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'U' or eingabe2 == 'u'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('U'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'v' or eingabe2 == 'V'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('V'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'w' or eingabe2 == 'W'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('W'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'x' or eingabe2 == 'X'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('X'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'y' or eingabe2 == 'Y'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('Y'):
                    print(wort)
                    namensliste.close()
    elif (eingabe2 == 'z' or eingabe2 == 'Z'):
        namensliste = open('namensliste.txt','r')
        for zeile in namensliste:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('Z'):
                    print(wort)
                    namensliste.close()
    else:
        print('Keine mögliche Eingabe, nach der gesucht werden kann!')
elif (eingabe1 == 'Startfahrzeug'):
    startfahrzeug = open('startfahrzeug.txt','r')
    inhalt = startfahrzeug.read()
    print(inhalt)
    startfahrzeug.close
    if (eingabe2 == 'a' or eingabe2 == 'A'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('A'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'b' or eingabe2 == 'B'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('B'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'c' or eingabe2 == 'C'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('C'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'D' or eingabe2 == 'd'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('D'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'e' or eingabe2 == 'E'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('E'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'f' or eingabe2 == 'F'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('F'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'G' or eingabe2 == 'g'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('G'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'h' or eingabe2 == 'H'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('H'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'I' or eingabe2 == 'i'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('I'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'J' or eingabe2 == 'j'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('J'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'k' or eingabe2 == 'K'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('K'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'l' or eingabe2 == 'L'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('L'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'm' or eingabe2 == 'M'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('M'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'n' or eingabe2 == 'N'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('N'):
                    print(wort)
                    startfahrzeug.
    elif (eingabe2 == 'O' or eingabe2 == 'o'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('O'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'p' or eingabe2 == 'P'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('P'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'q' or eingabe2 == 'Q'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('Q'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'r' or eingabe2 == 'R'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('R'):
                    print(wort)
                    startfahrzeug.close()
    elif (eingabe2 == 'S' or eingabe2 == 's'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('S'):
                    print(wort)
                    startfahrzeug.close()
     elif (eingabe2 == 't' or eingabe2 == 'T'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('T'):
                    print(wort)
                    startfahrzeug.close()
     elif (eingabe2 == 'U' or eingabe2 == 'u'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('U'):
                    print(wort)
                    startfahrzeug.close()
     elif (eingabe2 == 'b' or eingabe2 == 'B'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('B'):
                    print(wort)
                    startfahrzeug.close()
     elif (eingabe2 == 'v' or eingabe2 == 'V'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('V'):
                    print(wort)
                    startfahrzeug.close()
     elif (eingabe2 == 'W' or eingabe2 == 'w'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('W'):
                    print(wort)
                    startfahrzeug.close()
     elif (eingabe2 == 'x' or eingabe2 == 'X'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('X'):
                    print(wort)
                    startfahrzeug.close()
     elif (eingabe2 == 'y' or eingabe2 == 'Y'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('Y'):
                    print(wort)
                    startfahrzeug.close()
     elif (eingabe2 == 'z' or eingabe2 == 'Z'):
        startfahrzeug = open('startfahrzeug.txt','r')
        for zeile in startfahrzeug:
            woerter in zeile.split()
            for wort in woertern:
                if wort.startswith('Z'):
                    print(wort)
                    startfahrzeug.close()
    else:
        print('Keine mögliche Eingabe, nach der gesucht werden kann!')
elif (eingabe1 == 'Leistungsvergleich'):
    leistungsvergleich = open('leistungsvergleich.txt','r')
    inhalt = leistungsvergleich.read()
    print(inhalt)
    leistungsvergleich.close
    if (eingabe2 == '8' or eingabe2 == 'A'):
        leistungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergleich:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('A'):
                    print(wort)
                    leitsungsvergleich.close()
    elif (eingabe2 == 'b' or eingabe2 == 'B'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('B'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'c' or eingabe2 == 'c'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('C'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'd' or eingabe2 == 'D'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('D'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'e' or eingabe2 == 'E'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('E'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'f' or eingabe2 == 'F'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('F'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'g' or eingabe2 == 'G'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('G'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'h' or eingabe2 == 'h'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('H'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'i' or eingabe2 == 'I'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('I'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'j' or eingabe2 == 'J'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('J'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'k' or eingabe2 == 'K'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('K'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'l' or eingabe2 == 'L'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('L'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'm' or eingabe2 == 'M'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('M'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'N' or eingabe2 == 'n'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('N'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'O' or eingabe2 == 'o'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('O'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'p' or eingabe2 == 'P'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('P'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'q' or eingabe2 == 'Q'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('Q'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'R' or eingabe2 == 'r'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('R'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 's' or eingabe2 == 'S'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('S'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'T' or eingabe2 == 't'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('T'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'u' or eingabe2 == 'U'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('U'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'v' or eingabe2 == 'V'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('V'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'W' or eingabe2 == 'w'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('W'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'z' or eingabe2 == 'Z'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('Z'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'x' or eingabe2 == 'X'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('X'):
                    print(wort)
                    leistungsvergleich.close()
     elif (eingabe2 == 'y' or eingabe2 == 'Y'):
        leitsungsvergleich = open('leistungsvergleich.txt','r')
        for zeile in leistungsvergliche:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('Y'):
                    print(wort)
                    leistungsvergleich.close()
    else:
        print('Keine mögliche Eingabe, nach der gesucht werden kann!')
else:
    startposition = open.('startposition.txt','r')
    inhalt = startposition.read()
    print(inhalt)
    startposition.close
    if (eingabe2 == 'a' or eingabe2 == 'A'):
         startposition = open('startposition.txt','r')
        for zeile in startfahrzeug:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('A'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'b' or eingabe2 == 'B'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('B'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'C' or eingabe2 == 'c'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('C'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'd' or eingabe2 == 'D'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('D'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'e' or eingabe2 == 'E'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('E'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'f' or eingabe2 == 'F'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('F'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'g' or eingabe2 == 'G'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('G'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'h' or eingabe2 == 'H'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('H'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'i' or eingabe2 == 'I'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('I'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'j' or eingabe2 == 'J'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('J'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'k' or eingabe2 == 'K'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('K'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'l' or eingabe2 == 'L'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('L'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'm' or eingabe2 == 'M'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('M'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'N' or eingabe2 == 'n'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('N'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'o' or eingabe2 == 'O'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('O'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'p' or eingabe2 == 'P'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('P'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'q' or eingabe2 == 'Q'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('Q'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'R' or eingabe2 == 'r'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('R'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'S' or eingabe2 == 's'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('S'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 't' or eingabe2 == 'T'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('T'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'u' or eingabe2 == 'U'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('U'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'v' or eingabe2 == 'V'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('V'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'w' or eingabe2 == 'W'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('W'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'x' or eingabe2 == 'X'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('X'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'y' or eingabe2 == 'Y'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('Y'):
                    print(wort)
                    startposition.close()
    elif (eingabe2 == 'z' or eingabe2 == 'Z'):
        startposition = open('startposition.txt','r')
        for zeile in startposition:
            woerter = zeile.split()
            for wort in woerter:
                if wort.startswith('Z'):
                    print(wort)
                    startposition.close()
    else:
        print('Keine mögliche Eingabe, nach der gesucht werden kann!')


# Ende---------------------------------------------------------------------------------



    

