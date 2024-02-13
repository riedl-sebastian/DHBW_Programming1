# Different Typs of Sortingmechanisms

from tkinter import *
from tkinter.ttk import Combobox
import random
import time

# Funktionen

# Auswahlen
def w():
    auswahl=combi.get()
    auswahl2=combi2.get()
    if auswahl=='InsertionSort':
        if auswahl2=='short':
            startzeit=time.time()
            elements=[random.randint(1,1000)for _ in range(100)]
            for i in range(1,len(elements)):
                m=elements[i]
                j=i-1
                while j>=0 and m<elements[j]:
                    elements[j+1]=elements[j]
                    j=j-1
                elements[j+1]=m
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']=geszeit
            Label3['text']=elements
        elif auswahl2=="mid":
            startzeit=time.time()
            elements=[random.randint(1,1000)for _ in range(200)]
            for i in range(1,len(elements)):
                m=elements[i]
                j=i-1
                while j>=0 and m<elements[j]:
                    elements[j+1]=elements[j]
                    j=j-1
                elements[j+1]=m
            endzeit=time.time()
            geszeit=endzeit-startzeit()
            Label4['text']=geszeit
            Label3['text']=elements
        elif auswahl2=="long":
            startzeit=time.time()
            elements=[random.randint(1,1000)for _ in range(500)]
            for i in range(1,len(elements)):
                m=elements[i]
                j=i-1
                while j>=0 and m<elements[j]:
                    elements[j+1]=elements[j]
                    j=j-1
                elements[j+1]=m
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']=geszeit
            Label3['text']=elements
        elif auswahl2=="very long(decades)":
            startzeit=time.time()
            elements=[random.randint(1,10000)for _ in range(1000)]
            for i in range(1,len(elements)):
                m=elements[i]
                j=i-1
                while j>=0 and m<elements[j]:
                    elements[j+1]=elements[j]
                    j=j-1
                elements[j+1]=m
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']=geszeit
            Label3['text']=elements
        else:
            pass
    elif auswahl=='Quicksort':
        if auswahl2=="short":
            def aufteilen(lst,niedrig,hoch):
                pivot=lst[hoch]
                i=niedrig-1
                for j in range(niedrig,hoch):
                    if lst[j]<=pivot:
                        i =i+1
                        lst[i],lst[j]=lst[j],lst[i]
                        lst[i+1],lst[hoch]=lst[hoch],lst[i+1]
                        return i+1
            def sort(lst,niedrig,hoch):
                if niedrig<hoch:
                    pi=aufteilen(lst,niedrig,hoch)
                    sort(lst,niedrig,pi-1)
                    sort(lst,niedrig+1,hoch)
            elements=[random.randint(1,1000)for _ in range(100)]
            size=len(elements)
            sort(elements,0,size-1)
            Label3['text']=elements
        elif auswahl2=="mid":
            def aufteilen(lst,niedrig,hoch):
                pivot=lst[hoch]
                i=niedrig-1
                for j in range(niedrig,hoch):
                    if lst[j]<=pivot:
                        i =i+1
                        lst[i],lst[j]=lst[j],lst[i]
                        lst[i+1],lst[hoch]=lst[hoch],lst[i+1]
                        return i+1
            def sort(lst,niedrig,hoch):
                if niedrig<hoch:
                    pi=aufteilen(lst,niedrig,hoch)
                    sort(lst,niedrig,pi-1)
                    sort(lst,niedrig+1,hoch)
            elements=[random.randint(1,1000)for _ in range(200)]
            size=len(elements)
            sort(elements,0,size-1)
            Label3['text']=elements
        elif auswahl2=="long":
            def aufteilen(lst,niedrig,hoch):
                pivot=lst[hoch]
                i=niedrig-1
                for j in range(niedrig,hoch):
                    if lst[j]<=pivot:
                        i =i+1
                        lst[i],lst[j]=lst[j],lst[i]
                        lst[i+1],lst[hoch]=lst[hoch],lst[i+1]
                        return i+1
            def sort(lst,niedrig,hoch):
                if niedrig<hoch:
                    pi=aufteilen(lst,niedrig,hoch)
                    sort(lst,niedrig,pi-1)
                    sort(lst,niedrig+1,hoch)
            elements=[random.randint(1,1000)for _ in range(500)]
            size=len(elements)
            sort(elements,0,size-1)
            Label3['text']=elements
        elif auswahl2=="very long(decades)":
            def aufteilen(lst,niedrig,hoch):
                pivot=lst[hoch]
                i=niedrig-1
                for j in range(niedrig,hoch):
                    if lst[j]<=pivot:
                        i =i+1
                        lst[i],lst[j]=lst[j],lst[i]
                        lst[i+1],lst[hoch]=lst[hoch],lst[i+1]
                        return i+1
            def sort(lst,niedrig,hoch):
                if niedrig<hoch:
                    pi=aufteilen(lst,niedrig,hoch)
                    sort(lst,niedrig,pi-1)
                    sort(lst,niedrig+1,hoch)
            elements=[random.randint(1,10000)for _ in range(1000)]
            size=len(elements)
            sort(elements,0,size-1)
            Label3['text']=elements
        else:
            pass
    elif auswahl=='Bubblesort':
        if auswahl2=="short":
            startzeit=time.time()
            elements=[random.randint(1,1000)for _ in range(100)]
            n=len(elements)
            for i in range(n):
                for j in range(0,n-i-1):
                    if elements[j]>elements[j+1]:
                        elements[j],elements[j+1]=elements[j+1],elements[j]
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']=geszeit
            Label3['text']=elements
        elif auswahl2=="mid":
            startzeit=time.time()
            elements=[random.randint(1,1000)for _ in range(200)]
            n=len(elements)
            for i in range(n):
                for j in range(0,n-i-1):
                    if elements[j]>elements[j+1]:
                        elements[j],elements[j+1]=elements[j+1],elements[j]
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']=geszeit
            Label3['text']=elements
        elif auswahl2=="long":
            startzeit=time.time()
            elements=[random.randint(1,1000)for _ in range(500)]
            n=len(elements)
            for i in range(n):
                for j in range(0,n-i-1):
                    if elements[j]>elements[j+1]:
                        elements[j],elements[j+1]=elements[j+1],elements[j]
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']=geszeit
            Label3['text']=elements
        elif auswahl2=="very long(decades)":
            startzeit=time.time()
            elements=[random.randint(1,10000)for _ in range(1000)]
            n=len(elements)
            for i in range(n):
                for j in range(0,n-i-1):
                    if elements[j]>elements[j+1]:
                        elements[j],elements[j+1]=elements[j+1],elements[j]
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']=geszeit
            Label3['text']=elements
        else:
            pass
    elif auswahl=='Mergesort':
        if auswahl2=="short":
            startzeit=time.time()
            elements=[random.randint(1,1000)for _ in range(100)]
            def merge_sort(liste):
                if len(liste)<=1:
                    return liste
                mid = len(liste)//2
                links=merge_sort(liste[:mid])
                rechts=merge_sort(liste[mid:])
                return merge(links,rechts)
            def merge(links,rechts):
                sortiert=[]
                linksIndex=rechtsIndex=0
                while linksIndex < len(links) and rechtsIndex < len(rechts):
                    if links[linksIndex]<=rechts[rechtsIndex]:
                        sortiert.append(links[linksIndex])
                        rechtsIndex +=1
                while linksIndex<len(links):
                    sortiert.append(links[linksIndex])
                    linksIndex +=1
                while rechtsIndex < len(rechts):
                    sortiert.append(rechts[rechtsIndex])
                    rechtsindex +=1
                return sortiert
            elements=[random.randint(1,1000)for _ in range(100)]
            Sort=merge_sort(elements)
            Label3['text']=Sort
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']=geszeit
        elif auswahl2=="mid":
            startzeit=time.time()
            elements=[random.randint(1,1000)for _ in range(200)]
            def merge_sort(liste):
                if len(liste)<=1:
                    return liste
                mid = len(liste)//2
                links=merge_sort(liste[:mid])
                rechts=merge_sort(liste[mid:])
                return merge(links,rechts)
            def merge(links,rechts):
                sortiert=[]
                linksIndex=rechtsIndex=0
                while linksIndex < len(links) and rechtsIndex < len(rechts):
                    if links[linksIndex]<=rechts[rechtsIndex]:
                        sortiert.append(links[linksIndex])
                        rechtsIndex +=1
                while linksIndex<len(links):
                    sortiert.append(links[linksIndex])
                    linksIndex +=1
                while rechtsIndex < len(rechts):
                    sortiert.append(rechts[rechtsIndex])
                    rechtsindex +=1
                return sortiert
            elements=[random.randint(1,1000)for _ in range(200)]
            Sort=merge_sort(elements)
            Label3['text']=Sort
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']=geszeit
        elif auswahl2=="long":
            startzeit=time.time()
            elements=[random.randint(1,1000)for _ in range(500)]
            def merge_sort(liste):
                if len(liste)<=1:
                    return liste
                mid = len(liste)//2
                links=merge_sort(liste[:mid])
                rechts=merge_sort(liste[mid:])
                return merge(links,rechts)
            def merge(links,rechts):
                sortiert=[]
                linksIndex=rechtsIndex=0
                while linksIndex < len(links) and rechtsIndex < len(rechts):
                    if links[linksIndex]<=rechts[rechtsIndex]:
                        sortiert.append(links[linksIndex])
                        rechtsIndex +=1
                while linksIndex<len(links):
                    sortiert.append(links[linksIndex])
                    linksIndex +=1
                while rechtsIndex < len(rechts):
                    sortiert.append(rechts[rechtsIndex])
                    rechtsindex +=1
                return sortiert
            elements=[random.randint(1,1000)for _ in range(500)]
            Sort=merge_sort(elements)
            Label3['text']=Sort
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']==geszeit
        elif auswahl2=="very long(decades)":
            startzeit=time.time()
            elements=[random.randint(1,10000)for _ in range(1000)]
            def merge_sort(liste):
                if len(liste)<=1:
                    return liste
                mid = len(liste)//2
                links=merge_sort(liste[:mid])
                rechts=merge_sort(liste[mid:])
                return merge(links,rechts)
            def merge(links,rechts):
                sortiert=[]
                linksIndex=rechtsIndex=0
                while linksIndex < len(links) and rechtsIndex < len(rechts):
                    if links[linksIndex]<=rechts[rechtsIndex]:
                        sortiert.append(links[linksIndex])
                        rechtsIndex +=1
                while linksIndex<len(links):
                    sortiert.append(links[linksIndex])
                    linksIndex +=1
                while rechtsIndex < len(rechts):
                    sortiert.append(rechts[rechtsIndex])
                    rechtsindex +=1
                return sortiert
            elements=[random.randint(1,10000)for _ in range(1000)]
            Sort=merge_sort(elements)
            Label3['text']=Sort
            endzeit=time.time()
            geszeit=endzeit-startzeit
            Label4['text']=geszeit
        else:
            pass
    else:
        if auswahl2=="short":
            Label3['text']="Still in Construction"
        elif auswahl2=="mid":
            Label3['text']="Still in Construction"
        elif auswahl2=="long":
            Label3['text']="Still in Construction"
        elif auswahl2=="very long(decades)":
            Label3['text']="Still in Construction"
# neuen Text in Label2 laden
def aktlabel():
    auswahl=combi.get()
    if auswahl=='InsertionSort':
        Label2['text']="Element wird aus dem alten Array in ein neues Array an\nder richtigen Stelle hinzugefügt"
    elif auswahl=='Quicksort':
        Label2['text']="Aufteilung der Liste in zwei Teillisten bezüglich eines Pivot-Elements,\nwobei in einer Liste alle Elemente größer als das Pivot/Referenz-Element sind,\nin dem anderen Teil sind alle Elemente kleiner als das Pivot-Element."
    elif auswahl=='Bubblesort':
        Label2['text']="Zwei Werte werden miteinander verglichen, der kleinere vor den größeren \ngeschrieben"
    elif auswahl=='Mergesort':
        Label2['text']="Aufteilung in mehrere Teile, sortieren der einzelnen Teile, dann die\nTeile wieder zusammenfügen"
    else:
        Label2['text']="größten Wert in der Liste suchen und an die letzte Stelle packen\ndann mit dem nächsten kleineren weitermachen "
# Hauptfenster erstellen
sort=Tk()
sort.title("Different Sortingmechanisms")
sort.geometry("600x400")

# Elemente

# Fenster inf.:
def java():
    java=Tk()
    java.geometry("800x800")
    java.title("Code in Java")
    java.configure(bg="green")

    schlies=Button(java, text="close", command=java.destroy)
    label1=Label(java,text="Insertionsort:\nUmsetzung der typisch menschlichen Vorgehensweise zum sortieren, z. B.\neines Stapels Karten.\nMan nimmt die erste Karte des ersten Stapels und beginnt mit ihr einen neuen Stapel.\nAlle anderen Karten werden dann der Reihe nach in den neuen Stapel einsortiert.",)
    label2=Label(java,text="Code:\npublic static void insertion(int [] array){\nint j,m;\n for() int i=1,1<array.length,i++){\ni=j;array[i]=m;\nwhile(j>0 && array[j-1]>m){\narray[j]=array[j-1];\nj--;\n}\narray[j]=m;\n}\n}")
    label3=Label(java,text="Selectionsort:\nBei diesem Sortierverfahren wird immer das größte Element des\nArrays ausgewählt und an die letzte postion gepackt")
    label4=Label(java,text="Code:\nprivate static void selection(int [] array){\nint markter=array.lenght-1;\nwhile(marker>=0){\nint max=0;\nfor(int i=1,i<=marker,i++){\nif(array[i]>array[max])max=i;\nswamp(array, i, marker)\n}\nmarker--;\n}\n}")
    label5=Label(java,text="Bubblesort:\nGrößere von einer Flüssigkeit aufsteigende Blasen überholen die kleineren Blasen.")
    label6=Label(java,text="private static void bubble(int [] array){\ndo{\nboolean swamped=flase;\nfor(int i=0;i<array.lenght-1,i++){\nif (array[i]>array[i+1]){\nswamp(array, i, i+1);\nswamped=true;\n}while(swamped)\n}")

    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    label6.pack()
    schlies.pack()

# Start-Button
start=Button(sort,text="start",command=w)

# Select-Button:
select=Button(sort,text="select",command=aktlabel)

# Infos zu verfahren öffenen
ink=Button(sort, text="Informations to mechanisms",command=java)

# Schließen-Button
schliessen=Button(sort,text="close",command=sort.destroy)
# Combobox
opts=["InsertionSort","Quicksort","Bubblesort","Mergesort","Selectionsort"]
combi=Combobox(sort, values=opts)
combi.current(0)

combi.bind('<<ComboboxSelect>>',w)
# Auswahl verschiedener Arrays
opts2=["short","mid","long","very long(decades)"]
combi2=Combobox(sort,values=opts2)
combi2.current(0)

combi2.bind('<<ComboboxSelect>>',w)

# Labels
Label1=Label(sort,text="This application allows you to choose between different Sorting-Mechanisms",fg="red")
# Beschreibungslabel
Label2=Label(sort,text="Description of mechanisms after selection")
# Ergebnissvorschau
Label3=Label(sort,text="Result-preview")
# Timerausgabe
Label4=Label(sort,text="Timer", bg="white",fg="red")


# Anordung der Elemente

Label1.grid(row=1,column=1)
Label2.grid(row=2,column=1)
Label3.grid(row=3,column=1)
Label4.grid(row=4,column=1)

combi.grid(row=2,column=0)
combi2.grid(row=4, column=0)

schliessen.grid(row=5, column=3)
select.grid(row=3,column=0)
ink.grid(row=5,column=3)
start.grid(row=5,column=0)
