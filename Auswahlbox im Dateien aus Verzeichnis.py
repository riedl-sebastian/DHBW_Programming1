import os
import tkinter as tk


fenster = tk.Tk()


directory = os.getcwd()  
files = os.listdir(directory)  


lbox = tk.Listbox(fenster)
for file in files:
    lbox.insert(tk.END, file)
lbox.pack()


fenster.mainloop()
