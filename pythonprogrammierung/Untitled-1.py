from tkinter import *
import os

window = Tk()

window.geometry("300x300")
window.title("Fenster mit Bunten Buttons")

window.configure(background="blue")

schliessen=Button(window,text="Schließen", command=window.destroy, bg="red", fg="yellow")
label1=Label(window, text="Dieses Fenster wird auf Windows 10 64 bit ausgeführt", bg="green", fg="white")
def textchange():
    neu=os.cwd()
    label1.config(text=neu,bg="black",fg="red")

def anderes_Fenster():
    adf=Tk()
    adf.title("???")
    label3=Label(adf,text="No Help availabel")
    label3.pack()
    schliessen2=Button(adf,text="Schließen",command=adf.destroy)
    schliessen2.pack()

aendern=Button(window,text="Aktuelles Verzeichnis", command=textchange)
help1=Button(window,text="help",command=anderes_Fenster)

help1.grid(row=0,column=0)
label1.grid(row=1,column=1)
schliessen.grid()
