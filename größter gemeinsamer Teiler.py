# ggT nach Euklid

def ggT(eingabe1,eingabe2):
    n=eingabe1
    x=eingabe2
    if x<n:
        m=x
    else:
        m=n
        z=n%x
    while z>=m:
        n=x
        x=z
        z=n%x
    return(z)

eingabe=int(input("Was ist die erste Zahl? "))
a=eingabe
eingabee=int(input("Was ist die zweite Zahl? "))
b=eingabee
ans=ggT(a,b)
print(ans, " ist der größte gemeinsame Teiler von ",a," und ",b," !")
