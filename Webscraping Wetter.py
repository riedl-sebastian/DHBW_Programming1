# Wetterbericht

from tkinter import *
from tkinter.ttk import Combobox
from datetime import date
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
from io import BytesIO
import json
import webbrowser

# Abruf von Website

def wetterabruf(tag):
    url = "http://www.wetter24.de/vorhersage/karte/europa/deutschland/tag/",tag,"/"
    awt=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    bildmontagabruf=soup.find("div",{"id":"imgTagWrapperId"}).find("img")
    image_url=bildmontagabruf["src"]
    return bildmontagabruf

    

# Funktionen Hauptfenster
def webopen():
    webbrowser.open("http://www.wetter24.de")

def helpbutton():
    helpwindow=Tk()
    helpwindow.title("?")
    helpwindow.geometry("200x150")
    label1=Label(helpwindow,text="Dieses Fenster zeigt Ihnen den Wetterbericht dieser Woche an")
    label2=Label(helpwindow,text="Die Daten stammen vom Deutschen Wetterdienst.")
    label3=Label(helpwindow,text="Link: http://www.wetter24.de")
    buttonlinkd=Button(helpwindow,text="Visit",command=webopen)
    schliessen=Button(helpwindow,text="Schließen",command=helpwindow.destroy)

def montagfunk():
    montagstext=wetterabruf("montag")
    labeloben.config(text=montagstext)
    

def dienstagfunk():
    dienstagstext=wetterabruf("dienstag")
    labelstart.config(text=dienstagstext)
    
def mittwochfunk():
    mittwochstext=wetterabruf("mittwoch")
    labelstart.config(text=mittwochstext)

def donnerstagfunk():
    donnerstagstext=wetterabruf("donnerstag")
    labelstart.config(text=donnerstagstext)

def freitagfunk():
    freitagstext=wetterabruf("freitag")
    labelstart.config(text=freitagstext)

def samstagfunk():
    samstagstext=wetterabruf("samstag")
    labelstart.config(text=samstagstext)

def sonntagfunk():
    sonntagstext=wetterabruf("sonntag")
    labelstart.config(text=sonntagstext)

# Hauptfenster

wetterbericht = Tk()
wetterbericht.title("Wetterbericht")
wetterbericht.geometry("1000x800")

# Anschauungsbild oben
image1=Image.open("C:/theoretische Informatik/berge.jpg")
image1_tk=ImageTk.PhotoImage(image1)
labeloben=Label(wetterbericht,image=image1_tk)


# Startlabel in der Mitte(Main)
image2=Image.open("C:/theoretische Informatik/berge2.jpg")
image2_tk=ImageTk.PhotoImage(image2)
labelstart=Label(wetterbericht,text="",image=image2_tk)

# Helpbutton
helpbutton=Button(wetterbericht,text="Help?",command=helpbutton,bg="blue",fg="white")

# Datum ausgeben
aktuellesDatum=date.today()
date=Label(wetterbericht,text="Datum"+str(aktuellesDatum))

# Montags-Button
montag=Button(wetterbericht,text="Montag",command=montagfunk,bg="yellow")

# Dienstags-Button
dienstag=Button(wetterbericht,text="Dienstag",command=dienstagfunk,bg="yellow")

# Mittwochs-Button
mittwoch=Button(wetterbericht,text="Mittwoch",command=mittwochfunk,bg="yellow")

# Donnerstags-Button
donnerstag=Button(wetterbericht,text="Donnerstag",command=donnerstagfunk,bg="yellow")

# Freitags-Button
freitag=Button(wetterbericht,text="Freitag",command=freitagfunk,bg="yellow")

# Samstags-Button
samstag=Button(wetterbericht,text="Samstag",command=samstagfunk,bg="yellow")

# Sonntags-Button
sonntag=Button(wetterbericht,text="Sonntag",command=sonntagfunk,bg="yellow")

# Aufteilung:
#|Help|_|_|date|
#|_|Anschauungsbild|_|
#|Montag|
#|Dienstag|
#|Mittwoch|
#|Donnerstag|
#|Freitag|
#|Samstag|
#|Sonntag|
# Hauptfenster Aufbau

# Help-Button
helpbutton.grid(row=0,column=0)
# Date-Label
date.grid(row=0,column=3)
# Anschauungsbild
labeloben.grid(row=1,column=1)
# Montag-Button
montag.grid(row=1,column=0)
# Dienstag-Button
dienstag.grid(row=1,column=0)
# Mittwoch-Button
mittwoch.grid(row=1,column=0)
# Donnerstag-Button
donnerstag.grid(row=1,column=0)
# Freitags-Button
freitag.grid(row=1,column=0)
# Samstag-Button
samstag.grid(row=1,column=0)
# Sonntag-Button
sonntag-grid(row=1,column=0)
