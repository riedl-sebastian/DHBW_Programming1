from tkinter import *
from tkinter.ttk import Combobox

def drittfenster():
    dreifenster=Tk()
    dreifenster.title("Attention")
    dreifenster.geometry("200x200")
    label1=Label(dreifenster, text="Sie haben Ihre Auswahl nicht revidiert!", fg="red")
    label1.pack()
    jabu=Button(dreifenster, text="Ja, ich revidiere meine Auswahl.", command=dreifenster.destroy)
    jabu.pack()
    neinbu=Button(dreifenster, text="Nein!",command=fenster.destroy)


def zweitesfenster():
    zweifenster=Tk()
    zweifenster.title("Befehl")
    zweifenster.geomtery("200x200")
    label1=Label(zweifenster,text="Revidieren Sie Ihre Auswahl", fg="red")
    label1.pack()
    schaltfaeche=Button(zweifenster, text="yes",command=zweifenster.destroy)
    schaltfaeche.pack()
    schliessen=Button(zweifenster, text="Schließen",command=drittfenster)

fenster=Tk()
fenster.title("Combobox")
fenster.geometry("400x400")

label1=Label(fenster, text="Hallo, hier können sie verschiedene Sachen auswählen!")
label1.grid(row=0,column=0)

zeug=['\n','Haus','Auto','Hund','Katze','Maus']
ausw=Combobox('fenster', values=zeug)
ausw.grid(row=1,column=2)

schliessen=Button(fenster,text="Schließen", command=zweitesfenster, bg="red")
schliessen.grid(row=3,column=3)

fenster.mainloop()