# Python Autowetten ohne def von Funktionen, da diese heute einfach keinen Bock hatten

GT2RSClubsport = [700, 3800, 7, 1390] 
BMWM4CSL = [1000, 2993, 8, 1618, ]
AUDIR8GT = [620, 5200, 8, 1570]
P1GTR = [1000, 3800, 7, 1395]
Bugatti = [1600, 8000, 8, 1825]
print("Welches Auto interessiert Sie besonders?")
print("Zur Auswahl stehen: ")
print("                    Bugatti")
print("                    Porsche")
print("                    BM4 M4 CSL")
print("                    McLaren P1 GTR")
print("                    Audi R8 GT")
print()
info = input('Ihre Entscheidung: ')

if info == 'Porsche':
    print("Der Porsche GT2RS Clubsport verfügt über einen 700Ps starken 6 Zylinder Aluminium Biturbo-Boxermotor in Hecklage und starrer Aufhängung. Der Hubraum beträg 3.800 Kubik-Centimeter, der Kolbenhub liegt bei 77,5mm. Das 7-Gang PDK Getriebe in ebenfalls starrer Aufhängung sorgt für kurze Schaltzeiten und eine maximale Drehmomentsübertragung. Das Fahrzeug wiegt 1380kg und verfügt über eine Heckantrieb. Der Drehmoment liegt ebenfalls bei ca. 770Nm.")
elif info == 'BMW M4 CSL':
    print("Der BMW M4 CSL verfügt über einen V6-Schmiedemotor mit 550Ps in Frontlage mit starrer Aufhängung. Der Hubraum beträgt 2993 Kubikcentimeter. Ein herausstechen des Detail des M4 CSL ist sein Turbolader mit einem Maximaldruck von 2,1 Bar. Das sportlichste Modell der 4er-Reihe verfügt über ein Automatisches-8-Gang-Getriebe welches einen schnellen Gangwechsel und eine großartige Drehmomentübertragung liefer. Typisch für BMW verfügt auch dieser über einen Heckantrieb. Der Drehmoment liegt etwas unter dem seines großen Bruder, des M5 CS. Hierbei gehen wir jedoch von der Britischen Version des M4 CSL´s aus, welche über 1000Ps verfügt. Zudem wurde das Chassi verstärkt, was für eine verbesserte Kurvelage sorgt.")
elif info == 'Audi R8 GT':
    print("Der Audi R8 GT ist die sportlichere Version des R8 V10, dieser verfügt ebenfalls über einen 5,2 Liter V10 Aluminium-Motor in Hecklage mit einer direkten Fahrtwindkühlung. Der Audi ist bekannt für seine hervorragende Kurvenlage und seinen exzellenten Allrad-Antrieb, das Renndifferenzial lässt trotzdem noch zu wünschen übrig. Das Renndifferenzials sorgt durch die möglichst effektive Verlagerung des Drehmoments teilweise für kurze Leistungsverlust nach einem  Schalten des 8-Gang-Automatik-Getriebes. Jetzt aber wieder mehr zu den technischen Details: Der Motor des Audis hat nämlich noch einen Trumpf, der sogar den V10 6.2l des Adventador SVJ alt aussehen lässt - der Drehzahlbegrenzer schlägt erst bei 8600 Umdrehungen pro Minute zu, bei so einer Umdrehungszahl und Hubraum ist der Abgasstrom sehr voluminös, wodurch die Aufladung des Turbladers extrem schnell geschieht.")
elif info == 'McLaren P1 GTR':
    print("Der P1 GTR ist die Motorsport Version des P1s und verfügt über einen 3,8-Liter-BI-Turbo-V8 Motor, welcher sich ebenfalls im Heck befindet. Der Motor bring eine Leistungvon 1000Ps, während das Gewicht nur bei 1395 Kilogramm liegt. Der P1 GTR ist leider nicht auf öffenlichen Straßen zulassbar. Damit das Gewicht so gering ausfällt, bestehen grosse Teile der Verkleidung aus Carbon. Das Chassi besteht zu Großteil aus Aluminium. Ein weiteres interessantes Detail des P1 GTRs ist sein auffälliges Heck: in den normalerweise etwas mehr verkleideten Luftdurchlässen lassen sich zwei rote Luftfilter in Zylinderform erkennen. Durch diese liegt die Luftansaugung bei ca. 800 Liter pro Minute (etwas niedriger als bei einem Bugatti Chiron, dessen liegt bei 1000 Liter pro Sekunde).")
else:
    print("Der Bugatti Chiron Supersport 300+ ist noch nachgewiesen das schnellste Auto der Welt mit einer Geschwindigkeit von 490,484km/h, dieser Rekord wurde auf einer speziellen Test-strecke nahe Wolfsburg erzielt. Noch, da der Koenigsegg Jesko Absolute angeblich eine Höchstgeschwindigkeit von über 500km/h erreichen kann, dies wurde jedoch noch nicht offziell erfasst. Ein Serien-Bugatti Chiron Supersport 300+, von dem es nur 30 Stück gibt, schaft unter normalen Bedingungen eine Höchstgeschwindigkeit von 440km/h. Der Bugatti verfügt über Chiron Supersport 300+  ist ebenfalls sehr bemerkenswert: bei einem Druck von 50t verschiebt sich das Chassi nur um ca. 1°. Durch diese ausergewöhnliche Stärke werden solche Geschwindigkeiten erst möglich.")
print()
eingabe1 = input('Geben Sie Ihren Spielvermögen für den Abend ein: ')
g = int(eingabe1)
print()
tipp = input('Geben Sie das Auto ein, auf das Sie setzten: ')
print()
while g<1000:
    print("Der Mindestspielbetrag liegt bei 1000 Euro!")
if g<10000000 and g>10000:
    print("Wir danken Ihnen für den Spaß an unserem Spiel und Ihren leichtsinnigen Umgang mit Geld!")
    t = g/100*90 
    s = 5000
    print("Wenn Sie mehr als " , t , " Euro ihres Spielvermögens auf ein Spiel setzen, bekommen Sie 5000Euro auf Ihr Spielvermögen!")
else:
    print("Viel Spaß beim Wetten!")
print()
eingabe3 = input('Geben Sie Ihren Einsatz für das Renne ein: ')
n = int(eingabe3)
t = g/100*90
print()
if(n>=t):
    s=5000
    g = g + s
    print("Ihr Spielvermögen liegt derzeit bei ", g ,"Euro")
    print()
rennen = input("Welche Art von Rennen solle die Autos fahren? (Moeglichkeiten: Dragrace(1), Sprintrennen(2), Rundkurs(3), Technical(4)): ")
rennen_1= int(rennen)
print(".......................Rennen wird simuliert.........................................")
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
    print("Ihr derzeitiges Spielvermögen liegt bei ", g, " Euro!")
elif tipp == 'BMWM4CSL' and BMWM4CSLW > BugattiW and BMWM4CSLW > AUDIR8GTW and BMWM4CSLW > GT2RS and BMWM4CSLW > P1GTRW:
    print("HERZLICHEN GLÜCKWUNSCH!! Der BMW M4 CSL hat gewonnen!")
    g = g + n
    print("Ihr derzeitiges Spielvermögen liegt bei ", g, " Euro!")
elif tipp == 'AUDIR8GT' and AUDIR8GTW > BugattiW and AUDIR8GTW > BMWM4CSLW and AUDIR8GTW > GT2RS and AUDIR8GTW > P1GTRW:
    print("HERZLICHEN GLÜCKWUNSCH!! Der Audi R8 GT hat gewonnen!")
    g = g + n
    print("Ihr derzeitiges Spielvermögen liegt bei ", g, " Euro!")
elif tipp == 'GT2RS Clubsport' and GT2RS > BugattiW and GT2RS > BMWM4CSLW and GT2RS > AUDIR8GTW and GT2RS > P1GTRW:
    print("HERZLICHEN GLÜCKWUNSCH!! Der Porsche GT2 RS Clubsport hat gewonnen!")
    g = g + n
    print("Ihr derzeitiges Spielvermögen liegt bei ", g, " Euro!")
elif tipp == 'P1 GTR' and P1GTRW > BugattiW and P1GTRW > BMWM4CSLW and P1GTRW > AUDIR8GTW and P1GTRW > GT2RS:
    print("HERZLICHEN GLÜCKWUNSCH!! Der McLaren P1 GTR hat gewonnen!")
    g = g + n
    print("Ihr derzeitiges Spielvermögen liegt bei ", g, " Euro!")
else:
    print("Sie haben die Wette verloren!!")
    g = g - n
    print("Ihr restliches Spielvermögen liegt bei ",g,"Euro!")
eingabe4 = input("Sie haben die Chance noch einen besonderen Preis zugewinnen, wenn Sie eine Zahl zwischen 0 und 1000 eingeben: ")
print()
u = int(eingabe4)
print()

if u<1000:
    print()
    for m in range(1,10):
        d = ((m + 10)^10)%7
        print(d)
        if d == u:
            print("HERZLICHEN GLÜCKWUNSCH!! Sie haben den besonderen Preis gewonnen! Melden Sie sich bei einer zuständigen Person!")
        else:
            print("Sie haben leider nicht gewonnen. Beim nächten Mal gewinnen Sie bestimmt!")
else:
    print("Sie haben keine Zahl innerhalb des Intervalls eingegeben! Wiederufen Sie Ihre Eingabe, indem hinter dem Folgenden JA eingeben!")
    h = input("Ich wiederufe meine Eingabe und Zahle eine Strafe von 5000 Euro: ")
    if h == 'JA':
        g = g - 5000
        print("Ihr Spielvermögen liegt bei ",g,"Euro!")
    else:
        while h != 'JA':
            print("dailing police")
		
print()

