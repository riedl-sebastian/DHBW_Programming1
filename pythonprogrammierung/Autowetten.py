# Python Kurs 1 Woche 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1 Projekt // Autorennen //

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Bei dem Autorennen werden die verschiedenen Stats von den Autos verglichen und ausgerechnet, welches am wahrscheinlichsten gewinnt. Der User kann auf verschiedene Autos tippen und sehen, ob sein Wagen gewinnt.

# Der import.random()-Befehl importiert ein Hilfspaket, welches Zufallszahlen importieren kann

import.random()

# Variablen einstellen (Stats von den Autos)
# Werte in den list´s: 1. Wert=PS, 2.Wert=Hubraum, 3.Wert=Gänge, 4.Wert=Gewicht,
GT2RSClubsport = [700, 3800, 7, 1390] 
BMWM4CSL = [1000, 2993, 8, 1618, ]
AUDIR8GT = [620, 5200, 8, 1570]
P1GTR = [1000, 3800, 7, 1395]
Bugatti = [1600, 8000, 8, 1825]

#Variablen für Bestimmung des Siegers
BugattiW
BMWM4CSLW
AUDIR8GTW
GT2RS
P1GTRW

# Variablen für Einsatz des Spielers

n #Geldeinsatz
g #Gesamteinsatz

# Wenn der User mehr Infos haben willy

def infos():

	info = input('Welches Auto intressiert Sie besonders: ')

	if info == 'Porsche':
		print('Der Porsche GT2RS Clubsport verfügt über einen 700Ps starken 6 Zylinder Aluminium Biturbo-Boxermotor in Hecklage und starrer Aufhängung. Der Hubraum beträg 3.800 Kubik-Centimeter, der Kolbenhub liegt bei 77,5mm. Das 7-Gang PDK Getriebe in ebenfalls starrer Aufhängung sorgt für kurze Schaltzeiten und eine maximale Drehmomentsübertragung. Das Fahrzeug wiegt 1380kg und verfügt über eine Heckantrieb. Der Drehmoment liegt ebenfalls bei ca. 770Nm.)
	elif info == 'BMW M4 CSL':
		print('Der BMW M4 CSL verfügt über einen V6-Schmiedemotor mit 550Ps in Frontlage mit starrer Aufhängung. Der Hubraum beträgt 2993 Kubikcentimeter. Ein herausstechen des Detail des M4 CSL ist sein Turbolader mit einem Maximaldruck von 2,1 Bar. Das sportlichste Modell der 4er-Reihe verfügt über ein Automatisches-8-Gang-Getriebe welches einen schnellen Gangwechsel und eine großartige Drehmomentübertragung liefer. Typisch für BMW verfügt auch dieser über einen Heckantrieb. Der Drehmoment liegt etwas unter dem seines großen Bruder, des M5 CS. Hierbei gehen wir jedoch von der Britischen Version des M4 CSL´s aus, welche über 1000Ps verfügt. Zudem wurde das Chassi verstärkt, was für eine verbesserte Kurvelage sorgt.')
	elif info == 'Audi R8 GT':
		print('Der Audi R8 GT ist die sportlichere Version des R8 V10, dieser verfügt ebenfalls über einen 5,2 Liter V10 Aluminium-Motor in Hecklage mit einer direkten Fahrtwindkühlung. Der Audi ist bekannt für seine hervorragende Kurvenlage und seinen exzellenten Allrad-Antrieb, das Renndifferenzial lässt trotzdem noch zu wünschen übrig. Das Renndifferenzials sorgt durch die möglichst effektive Verlagerung des Drehmoments teilweise für kurze Leistungsverlust nach einem  Schalten des 8-Gang-Automatik-Getriebes. Unter Autofreunde ist ein bekannter Spruch über R8 besitzter, dass diese nicht das Geld für einen Hurracan hatten, aber trotzdem zu den Supercar-Besitzern gehören wollen. Jetzt aber wieder mehr zu den technischen Details: Der Motor des Audis hat nämlich noch einen Trumpf, der sogar den V10 6.2l des Adventador SVJ alt aussehen lässt - der Drehzahlbegrenzer schlägt erst bei 8600 Umdrehungen pro Minute zu, bei so einer Umdrehungszahl und Hubraum ist der Abgasstrom sehr voluminös, wodurch die Aufladung des Turbl		ders extrem schnell geschieht.')
	elif info == 'McLaren P1 GTR':
		print('Der P1 GTR ist die Motorsport Version des P1s und verfügt über einen 3,8-Liter-BI-Turbo-V8 Motor, welcher sich ebenfalls im Heck befindet. Der Motor bring eine Leistung
		von 1000Ps, während das Gewicht nur bei 1395 Kilogramm liegt. Der P1 GTR ist leider nicht auf öffenlichen Straßen zulassbar. Damit das Gewicht so gering ausfällt, bestehen
		grosse Teile der Verkleidung aus Carbon. Das Chassi besteht zu Großteil aus Aluminium. Ein weiteres interessantes Detail des P1 GTRs ist sein auffälliges Heck: in den normalerweise
		etwas mehr verkleideten Luftdurchlässen lassen sich zwei rote Luftfilter in Zylinderform erkennen. Durch diese liegt die Luftansaugung bei ca. 800 Liter pro Minute (etwas 
		niedriger als bei einem Bugatti Chiron, dessen liegt bei 1000 Liter pro Sekunde).')
	else:
		print('Der Bugatti Chiron Supersport 300+ ist noch nachgewiesen das schnellste Auto der Welt mit einer Geschwindigkeit von 490,484km/h, dieser Rekord wurde auf einer speziellen Test-
		strecke nahe Wolfsburg erzielt. Noch, da der Koenigsegg Jesko Absolute angeblich eine Höchstgeschwindigkeit von über 500km/h erreichen kann, dies wurde jedoch noch nicht offziell
		erfasst. Ein Serien-Bugatti Chiron Supersport 300+, von dem es nur 30 Stück gibt, schaft unter normalen Bedingungen eine Höchstgeschwindigkeit von 440km/h. Der Bugatti verfügt über
		Chiron Supersport 300+  ist ebenfalls sehr bemerkenswert: bei einem Druck von 50t verschiebt sich das Chassi nur um ca. 1°. Durch diese ausergewöhnliche Stärke werden solche 
		Geschwindigkeiten erst möglich')

#Auswahl Art des Rennens

def verschrennen():

	g = input('Geben Sie Ihren Spielvermögen für den Abend ein: ')
	tipp = input('Geben Sie das Auto ein, auf das Sie setzten: ')

	while g<1000:
		print("Der Mindestspielbetrag liegt bei 1000 Euro!")	
		if g<10000000 AND g>10000:
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
			
	rennen = input('Welche Art von Rennen solle die Autos fahren? (Moeglichkeiten: Dragrace, Sprintrennen, Rundkurs, Technical): ')

	if rennen = 'Dragrace':
		BugattiW = 2*Bugatti[0]-Bugatti[3]
		BMWM4CSLW = 2*BMWM4CSL[0]-BMWM4CSL[3]
		AUDIR8GTW = 2*AUDIR8GT[0]-AUDIR8GT[3]
		GT2RS = 2*GT2RSClubsport[0]-GT2RSClubsport[3]
		P1GTRW = 2*P1GTR[0]-P1GTR[3]
		if BugattiW > BMWM4CSLW AND BugattiW > AUDIR8GTW AND BugattiW > GT2RS AND BugattiW > P1GTRW:
			print("Der Bugatti Chiron Supersport+ hat das Rennen gewonnen!")
		elif BMWM4CSLW > BugattiW AND BMWM4CSLW > AUDIR8GTW AND BMWM4CSLW > GT2RS AND BMWM4CSLW > P1GTRW:
			print("Der BMW M4 CSL hat das Rennen gewonnen!")
		elif AUDIR8GTW > BugattiW AND AUDIR8GTW > BMWM4CSLW AND AUDIR8GTW > GT2RS AND AUDIR8GTW > P1GTRW:
			print("Der Audi R8 GT hat das Rennen gewonnen!")
		elif GT2RS > BugattiW AND GT2RS > BMWM4CSLW AND GT2RS > AUDIR8GTW AND GT2RS > P1GTRW:
			print("Der Porsche GT2 RS Clubsport hat das Rennen gewonnen!")
		else
			print("Der McLaren P1 GTR hat das Rennen gewonnen!")
	elif rennen = 'Sprintrennen':
		BugattiW = Bugatti[0] + Bugatti[1] + Bugatti[2] - 2*Bugatti[3]
		BMWM4CSLW = BMWM4CSL[0] + BMWM4CSL[1] + BMWM4CSL[2] - 2*BMWM4CSL[3]
		AUDIR8GTW = AUDIR8GT[0] + AUDIR8GT[1] + AUDIR8GT[2]- 2*AUDIR8GT[3]
		GT2RS = GT2RSClubsport[0] + GT2RSClubsport[1] + GT2RSClubsport[2] - 2*GT2RSClubsport[3]
		P1GTRW = P1GTR[0] + P1GTR[1] + P1GTR[2] - 2*P1GTR[3]
		if BugattiW > BMWM4CSLW AND BugattiW > AUDIR8GTW AND BugattiW > GT2RS AND BugattiW > P1GTRW:
			print("Der Bugatti Chiron Supersport+ hat das Rennen gewonnen!")
		elif BMWM4CSLW > BugattiW AND BMWM4CSLW > AUDIR8GTW AND BMWM4CSLW > GT2RS AND BMWM4CSLW > P1GTRW:
			print("Der BMW M4 CSL hat das Rennen gewonnen!")
		elif AUDIR8GTW > BugattiW AND AUDIR8GTW > BMWM4CSLW AND AUDIR8GTW > GT2RS AND AUDIR8GTW > P1GTRW:
			print("Der Audi R8 GT hat das Rennen gewonnen!")
		elif GT2RS > BugattiW AND GT2RS > BMWM4CSLW AND GT2RS > AUDIR8GTW AND GT2RS > P1GTRW:
			print("Der Porsche GT2 RS Clubsport hat das Rennen gewonnen!")
		else
			print("Der McLaren P1 GTR hat das Rennen gewonnen!")
	elif rennen = 'Rundkurs':
		BugattiW = Bugatti[2]-Bugatti[3] 
		BMWM4CSLW = BMWM4CSL[2]-BMWM4CSL[3]
		AUDIR8GTW = AUDIR8GT[2]-AUDIR8GT[3]
		GT2RS = GT2RSClubsport[2]-GT2RSClubsport[3]
		P1GTRW = P1GTR[2]-P1GTR[3]
		if BugattiW > BMWM4CSLW AND BugattiW > AUDIR8GTW AND BugattiW > GT2RS AND BugattiW > P1GTRW:
			print("Der Bugatti Chiron Supersport+ hat das Rennen gewonnen!")
		elif BMWM4CSLW > BugattiW AND BMWM4CSLW > AUDIR8GTW AND BMWM4CSLW > GT2RS AND BMWM4CSLW > P1GTRW:
			print("Der BMW M4 CSL hat das Rennen gewonnen!")
		elif AUDIR8GTW > BugattiW AND AUDIR8GTW > BMWM4CSLW AND AUDIR8GTW > GT2RS AND AUDIR8GTW > P1GTRW:
			print("Der Audi R8 GT hat das Rennen gewonnen!")
		elif GT2RS > BugattiW AND GT2RS > BMWM4CSLW AND GT2RS > AUDIR8GTW AND GT2RS > P1GTRW:
			print("Der Porsche GT2 RS Clubsport hat das Rennen gewonnen!")
		else
			print("Der McLaren P1 GTR hat das Rennen gewonnen!")
	else 	
		BugattiW = Bugatti[0] / Bugatti[2] - 0.5*Bugatti[3]
		BMWM4CSLW = BMWM4CSL[0] / BMWM4CSL[2] - 0.5*BMWM4CSL[3]
		AUDIR8GTW = AUDIR8GT[0] / AUDIR8GT[2] - 0.5*AUDIR8GT[3]
		GT2RS = GT2RSClubsport[0] / GT2RSClubsport[2] - 0.5*GT2RSClubsport[3] 
		P1GTRW = P1GTR[0] / P1GTR[2] - 0.5*P1GTR[3]
		if BugattiW > BMWM4CSLW AND BugattiW > AUDIR8GTW AND BugattiW > GT2RS AND BugattiW > P1GTRW:
			print("Der Bugatti Chiron Supersport+ hat das Rennen gewonnen!")
		elif BMWM4CSLW > BugattiW AND BMWM4CSLW > AUDIR8GTW AND BMWM4CSLW > GT2RS AND BMWM4CSLW > P1GTRW:
			print("Der BMW M4 CSL hat das Rennen gewonnen!")
		elif AUDIR8GTW > BugattiW AND AUDIR8GTW > BMWM4CSLW AND AUDIR8GTW > GT2RS AND AUDIR8GTW > P1GTRW:
			print("Der Audi R8 GT hat das Rennen gewonnen!")
		elif GT2RS > BugattiW AND GT2RS > BMWM4CSLW AND GT2RS > AUDIR8GTW AND GT2RS > P1GTRW:
			print("Der Porsche GT2 RS Clubsport hat das Rennen gewonnen!")
		else
			print("Der McLaren P1 GTR hat das Rennen gewonnen!")

	if tipp == 'Bugatti' AND BugattiW > BMWM4CSLW AND BugattiW > AUDIR8GTW AND BugattiW > GT2RS AND BugattiW > P1GTRW:
		print("HERZLICHEN GLÜCKWUNSCH!! Der Bugatti Chiron Supersport hat gewonnen!")
		g = g + n
		print(g)
	elif tipp == 'BMWM4CSL' AND BMWM4CSLW > BugattiW AND BMWM4CSLW > AUDIR8GTW AND BMWM4CSLW > GT2RS AND BMWM4CSLW > P1GTRW:
		print("HERZLICHEN GLÜCKWUNSCH!! Der BMW M4 CSL hat gewonnen!")
		g = g + n
		print(g)
	elif tipp == 'AUDIR8GT' AND AUDIR8GTW > BugattiW AND AUDIR8GTW > BMWM4CSLW AND AUDIR8GTW > GT2RS AND AUDIR8GTW > P1GTRW:
		print("HERZLICHEN GLÜCKWUNSCH!! Der Audi R8 GT hat gewonnen!")
		g = g + n
		print(g)
	elif tipp == 'GT2RS Clubsport' AND GT2RS > BugattiW AND GT2RS > BMWM4CSLW AND GT2RS > AUDIR8GTW AND GT2RS > P1GTRW:
		print("HERZLICHEN GLÜCKWUNSCH!! Der Porsche GT2 RS Clubsport hat gewonnen!")
		g = g + n
		print(g)
	elif tipp == 'P1 GTR' AND P1GTRW > BugattiW AND P1GTRW > BMWM4CSLW AND P1GTRW > AUDIR8GTW AND P1GTRW > GT2RS:
		print("HERZLICHEN GLÜCKWUNSCH!! Der McLaren P1 GTR hat gewonnen!")
		g = g + n
		print(g)
	else:
		print("Sie haben die Wette verloren!!")
		g = g - n
		print(g)
	u = input('Sie haben die Chance noch einen besonderen Preis zugewinnen, wenn Sie eine Zahl zwischen 0 und 1000 eingeben: ")
	while u>1000:
		print("Diese Zahl ist nicht in der möglichen Menge enthalten. Geben Sie eine Zahl zwischen 0 und 1000!")
		u = input('Sie haben die Chance noch einen besonderen Preis zugewinnen, wenn Sie eine Zahl zwischen 0 und 1000 eingeben: ")
	for m in range(1,10):
		d = ((m + 10)^10)%7
		print(d)
		if d == u:
			print("HERZLICHEN GLÜCKWUNSCH!! Sie haben den besonderen Preis gewonnen! Melden Sie sich bei einer zuständigen Person!")
		else:
			print("Sie haben leider nicht gewonnen. Beim nächten Mal gewinnen Sie bestimmt!")
		
		
		
# Ausgabe der einzelnen Funktionen
print(def infos())
print(def verschrennen())
