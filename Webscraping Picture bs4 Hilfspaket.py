from tkinter import *
from tkinter.ttk import Combobox
from datetime import date
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import shutil
from urllib.parse import urljoin

main=Tk()
main.geometry("1000x800")
main.title("Wetterbericht für die nächsten 7 Tagen")

url="https://www.tagesschau.de/wetter/deutschland/wettervorhersage-deutschland-100.html"
response=requests.get(url, stream=True)
soup=BeautifulSoup(response.text,'html.parser')
image=soup.find('img')
img_src=image.get('src')
img_url=urljoin(url,img_src)
response = requests.get(img_url,stream=True)
with open('image.jpg','wb') as out_file:
    shutil.copyfileobj(response.raw,out_file)
image_open=Image.open("image.jpg")
bilds=ImagTk.PhotoImage(image_open)
mainlabel=tk.Label(main, image=bilds)

mainlabel.pack()
main.mainloop()