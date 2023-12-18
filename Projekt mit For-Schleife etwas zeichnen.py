# Mit einer For-Schleife etwas zeichnen

#-------------------------------------------------------------------------------------------------------------------------------------------------

spalten = int(input("Wie viele Zeilen sollen es seine? "))

for i in range(spalten):
    for t in range(spalten-1-i):
        print("_", end="")
    for s in range(spalten-(spalten-1)+i):
        print("[]", end="")
    for q in range(spalten-1-i):
        print("_", end="")
    print()
print()

#-------------------------------------------------------------------------------------------------------------------------------------------------
var = int(input("Wie groß soll das ganze werden?"))
for j in range(var):
    for k in range(var-1-j):
        print("X",end ="")
    for i in range(var-(var-1)+j):
        print(" ",end="")
    for m in range(var-(var-1)+j):
        print(" ",end="")
    for l in range(var-1-j):
        print("O",end="")
    print()
for n in range(var):
    for p in range(var-(var-1)+n):
        print("X",end="")
    for q in range(var-n-1):
        print(" ",end="")
    for s in range(var-n-1):
        print(" ",end="")
    for t in range(var-(var-1)+n):
        print("O",end="")
    print()     

#-------------------------------------------------------------------------------------------------------------------------------------------------

zeilen = int(input("Wie groß soll das ganze werden?"))
print()
print()
for z in range(zeilen):
    for y in range(zeilen-1-z):
        print(" ",end="")
    for x in range(zeilen-(zeilen-1)+z):
        print("&", end ="")
    for w in range(zeilen-1-z):
        print("*",end="")
    for v in range(zeilen-(zeilen-1)+z):
        print(" ",end="")
    for u in range(zeilen-(zeilen-1)+z):
        print(" ",end="")
    for t in range(zeilen-z-1):
        print("*",end="")
    for s in range(zeilen-(zeilen-1)+z):
        print("&",end="")
    print()
for a in range(zeilen):
    for b in range(zeilen-(zeilen-1)+a):
        print(" ",end="")
    for c in range(zeilen-1-a):
        print("&",end="")
    for d in range(zeilen-(zeilen-1)+a):
        print("*",end="")
    for d in range(zeilen-1-a):
        print(" ",end="")
    for e in range(zeilen-1-a):
        print(" ",end="")
    for f in range(zeilen-(zeilen-1)+a):
        print("*",end="")
    for g in range(zeilen-1-a):
        print("&",end="")
    print()

            
                    
            
