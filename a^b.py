import numpy as np


ergebnisse = []

for a in range(2, 6):
    for b in range(2, 6):
        ergebnis = a ** b
        ergebnisse.append(ergebnis)

ergebnisse = np.array(ergebnisse)

print("Die Länge des Arrays ist:", len(ergebnisse))
print("ProjectEuler Problem")
