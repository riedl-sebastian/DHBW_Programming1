# Python Kurs 1 Woche 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1 Projekt // Autorennen //

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Bei dem Autorennen werden die verschiedenen Stats von den Autos verglichen und ausgerechnet, welches am wahrscheinlichsten gewinnt. Der User kann auf verschiedene Autos tippen und sehen, ob sein Wagen gewinnt.

# Variablen einstellen (Stats von den Autos)
# Werte in den list´s: 1. Wert=PS, 2.Wert=Hubraum, 3.Wert=Gänge, 4.Wert=Gewicht,
GT2RSClubsport = [700, 3800, 7, 1390] 
BMWM4CSL = [1000, 2993, 8, 1618, ]
AUDIR8GT = [620, 5200, 8, 1570]
P1GTR = [1000, 3800, 7, 1395]
Bugatti = [1600, 8000, 8, 1825]

#Variablen für Bestimmung des Siegers
# global sorgt dafür, dass die Variablen auch in allen anderen Funktionen so deklariert sind
global BugattiW
global BMWM4CSLW
global AUDIR8GTW
global GT2RS
global P1GTRW

# Variablen für Einsatz des Spielers

n #Geldeinsatz
g #Gesamteinsatz

# Wenn der User mehr Infos haben willy

def infos():

	info = input('Welches Auto intressiert Sie besonders: ')

	if info == 'Porsche':
		print("Hallo")
	elif info == 'BMW M4 CSL':
		print("Hallo2")
	elif info == 'Audi R8 GT':
		print("Hallo 3")
	elif info == 'McLaren P1 GTR':
		print("Hallo 4")
	else:
		print("Hallo 5")

#Auswahl Art des Rennens

def verschrennen():

	g = input('Geben Sie Ihren Spielvermögen für den Abend ein: ')
	tipp = input('Geben Sie das Auto ein, auf das Sie setzten: ')

	while g<1000:
		print("Der Mindestspielbetrag liegt bei 1000 Euro!")
		if g<10000000 and g>10000:
			print("Wir danken Ihnen für den Spaß an unserem Spiel und Ihren leichtsinnigen Umgang mit Geld!")
			t = g/100*90 
			s = 5000
			print("Wenn Sie mehr als " + t + " Euro ihres Spielvermögens auf ein Spiel setzen, bekommen Sie " + 5000 + " Euro auf Ihr Spielvermögen!")
			n = input('Geben Sie Ihren Einsatz für das Renne ein: ')
			if(n>t):
				g = g + s
				print(g)
			else: 
				print("Viel Spaß beim Wetten!")
	rennen = input("Welche Art von Rennen solle die Autos fahren? (Moeglichkeiten: Dragrace(1), Sprintrennen(2), Rundkurs(3), Technical(4)): ")
	rennen_1= int(rennen)
	if rennen_1 == 'Dragrace':
		BugattiW = 2*Bugatti[0]-Bugatti[3]
		BMWM4CSLW = 2*BMWM4CSL[0]-BMWM4CSL[3]
		AUDIR8GTW = 2*AUDIR8GT[0]-AUDIR8GT[3]
		GT2RS = 2*GT2RSClubsport[0]-GT2RSClubsport[3]
		P1GTRW = 2*P1GTR[0]-P1GTR[3]
		if BugattiW > BMWM4CSLW and BugattiW > AUDIR8GTW and BugattiW > GT2RS and BugattiW > P1GTRW:
			print("Der Bugatti Chiron Supersport+ hat das Rennen gewonnen!")
		elif BMWM4CSLW > BugattiW and BMWM4CSLW > AUDIR8GTW and BMWM4CSLW > GT2RS and BMWM4CSLW > P1GTRW:
			print("Der BMW M4 CSL hat das Rennen gewonnen!")
		elif AUDIR8GTW > BugattiW and AUDIR8GTW > BMWM4CSLW and AUDIR8GTW > GT2RS and AUDIR8GTW > P1GTRW:
			print("Der Audi R8 GT hat das Rennen gewonnen!")
		elif GT2RS > BugattiW and GT2RS > BMWM4CSLW and GT2RS > AUDIR8GTW and GT2RS > P1GTRW:
			print("Der Porsche GT2 RS Clubsport hat das Rennen gewonnen!")
		else:
			print("Der McLaren P1 GTR hat das Rennen gewonnen!")
	elif rennen_1 == 'Sprintrennen':
		BugattiW = Bugatti[0] + Bugatti[1] + Bugatti[2] - 2*Bugatti[3]
		BMWM4CSLW = BMWM4CSL[0] + BMWM4CSL[1] + BMWM4CSL[2] - 2*BMWM4CSL[3]
		AUDIR8GTW = AUDIR8GT[0] + AUDIR8GT[1] + AUDIR8GT[2]- 2*AUDIR8GT[3]
		GT2RS = GT2RSClubsport[0] + GT2RSClubsport[1] + GT2RSClubsport[2] - 2*GT2RSClubsport[3]
		P1GTRW = P1GTR[0] + P1GTR[1] + P1GTR[2] - 2*P1GTR[3]
		if BugattiW > BMWM4CSLW and BugattiW > AUDIR8GTW and BugattiW > GT2RS and BugattiW > P1GTRW:
			print("Der Bugatti Chiron Supersport+ hat das Rennen gewonnen!")
		elif BMWM4CSLW > BugattiW and BMWM4CSLW > AUDIR8GTW and BMWM4CSLW > GT2RS and BMWM4CSLW > P1GTRW:
			print("Der BMW M4 CSL hat das Rennen gewonnen!")
		elif AUDIR8GTW > BugattiW and AUDIR8GTW > BMWM4CSLW and AUDIR8GTW > GT2RS and AUDIR8GTW > P1GTRW:
			print("Der Audi R8 GT hat das Rennen gewonnen!")
		elif GT2RS > BugattiW and GT2RS > BMWM4CSLW and GT2RS > AUDIR8GTW and GT2RS > P1GTRW:
			print("Der Porsche GT2 RS Clubsport hat das Rennen gewonnen!")
		else:
			print("Der McLaren P1 GTR hat das Rennen gewonnen!")
	elif rennen_1 == 'Rundkurs':
		BugattiW = Bugatti[2]-Bugatti[3] 
		BMWM4CSLW = BMWM4CSL[2]-BMWM4CSL[3]
		AUDIR8GTW = AUDIR8GT[2]-AUDIR8GT[3]
		GT2RS = GT2RSClubsport[2]-GT2RSClubsport[3]
		P1GTRW = P1GTR[2]-P1GTR[3]
		if BugattiW > BMWM4CSLW and BugattiW > AUDIR8GTW and BugattiW > GT2RS and BugattiW > P1GTRW:
			print("Der Bugatti Chiron Supersport+ hat das Rennen gewonnen!")
		elif BMWM4CSLW > BugattiW and BMWM4CSLW > AUDIR8GTW and BMWM4CSLW > GT2RS and BMWM4CSLW > P1GTRW:
			print("Der BMW M4 CSL hat das Rennen gewonnen!")
		elif AUDIR8GTW > BugattiW and AUDIR8GTW > BMWM4CSLW and AUDIR8GTW > GT2RS and AUDIR8GTW > P1GTRW:
			print("Der Audi R8 GT hat das Rennen gewonnen!")
		elif GT2RS > BugattiW and GT2RS > BMWM4CSLW and GT2RS > AUDIR8GTW and GT2RS > P1GTRW:
			print("Der Porsche GT2 RS Clubsport hat das Rennen gewonnen!")
		else:
			print("Der McLaren P1 GTR hat das Rennen gewonnen!")
	else:
		BugattiW = Bugatti[0] / Bugatti[2] - 0.5*Bugatti[3]
		BMWM4CSLW = BMWM4CSL[0] / BMWM4CSL[2] - 0.5*BMWM4CSL[3]
		AUDIR8GTW = AUDIR8GT[0] / AUDIR8GT[2] - 0.5*AUDIR8GT[3]
		GT2RS = GT2RSClubsport[0] / GT2RSClubsport[2] - 0.5*GT2RSClubsport[3] 
		P1GTRW = P1GTR[0] / P1GTR[2] - 0.5*P1GTR[3]
		if BugattiW > BMWM4CSLW and BugattiW > AUDIR8GTW and BugattiW > GT2RS and BugattiW > P1GTRW:
			print("Der Bugatti Chiron Supersport+ hat das Rennen gewonnen!")
		elif BMWM4CSLW > BugattiW and BMWM4CSLW > AUDIR8GTW and BMWM4CSLW > GT2RS and BMWM4CSLW > P1GTRW:
			print("Der BMW M4 CSL hat das Rennen gewonnen!")
		elif AUDIR8GTW > BugattiW and AUDIR8GTW > BMWM4CSLW and AUDIR8GTW > GT2RS and AUDIR8GTW > P1GTRW:
			print("Der Audi R8 GT hat das Rennen gewonnen!")
		elif GT2RS > BugattiW and GT2RS > BMWM4CSLW and GT2RS > AUDIR8GTW and GT2RS > P1GTRW:
			print("Der Porsche GT2 RS Clubsport hat das Rennen gewonnen!")
		else:
			print("Der McLaren P1 GTR hat das Rennen gewonnen!")

	if tipp == 'Bugatti' and BugattiW > BMWM4CSLW and BugattiW > AUDIR8GTW and BugattiW > GT2RS and BugattiW > P1GTRW:
		print("HERZLICHEN GLÜCKWUNSCH!! Der Bugatti Chiron Supersport hat gewonnen!")
		g = g + n
		print(g)
	elif tipp == 'BMWM4CSL' and BMWM4CSLW > BugattiW and BMWM4CSLW > AUDIR8GTW and BMWM4CSLW > GT2RS and BMWM4CSLW > P1GTRW:
		print("HERZLICHEN GLÜCKWUNSCH!! Der BMW M4 CSL hat gewonnen!")
		g = g + n
		print(g)
	elif tipp == 'AUDIR8GT' and AUDIR8GTW > BugattiW and AUDIR8GTW > BMWM4CSLW and AUDIR8GTW > GT2RS and AUDIR8GTW > P1GTRW:
		print("HERZLICHEN GLÜCKWUNSCH!! Der Audi R8 GT hat gewonnen!")
		g = g + n
		print(g)
	elif tipp == 'GT2RS Clubsport' and GT2RS > BugattiW and GT2RS > BMWM4CSLW and GT2RS > AUDIR8GTW and GT2RS > P1GTRW:
		print("HERZLICHEN GLÜCKWUNSCH!! Der Porsche GT2 RS Clubsport hat gewonnen!")
		g = g + n
		print(g)
	elif tipp == 'P1 GTR' and P1GTRW > BugattiW and P1GTRW > BMWM4CSLW and P1GTRW > AUDIR8GTW and P1GTRW > GT2RS:
		print("HERZLICHEN GLÜCKWUNSCH!! Der McLaren P1 GTR hat gewonnen!")
		g = g + n
		print(g)
	else:
		print("Sie haben die Wette verloren!!")
		g = g - n
		print(g)
	u = input("Sie haben die Chance noch einen besonderen Preis zugewinnen, wenn Sie eine Zahl zwischen 0 und 1000 eingeben: ")
	while u>1000:
		print("Diese Zahl ist nicht in der möglichen Menge enthalten. Geben Sie eine Zahl zwischen 0 und 1000!")
		u = input("Sie haben die Chance noch einen besonderen Preis zugewinnen, wenn Sie eine Zahl zwischen 0 und 1000 eingeben: ")
	for m in range(1,10):
		d = ((m + 10)^10)%7
		print(d)
		if d == u:
			print("HERZLICHEN GLÜCKWUNSCH!! Sie haben den besonderen Preis gewonnen! Melden Sie sich bei einer zuständigen Person!")
		else:
			print("Sie haben leider nicht gewonnen. Beim nächten Mal gewinnen Sie bestimmt!")
		
		
		
# Ausgabe der einzelnen Funktionen
infos()
verschrennen()
