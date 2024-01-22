# Ein Bild als Hintergrund eines Labels einfügen

from tkinter import *
from tkinter import PhotoImage

bildfenster=Tk()
bildfenster.title("Bild")
bildfenster.geometry("800x600")

bild = PhotoImage(file="C:/theoretische Informatik/CLK_GTR.jpg")
labelbild=Label(bildfenster,image=bild)
labelbild.pack()

bildfenster.mainloop()