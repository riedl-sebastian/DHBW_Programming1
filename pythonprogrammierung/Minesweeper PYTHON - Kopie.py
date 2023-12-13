# Minesweeper in Python

import random
import os


# Minen platzieren

def minen_legen():

    global numbers
    global minen_anzahl
    global n

    count = 0
    while count < minen_anzahl:

        wert = random.randint(0, n*n - 1)
        r = wert // n
        col = wert % n

        if numbers[r][col] != -1:
            count = count + 1
            numbers[r][col]= -1

# Andere Spielfeldwerte

def andere_werte():

    global numbers
    global n

    for r in range(n):
        for col in range(n):

            if numbers[r][col] == -1:
                continue
# oben
            if r > 0 and numbers[r-1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
# unten             
            if r < n-1 and numbers[r+1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
# links
            if col > 0 and numbers[r][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
# rechts
            if col < n-1 and numbers[r][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
# oben links
            if r > 0 and col > 0 and numbers[r-1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
# oben rechts
            if r > 0 and col < n-1 and numbers[r-1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
# unten links
            if r < n-1 and col > 0 and numbers[r+1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
# unten rechts
            if r < n-1 and col < n-1 and numbers[r+1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1

# Alle Felder mit dem Wert Null
#----------------------CODE übernommen und angepasst-----------------------------
def null_felder(r,col):

    global minen_werte
    global numbers
    global vis

    if [r,col] not in vis:
        vis.append([r,col])
        if numbers[r][col] == 0:
            minen_werte[r][col]=numbers[r][col]
            if r>0:
                null_felder(r-1,col)
            if r<n-1:
                null_felder(r+1,col)
            if col>0:
                null_felder(r,col-1)
            if col<n-1:
                null_felder(r,col+1)
            if r > 0 and col > 0:
                null_felder(r-1, col-1)
            if r > 0 and col < n-1:
                null_felder(r-1, col+1)
            if r < n-1 and col > 0:
                null_felder(r+1, col-1)
            if r < n-1 and col < n-1:
                null_felder(r+1, col+1)

    # Wenn Spielfeld nicht mit Wert 0   

        if numbers[r][col] !=0:
            minen_werte[r][col]=numbers[r][col]
#-----------------------------------------------------------------------------
# Spielfeld erstellen
#---------------------------CODE übernommen und angepasst-----------------------
def spielfeld():
    global minen_werte
    global n

    print()
    print("MINESWEEPER\n")
 
    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)   
 
    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______" 
            print(st)
 
        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")
         
        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(minen_werte[r][col]) + "  "
        print(st + "|") 
 
        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')
 
    print()
#-------------------------------------------------------------------------------
# Spieleranleitung
def spielanleitung():
    print("Anleitung: ")
    print("1. Geben Sie eine Zeilen-(vertikal) und Spaltennummer(horizontal) ein, um ein Feld auszuwählen.")
    print("2. Um eine Mine zu markieren, nach Eingabe der Zeilen- und Spaltennjmmer F drücken.")

# Kontrolle, ob alle Minen gefunden wurden
def kontrolle():

    global minen_werte
    global n
    global minen_anzahl

    count = 0

    for r in range(n):
        for col in range(n):
            if minen_werte[r][col] != ' ' and minen_werte[r][col] != 'F':
                count =count + 1

    if count == n*n-minen_anzahl:
        return True
    else:
        return False

def zeige_minen():

    global minen_werte
    global numbers
    global n

    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                minen_werte[r][col] = 'M'


#-------------------CODE übernommen und angepasst--------------------------------
if __name__ == "__main__":

    n = 8
    minen_anzahl = 8
    numbers = [[0 for y in range(n)]for d in range(n)]
    minen_werte = [[' '  for y in range(n)]for d in range(n)]
    flags = []

# Alle Funktionen ausführen
    

    minen_legen()

    andere_werte()

    spielanleitung()

    over = False

    while not over:
        spielfeld()

        eingabe = input("Geben Sie eine Spaltennummer gefolgt von einer Zeilennummer ein.")

        if len(eingabe) == 2:
#-------------------------------------------------------------------------------
            try:
                wert = list(map(int,eingabe))
            except ValueError:
                    os.system("clear")
                    print("Falsche Eingabe")
                    spielanleitung()
                    continue
        elif len(eingabe) == 3:
            if eingabe[2] != 'F' and eingabe[2] != 'f':
                os.system("clear")
                print("Falsche Eingabe")
                spielanleitung()
                continue
            try:
                wert=list(map(int,eingabe[:2]))
            except ValueError:
                os.system("clear")
                print("Falsche Eingabe")
                spielanleitung()
                continue
            if wert[0]>n or wert[0]<1 or wert[1]>n or wert[1]<1:
                os.system("clear")
                print("Falsche Eingabe")
                spielanleitung()
                continue
            r = wert[0]-1
            col = wert[1]-1

            if [r,col] in flags:
                os.system("clear")
                print("Markierung schon platziert")
                continue
            if minen_werte[r][col] != ' ':
                os.system("clear")
                print("Wert bereits bekannt")
                continue
            if len(flags) < minen_anzahl:
                os.system("clear")
                print("Markierung platziert")
                flags.append([r,col])

                minen_werte[r][col] = 'F'
                continue
            else:
                os.system("clear")
                print("Markierungen fertig")
                continue
        else:
            os.system("clear")
            print("Falsche Eingabe")
            spielanleitung()
            continue
        if wert[0] > n or wert[0] < 1 or wert[1] > n or wert[1] < 1:
            os.system("clear")
            print("Falsche Eingabe")
            spielanleitung()
            continue

        r = wert[0]-1
        col = wert[1]-1

        if [r, col] in flags:
            flags.remove([r, col])

        if numbers[r][col] == -1:
            minen_werte[r][col] = 'M'
            zeige_minen()
            spielfeld()
            print("Auf einer Mine gelandet. GAME OVER!!!!!")
            over = True
            continue

        elif numbers[r][col] == 0:
            vis = []
            minen_werte[r][col] = '0'
            null_felder(r, col)

        else:
            minen_werte[r][col] = numbers[r][col]

        if(kontrolle()):            
            zeige_minen()
            spielfeld()
            print("Du hast alle Minen markiert!")
            over = True
            continue
        os.system("clear")
        

# Die verschiedenen benötigten Funktionen des Moduls wurden nachgelesen.           

