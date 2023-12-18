# mit Pythonfunktionen etwas Zeichnen


import turtle
# von Edge-Copilot
rows = int(input("Geben Sie die Anzahl der Reihen ein: "))
for i in range(rows):
    for j in range(rows-i-1):
        print(end=" ")
    for j in range(2*i+1):
        print("*", end="")
    print()

# Eigenes

zeilen = int(input("Wie viele Zeilen?"))
for i in range(zeilen):
    print(" ", end="")
    for i in range(zeilen-1):
        print("[]", end="")
    for i in range(zeilen-1):
        print("O", end="")
    print()
print()

# Turtle-Arbeiten
sternflocke = turtle.Turtle()

# Setzen Sie die Geschwindigkeit der Turtle
sternflocke.speed(10)

# Setzen Sie die Farbe der Turtle
sternflocke.color("cyan")

# Zeichnen Sie eine Sternflocke
for i in range(50):
    sternflocke.forward(100)
    sternflocke.right(144)

# Beenden Sie das Zeichnen
turtle.done()

#neuer Turtle

wasweisich = turtle.Turtle()
for i in range(100):
    wasweisich.forward(500)
    wasweisich.right(90)
    wasweisich.forward(500)
    wasweisich.right(90)
    wasweisich.forward(500)
    wasweisich.right(90)
    wasweisich.forward(500)
    wasweisich.right(90)
wasweisich.left(10)
        
    
