# Was kann man in Python alles verrechnen
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
a = int(12)
b = "Haus"
c = [1,'Dreiundzwanzig',56,'bobbycar']
d = float(1)
e = True

#x = a+b
#print(x)-> Verrechnung nicht möglich!!-> Die Datentypen int und String können nicht verrechnet werden
#y = a+c
#print(y)-> Verrechnung nicht möglich!!-> Die Datentypen int und list können nicht verrechnet werden
z = a+d
print(z)#-> 13
m = a+e
print(m)#-> 13.0
#n = b+c
#print(n)-> Verrechnung nicht möglich!!-> Die Datentypen String und list können nicht verrechnet werden
#k = b+d
#print(k)-> Verrechnung nicht möglich!!-> Die Datentypen String und float können nicht verrechnet werden
#l = b+e
#print(l)-> Verrechnung nicht möglich!!-> Die Datentypen String und boolean können nicht verrechnet werden
#i = c+d
#print(i)-> Verrechnung nicht möglich!!-> Die Datentypen list und float können nicht verrechnet werden
#j = c+e
#print(j)-> Verrechnung nicht möglich!!-> Die Datentypen list und boolean können nicht verrechnet werden
h = d+e
print(h)#-> 2.0

#String + String
t = "Haus"
s = "Hund"
r = s + t
print(r)#-> HundHaus
#String - String
#w = s - t ->Verrechnung nicht möglich
#print(w)
#String * String
#q = s * t ->Verrechnung nicht möglich
#print(q)
#Sting / String
#u = s / t ->Verrechnung nicht möglich
#print(u)

#Menge + Menge
ab = {1,2}
ac = {3,4}
#ad = ab + ac
#print(ad)-> TypeError: unsupported operand type(s) for +: 'set' and 'set'

#Menge - Menge
af = ab-ac
print(af)
