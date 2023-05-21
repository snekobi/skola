import random
from math import sqrt
from locale import delocalize
from pdb import lasti2lineno
import re
import math
import pprint
from tkinter import *
from tkinter.ttk import * 
from collections import Counter
from itertools import groupby
from decimal import Decimal


"""
def nacitaj():
    kam_data = []
    with open("31 kamosi.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            meno = lines[i].strip()
            udaje = lines[i+1].split()
            telefon = udaje[0]
            den = int(udaje[1])
            mesiac = int(udaje[2])
            rok = int(udaje[3])
            kam_data.append({"meno": meno, "telefon": telefon, "den": den, "mesiac": mesiac, "rok": rok})
    return kam_data

def utried(kam_data):
    return sorted(kam_data, key=lambda x: x["meno"])

def maju_nar(mesiac, rok):
    kam_data = nacitaj()
    existuje_osoba = False
    for osoba in kam_data:
        if osoba["mesiac"] == mesiac and osoba["rok"] == rok:
            existuje_osoba = True
            print(f"{osoba['meno']}    {osoba['den']}. {osoba['mesiac']}   {rok - osoba['rok']}")
    if not existuje_osoba:
        print("Žiadna osoba nemá narodeniny v danom mesiaci a roku.")
kamarati = nacitaj()
print(utried(kamarati))
maju_nar(2, 1973)


#32
def najvyssi_skok(skoky):
    najlepsi_pretekar = None
    najlepsi_skok = 0

    for riadok in skoky:
        data = riadok.split()
        cislo_pretekar = int(data[0])
        dlzky_skokov = [int(x) for x in data[1:]]

        for skok in dlzky_skokov:
            if skok == -1:
                continue

            if skok > najlepsi_skok:
                najlepsi_skok = skok
                najlepsi_pretekar = cislo_pretekar

    return najlepsi_pretekar, najlepsi_skok


# Načítanie údajov zo súboru
with open("32 skoky.txt", "r") as subor:
    vysledky = subor.readlines()

vysledky = [riadok.strip() for riadok in vysledky]

# Zistenie víťaza
vitaz, dlzka = najvyssi_skok(vysledky)

if vitaz is None:
    print("Žiadny pretekár nenastúpil na pretek.")
else:
    print(f"Zvíťazil pretekár s číslom {vitaz} s dĺžkou skoku {dlzka} cm.")

#33

y = [i for i in range(1, 11)]
z = [i for i in range(1, 11)]
random.shuffle(y)
random.shuffle(z)
meno = y
otazka = z
for i in range(10):
    print("Meno:", meno[i], "Otazka:", otazka[i])
skusanie = open("33 skusanie.txt", "w")
for i in range(10):
    print("Meno:", meno[i], "Otazka:", otazka[i], file = skusanie)


#34 - neviem
with open("34 rc.txt", "r") as rc:
    rclist = []
    for line in rc:
        rclist.append(line.split(None, 1)[0])
    #rclist = [int(i) for i in rclist]
    print(rclist)
    mesiace = ["Januar: ", "Februar: ", "Marec: ", "April: ", "Maj: ", "Jun: ", "Jul: ", "August: ",
                "September: ", "Oktober: ", "November: ", "December: "]
    for i in range (len(rclist)):
        d = rclist[i][4:6]
        m1 = rclist[i][2:4]
        m = int(m1)
        if m > 12:
            m -= 50
        r = rclist[i][0:2]
        for i in range(12):
            if m == mesiace[i]:
                print(mesiace[i], d, m, r)
            else:
                print(mesiace[i])

#35 - neviem text
with open("35 metro.txt","r") as metro:
    root = Tk()
    canvas = Canvas(root, width= 700, height = 500, bg = "white")
    canvas.pack()
    x = 10
    y = 200
    farba = metro.readline().strip()
    
    zastavky = metro.readlines()[2:]
    canvas.create_rectangle(x, y, x + 15, y + 15, outline = "", fill = farba)
    x += 15
    canvas.create_rectangle(x, y + 5, x + 20, y + 5, width = 1, outline = "", fill = farba)
    x += 20
    for line in zastavky:
        if line[0] == "*":
            canvas.create_oval(x, y, x + 10, y + 10, outline = farba)
        else:
            canvas.create_oval(x, y, x + 10, y + 10, outline = "",fill = farba)
        #canvas.create_text(x, y - 20, x + 30, y  -50, text = "Grand Central Station", fill = "black", font = "Arial 10")
        x += 10
        canvas.create_rectangle(x, y + 5, x + 20, y + 5, width = 1, outline = "", fill = farba)
        x += 20
canvas.create_rectangle(x, y, x + 15, y + 15, outline = "", fill = farba)
root.mainloop()




#36
with open("36 autobusy.txt", "r") as busy:
    root = Tk()
    canvas = Canvas(root, width= 700, height = 500, bg = "white")
    canvas.pack()
    x = 20
    y = 20
    kapacita = busy.readline()
    for line in busy.readlines()[1:]:
        canvas.create_text(x, y, x + 30, y  +30, text = line[3], fill = "black", font = "Arial 10")
root.mainloop()
#OPRAVIT TEXT


#37
with open("37 pacienti.txt", "r") as bmi:
    hmotlst = []
    bmis = []
    tuckovia = 0
    vysky = []
    menalist = []
    anorekticky = []
    rclist = []
    mzlist = []
    for line in bmi:
        hmotlst.append(line.split(" ")[2])
        vysky.append(line.split(" ")[3])
        rclist.append(line.split(" ")[1])
        menalist.append(line.split(" ")[0])
    
    hmotlst = [int(i) for i in hmotlst]
    vysky = [float(x.strip(' "')) for x in vysky]
    #print(rclist)
    for i in range (len(rclist)):
        rcdig = [x for x in rclist[i]]
        mzlist.append(rcdig[2])
    mzlist = [int(i) for i in mzlist]
  
    
    for i in range(len(vysky)):
        bmis.append(round(hmotlst[i] / (vysky[i] ** 2), 2))
        print("Meno:", menalist[i])
        print("Hmotnost:", hmotlst[i], "kg")
        print("BMI:", round(hmotlst[i] / (vysky[i] ** 2), 2))
    for i in range(len(bmis)):
        if bmis[i] > 30:
            tuckovia += 1
        if mzlist[i] > 4 and bmis[i] < 18.5:
            anorekticky.append(menalist[i])
    print("Pocet obeznych ludi:", tuckovia)
    print("Chude z*ny:", anorekticky)



#38
def uprav_vylety(subor):
    vylety = []
    with open(subor, "r") as f:
        for riadok in f:
            riadok = riadok.strip()
            casti = riadok.split(" ")
            datum = casti[0]
            vzdialenost = float(casti[1])
            trvanie = int(casti[2])
            ciel = " ".join(casti[3:])
            hodiny = trvanie // 60
            minuty = trvanie % 60
            trvanie_upravene = f"{hodiny}:{minuty:02d}"
            priemer_rychlosti = vzdialenost / (trvanie / 60)
            vylety.append((datum, vzdialenost, trvanie_upravene, priemer_rychlosti, ciel))
    return vylety

def vypis_vylety(vylety):
    for vylet in vylety:
        datum, vzdialenost, trvanie, priemer_rychlosti, ciel = vylet
        print(f"{datum} {vzdialenost:.1f} {trvanie} {priemer_rychlosti:.1f} {ciel}")

vylety = uprav_vylety("38 cyklovylety.txt")
vypis_vylety(vylety)

#39
with open("39 anketa.txt", 'r') as anketa:
    otazka = anketa.readlines()[0]
with open("39 anketa.txt", 'r') as anketa:
    #otazka = anketa.readlines()[0]
    lines = anketa.readlines()[1]
    lines = lines.split(" ")
    ano = (lines[0])
    nie = (lines[1])
    neviem = (lines[2])
    #print(otazka)
    print("Pocet ludi ktori hlasovali za ano:", ano)
    print("Pocet ludi ktori hlasovali za nie:", nie)
    print("Pocet ludi ktori hlasovali za neviem:", neviem)
    hlasano = ("1)Ano -", ano)
    root = Tk()
    canvas = Canvas(root, width= 700, height = 500, bg = "white")
    canvas.pack()

    x = 10
    y= 10
    canvas.create_text(x + 130, y + 10, text = otazka, font = "Arial 10", fill = "black")
    y += 30
    canvas.create_text(x + 50, y + 10, text = hlasano, font = "Arial 10", fill = "black")


    root.mainloop()


#41
with open("41 elektricky.txt", "r") as elektricky:
    trasypocet = len(elektricky.readlines())
    print("Pocet tras v meste:", trasypocet)
with open("41 elektricky.txt", "r") as elektricky:
    trasy = []
    trasa = 1
    for line in elektricky:
        trasy.append(line.strip())
        trasy = trasy[0].split(" ")
        if trasy[0] == trasy[-1]:
            print("Linka cislo", trasa, "konci vo vychodiskovej zastavke")
        else:
            print("Linka cislo", trasa, "nekonci vo vychodiskovej zastavke")
        revtrasa = trasy[::-1]
        if trasy == revtrasa:
            print("Tato linka ide naspat po rovnakej trase")
        else: 
            print("Tato linka ide naspat po inej trase")
        trasy.clear()
        trasa += 1


#42
with open("42 smsky.txt", "r") as smsky:
    newlines = []
    for line in smsky:
        newlines.append(line.title())
with open("42 smsky.txt", "r") as smsky:
    newlines = [line.replace(" ", "") for line in newlines]
    print(*newlines)

#43
priklady = []
zlepriklady = []
vysledky = []
opravysledky = []
body = 0

fpriklady = open("43 nasobilka_vystup.txt", "w")
for i in range(10):
    x = random.randint(1,10)
    y = random.randint(1,10)
    print(x,"*",y)
    prik = x,"*",y
    
    vysledok = x * y
    vysledky.append(vysledok)
    priklady.append(str(prik))
for i in range(len(priklady)):
    priklady[i] = priklady[i].replace(",", "").replace("(", "").replace("'","").replace(")", "")
#print(priklady)
fpriklady = open("43 nasobilka_vystup.txt", "w")
for i in range(len(priklady)):
    fpriklady.write(priklady[i])
    fpriklady.write("\n")
vysledky = [int(i) for i in vysledky]
for i in range(len(vysledky)):
    odhad = (int(input("Zadaj vysledok: ")))
    if odhad == vysledky[i]:
        body += 1
    else:
        priklady[i] == priklady[-1]
        zlepriklady.append(priklady[i])
        opravysledky.append(vysledky[i])
for i in range(len(zlepriklady)):
    print(*zlepriklady[i])
    odhad = (int(input("Zadaj vysledok: ")))
    if odhad == opravysledky[i]:
        print("Uz to mas spravne, ale bod nedostanes lmao")
    else:
        print("Stale si sprosty")
print("Pocet bodov:", body)
#print(priklady)
"""

#44
root = Tk()
canvas = Canvas(root, width= 700, height = 350, bg = "white")
canvas.pack()
x = 150
y = 100
cislo1 = random.randint(11, 20)
cislo2 = random.randint(2, 9)
priklad = cislo1, ":", cislo2, "="
canvas.create_text(x, y, text = priklad, fill = "black", font = "Arial 50")
vstup = Entry(root)
canvas.create_window(200, 300, window = vstup)
def podiel():
    vysledok = vstup.get
button1 = Tk.button(text = "Skontroluj", command = podiel)




root.mainloop()
