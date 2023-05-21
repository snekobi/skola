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
"""
file = open("obesenec.txt", "r")
words = file.read().splitlines()
randword = random.randint(0, len(words)-1)
theword = words[randword]

lives = 10
print("Mas", lives, "zivotov")
secretword = re.sub("[0-9a-zA-Z]", "_", theword)
def guess(letter, theword, secretw):
    inword = False
    if letter in theword:
        inword = True
        for i in range(0, len(theword)):
            if theword[i] == letter:
                secretw = secretw[0:i] + letter + secretw[i+1:len(secretw)]
    return(inword, secretw)
print(secretword)

gssdlttr = input("Guess the letter: ")[:1]
foundlttr, secretword = guess(gssdlttr, randword, secretword)

if not foundlttr:
    lives -= 1
    if lives == 0:
        print("GG, you lost")
    else:
        print("Neuhadol si, ostava ti", lives, "zivotov")
        print(secretword)
else:
    if "_" not in secretword:
        print("\nVyhral si, congrats")
    else:
        print("Toto pismeno sa v slove skutocne nachadza, good job")
        print(secretword)


#2
def spracuj_vysledky(subor):
    vysledky = []
    krajiny = set()
    with open(subor, "r") as f:
        for riadok in f:
            riadok = riadok.strip()
            casti = riadok.split(" ")
            meno = casti[0]
            krajina = casti[1]
            vykony = list(map(int, casti[2:]))
            krajiny.add(krajina)
            vysledky.append((meno, krajina, vykony))
    return vysledky, krajiny

def vypis_krajiny(vysledky, krajiny):
    print("Zúčastnené krajiny:")
    for krajina in krajiny:
        print(krajina)

def vypis_pocet_sutaziacich(vysledky):
    pocet_sutaziacich = {}
    for vysledok in vysledky:
        krajina = vysledok[1]
        if krajina in pocet_sutaziacich:
            pocet_sutaziacich[krajina] += 1
        else:
            pocet_sutaziacich[krajina] = 1
    print("Počet súťažiacich z jednotlivých krajín:")
    for krajina, pocet in pocet_sutaziacich.items():
        print(f"{krajina}: {pocet}")

def vypis_vitazov(vysledky):
    najlepsi_vykon = 0
    vitazi = []
    for vysledok in vysledky:
        vykony = vysledok[2]
        max_vykon = max(vykony)
        if max_vykon > najlepsi_vykon:
            najlepsi_vykon = max_vykon
            vitazi = [(vysledok[0], vysledok[1])]
        elif max_vykon == najlepsi_vykon:
            vitazi.append((vysledok[0], vysledok[1]))
    print("Celkový víťaz:")
    for vitaz in vitazi:
        meno, krajina = vitaz
        print(f"{meno} ({krajina})")

vysledky, krajiny = spracuj_vysledky("skok_do_dialky.txt")
vypis_krajiny(vysledky, krajiny)
vypis_pocet_sutaziacich(vysledky)
vypis_vitazov(vysledky)


#ciarovekody
x = 10
y = 10
hrubka = random.randint(0, 9)
cislo = hrubka

root = Tk()
canvas = Canvas(root, width= 500, height = 400, bg = "white")
canvas.pack()
farby = ["red", "blue", "yellow", "brown", "magenta",  
        "lime", "black", "cyan", "orange", "purple", "pink", "white"]
#canvas.create_rectangle(x, y, x + 80, y + 80, fill = "black", outline = "" )
hrubka = random.randint(1, 9)
#canvas.create_rectangle(x, y, x + 5, y + 80, fill = "black", outline = "" )


for i in range(8):
    hrubka = random.randint(1, 9)
    x += 10
    canvas.create_rectangle(x, y, x + 10, y + 60, fill = "black", outline = "" )
    canvas.create_text(x, y + 70,  text = hrubka, fill = "black", font = ("Arial 10"))
    canvas.create_rectangle(x, y, x + hrubka, y + 60, fill = "white", outline = "")
canvas.create_rectangle(x + hrubka, y, x + 10, y + 80, fill = "black", outline = "" )

#vela kodov naraz
file = open("ciarove_kody.txt", "r")
def groupcodes():
    global x, y, hrubka
    for i in range(3):
        kody = file.readline()
        canvas.create_rectangle(x, y, x + 5, y + 80, fill = "black", outline = "" )
        for j in range (8):
            hrubka = int(kody[j])
            x += 10
            canvas.create_rectangle(x, y, x + 10, y + 60, fill = "black", outline = "" )
            canvas.create_text(x, y + 70,  text = hrubka, fill = "black", font = ("Arial 10"))
            canvas.create_rectangle(x, y, x + hrubka, y + 60, fill = "white", outline = "")
        canvas.create_rectangle(x + 10, y, x + 15, y + 80, fill = "black", outline = "" )
        x += 80
for i in range(3):
    groupcodes()
    y += 120
    x = 10


#4
file = open("hlasovanie1.txt", "r")
pocetsms = len(file.readlines())
print("Pocet zaslanych sms:", pocetsms)

file1 = open("5220.txt", "w+")
for i in range(len(file.readlines())):
    if file[i] == 5220:
        print(file[i])
    else:
        pass

#5
root = Tk()
canvas = Canvas(root, width= 650, height = 400, bg = "white")
canvas.pack()

file = open("sr.txt", "r")
file = [i.strip().split() for i in file.readlines()]
for i in file:
    #a = file.readline(i)
    x = int(i[0])
    y = int(i[1])
    canvas.create_rectangle(x, y, x, y)

file1 = open("sneh.txt", "r")
file1 = [j.strip().split() for j in file1.readlines()]
def keypress(event):
    key = event.char
if root.bind("<Key>", keypress):
    for j in file1:
        x1 = int(j[0])
        y1 = int(j[1])
        canvas.create_oval(x1, y1, x1, y1, width = 5)
        print(*j)
root.mainloop()

#7
with open("hada.txt", "r") as hada:
    pocethier = sum(1 for line in open("hada.txt"))
    print("Pocet hier:", pocethier)
    najdlhsia_hra = ""
    for line in hada.readlines():
        for hra in line.split():
            if len(hra) > len(najdlhsia_hra):
                najdlhsia_hra = hra
    print("Najdlhsia hra:", len(najdlhsia_hra))
    
    
def compress_game(game):
    compressed_game = ""
    current_direction = ""
    current_count = 0
    for move in game:
        if move == current_direction:
            current_count += 1
        else:
            if current_direction:
                compressed_game += f"{current_direction} {current_count} "
            current_direction = move
            current_count = 1
    compressed_game += f"{current_direction} {current_count}"
    return compressed_game

def compress_games(file_path):
    compressed_file_path = "compressed_" + file_path
    with open(file_path, 'r') as file:
        lines = file.readlines()
        with open(compressed_file_path, 'w') as compressed_file:
            for line in lines:
                game = line.strip()
                compressed_game = compress_game(game)
                compressed_file.write(compressed_game + "\n")

file_hada = 'hada.txt'



# Vytvoríme komprimovanú kópiu súboru
compress_games(file_hada)
print("Súbor bol úspešne skomprimovaný.")

    


#8
teplist = []
stanicelist = []
with open("meteo_stanice.txt", "r") as merania:
    for line in merania:
        udaje = line.split()
        #najvteplota = ""
        teploty = udaje[3]
        teplist.append(teploty)
        stanice = udaje[0]
        stanicelist.append(stanice)
    print(*stanicelist)
with open("meteo_stanice.txt", "r") as merania:
    lines=merania.readlines()
    pocet_merani = len(lines)
    print("Pocet merani:", pocet_merani)
    #print(teplist)
    teplist = [i.replace("+", "") for i in teplist]
    print(*teplist)
    najvteplota = max(teplist)
    najvstanica = []
    for i in range(len(teplist)):
        if teplist[i] == najvteplota:
            najvstanica.append(stanicelist[i])
    print(*najvstanica)
    #chyba kod stanice    
    print("Najvyssia teplota bola", najvteplota, "stupnov")
    teplist = [float(i) for i in teplist]
    #print(teplist)
    priemer = sum(teplist)/len(teplist)
    priemer = round(priemer, 2)
    najmteplota = (min(teplist))
    print("Najnizsia teplota bola ", najmteplota, "stupnov")
    print("Priemerna teplota bola ", priemer, "stupnov",)   


#9
pocetnie = 0
hodlist = []
nielist = []
with open("spokojnost_1.txt", "r") as spoko:
    for line in spoko:
        anonie = line.split()
        odpoved = anonie[1]
        if odpoved == "nie":
            pocetnie += 1
            nielist.append(anonie[0][:2])
        hodlist.append(anonie[0][:2])
    print("Pocet negativnych vyjadreni:", pocetnie)
    for i in range (0, len(nielist)):
        nielist[i] = int(nielist[i])
    print(nielist)
    def najnespoko(hodlist):
        return max(set(hodlist), key = hodlist.count)
    print("Hodina kedy bolo najviac nespokojnych zakaznikov:", najnespoko(hodlist))
    #print(Counter(nielist))


root = Tk()
canvas = Canvas(root, width= 480, height = 520, bg = "white")
canvas.pack()
pocetlist = []
x = 10
y = 500
hod = 0 
for i in range(24):
    canvas.create_rectangle(x, y, x + 20, y + 1)
    canvas.create_text(x, y + 10,  text = ("%02d" % (hod, )), fill = "red", font = ("Arial 10"))
    hod += 1
    x += 20

#for i in Counter(nielist):
    #for j in i:
        #pocetlist.append(i[1])
for i in range (0, len(nielist)):
    x = 0
    y = 490
    canvas.create_rectangle(x + ((nielist[i])*20) , y + 10, x + (nielist[i])*20 + 20, y - 20, fill = "red")
    
    
print(pocetlist)
root.mainloop()

import sys
import tkinter
from collections import defaultdict
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 480, height = 520)
canvas.pack()

spokojnost = [i.strip().split() for i in open("spokojnost_1.txt", 'r').readlines()]
casy = defaultdict(lambda: 0)
nie = 0
for cas, vyjadrenie in spokojnost:
    hodina = int(cas[:2])
    if (vyjadrenie == "nie"):
        casy[hodina] += 1
        nie += 1
print("Počet negatívnych vyjadrení:", nie)
x = 0
for i in range(24):
    canvas.create_line(x, 500, x + 15, 500)
    t = '0' + str(i + 1) if (i < 9) else i + 1
    canvas.create_text(x + 7.5, 510, text = t, fill = 'red')
    canvas.create_rectangle(x, 500, x + 15, 500 - (casy[i + 1] * 50), fill = 'red')
    x += 17
root.mainloop()

#10
import sys
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

vyraz = input()[:-1]
# napr: (a+b)-((a-b)*2)
dlzka = len(vyraz)
lave, prave = 0, 0
ok = 1
stak = [] # zasobnik na ukladanie farieb pravych zatvoriek
farby = ['red', 'green', 'blue', 'orange', 'yellow', 'magenta', 'brown']
f = 0
ofarbenie = ['black'] * dlzka
for i, clen in enumerate(vyraz):
    if (clen == '('):
        lave += 1
        ofarbenie[i] = farby[f]
        stak.append(f)
        f += 1
    elif (clen == ')'):
        prave += 1
        if (prave > lave):
            ok = 0
            break
        ofarbenie[i] = farby[stak[-1]]
        stak.pop()
ok &= (lave == prave) # Je rovnaky pocet pravych aj lavych?
if (not ok):
    canvas.create_text(200, 200, text = "Uzátvorkovanie nie je správne")
else:
    for i, clen in enumerate(vyraz):
        canvas.create_text((i * 10) + 200, 200, text = clen, fill = ofarbenie[i])
    canvas.create_text(280, 250, text = "Uzátvorkovanie je správne")
root.mainloop()



#11
vstup = input("Napis vetu: ")
def veta(lst, vstup):
    n = len(vstup)
    vystup = ""
    for i in range(n):
        if (vstup[i] == " "):
            vystup += "0"
            vystup += " "
        else:
            position = ord(vstup[i]) - ord("A")
            vystup += lst[position]
            vystup += " "
    return vystup

lst = ["1", '11', "111",
        "2", "22", "222",
        "3", "33", "333",
        "4", "44", "444",
        "5", "55", "555",
        "6", "66", "666",
        "7", "77", "777",
        "8", "88", "888",
        "9", "99"
        ]
veta1 = veta(lst, vstup)
print(veta1)
veta1 = veta1.replace(" ", "")

def najcislo(veta1):
    counter = Counter(veta1)
    # Nájsť číslo s najväčším počtom výskytov
    
    most_common_number = max(counter, key=counter.get)
    
    return most_common_number
print(najcislo(veta1))


#12
hadanecisla = input("Zadaj cisla: ")
zoznamcisel = hadanecisla.split
#for i in range(6):
    #tip = int(input("Zadaj cislo: "))
    #hadanecisla.append(tip)
vysledok = []
uhadcisla = []
pocetuhadcisel = 0
for i in range(6):
    zrebcislo = random.randint(1, 49)
    print("Vyzrebovane cislo je: ", zrebcislo)
    vysledok.append(zrebcislo)
    for j in hadanecisla:
        if zrebcislo in hadanecisla:
            uhadcisla.append(zrebcislo)
            pocetuhadcisel += 1
            break
print("Tvoje tipy:", *hadanecisla)
print("Vyzrebovane cisla:", *vysledok)
print("Uhadnute cisla:", *uhadcisla)
if pocetuhadcisel == 0:
    print("Nic si neuhadol, prerobil si")
else:
    print("Pocet cisel ktore si uhadol:", pocetuhadcisel)


def read_user_input():
    # Prečíta vstup od používateľa a vráti zoznam čísel
    user_input = input("Zadajte svoje tipy (6 čísel oddelených medzerami): ")
    numbers = user_input.split()
    numbers = [int(num) for num in numbers]
    return numbers

def generate_lottery_numbers():
    # Generuje a vráti zoznam 6 vyžrebovaných čísel
    import random
    lottery_numbers = random.sample(range(1, 50), 6)
    return lottery_numbers

def compare_numbers(user_numbers, lottery_numbers):
    # Porovná tipy používateľa so žrebovanými číslami
    correct_numbers = set(user_numbers).intersection(lottery_numbers)
    return correct_numbers

def count_matched_numbers(tips_file, lottery_numbers):
    # Porovná vyžrebované čísla so všetkými tipmi účastníkov lotérie
    counts = [0, 0, 0, 0, 0, 0]  # počet účastníkov s 0, 1, 2, 3, 5 a 6 správnymi číslami
    with open("12 loteria1.txt", 'r') as file:
        for line in file:
            numbers = [int(num) for num in line.split()]
            correct_numbers = set(numbers).intersection(lottery_numbers)
            count = len(correct_numbers)
            counts[count] += 1
    return counts

def print_results(correct_numbers_user, counts):
    # Vypíše uhádnuté čísla používateľa a počet uhádnutých čísel
    print("Vaše uhádnuté čísla:", correct_numbers_user)
    print("Počet uhádnutých čísel:", len(correct_numbers_user))

    # Vypíše počet účastníkov, ktorí správne tipovali rôzny počet čísel
    print("Počet účastníkov, ktorí správne tipovali:")
    print("Práve jedno číslo:", counts[1])
    print("Práve dve čísla:", counts[2])
    print("Práve tri čísla:", counts[3])
    print("Práve päť čísel:", counts[5])
    print("Práve šesť čísel:", counts[6])

# Hlavná časť programu
user_numbers = read_user_input()
lottery_numbers = generate_lottery_numbers()
correct_numbers_user = compare_numbers(user_numbers, lottery_numbers)
counts = count_matched_numbers("12 loteria1.txt", lottery_numbers)
print_results(correct_numbers_user, counts)


#13
root = Tk()
canvas = Canvas(root, width= 600, height = 300, bg = "white")
canvas.pack()

x = 10
y = 150
x1 = []
y1 = []
with open("zastavba_na_ulici.txt", "r") as file:
    for line in file:
        suradky = line.split()
        x1.append(suradky[0])
        y1.append(suradky[1])
    x1 = [int(i) for i in x1]
    y1 = [int(i) for i in y1]
    for i in range(len(x1)):
        canvas.create_rectangle(x, y, x + x1[i], y  - y1[i], fill = "grey")
        if y1[i] == 0:
            canvas.create_rectangle(x, y, x + x1[i], y  - y1[i], fill = "lime", width = 8, outline = "")
        x += x1[i]
        vstup = Entry(root)
    canvas.create_window(300, 270, window = vstup)
    def redlines():
        global x, y
        y2 = int(vstup.get())
        for i in range(len(y1)):
            if y2 < y1[i] - y1[i - 1]:
                canvas.create_rectangle(x, y, x + x1[i], y + (y1[i] - y1[i+1]), 
                                        fill = "red", width = 8, outline = "")
            x += x1[i]
    Vykresli = Button(root, text = "Vykresli", command = redlines)
    Vykresli.pack()
print(x1)
print(y1)
root.mainloop()



#15

import random

def reverse_word(word):
    return word[::-1]

def transform_text(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Zmena poradia riadkov
    random.shuffle(lines)

    transformed_lines = []
    for line in lines:
        # Zmena poradia slov v riadku
        words = line.strip().split(' ')
        random.shuffle(words)

        transformed_words = []
        for word in words:
            # Otočenie slova
            if random.choice([True, False]):
                word = reverse_word(word)
            transformed_words.append(word)

        transformed_line = ' '.join(transformed_words)
        transformed_lines.append(transformed_line)

    with open('virus_vystup.txt', 'w') as output_file:
        output_file.write('\n'.join(transformed_lines))

    print('Text bol úspešne transformovaný.')

# Testovanie
transform_text('virus.txt')

#16

with open("cesty.txt", "r") as cesty:
    distlist = [[int(cislo) for cislo in line.split()]for line in cesty]
print(distlist)
dlzkalst = []
for i in distlist:
    dlzka1 = sum(i)
    dlzkalst.append(dlzka1)
dlzka = sum(dlzkalst)
mesto = []
print("Celkova dlzka cestnej siete je", dlzka, "kilometrov")

mesto1 = distlist[0]
mesto2 = distlist[1]
mesto3 = distlist[2]
mesto4 = distlist[3]
mesto5 = distlist[4]
#mesto[1][4] = mesto[4][1]
mesto1[3] = mesto4[0]


def find_most_distant_cities(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    max_distance = 0
    cities = []

    for i in range(len(lines)):
        distances = list(map(int, lines[i].strip().split()))
        for j in range(i+1, len(distances)):
            if distances[j] > max_distance:
                max_distance = distances[j]
                cities = [i+1, j+1]
            elif distances[j] == max_distance:
                cities.append(j+1)

    return cities

# Testovanie
most_distant_cities = find_most_distant_cities('cesty.txt')
print("Najviac vzdialené mestá s existujúcou spojnicou:")
for city in most_distant_cities:
    print(city, end=' ')
print()


#17
def count_meals(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    total_meals = len(lines)
    color_counts = {'z': 0, 'c': 0, 'm': 0, 'h': 0}
    less_than_20 = []

    for line in lines:
        student_id, color = line.strip().split()
        color_counts[color] += 1

    for color, count in color_counts.items():
        if count < 20:
            less_than_20.extend([line.split()[0] for line in lines if line.split()[1] == color])

    return total_meals, color_counts, less_than_20

# Testovanie
total_meals, color_counts, less_than_20 = count_meals('17 jedla.txt')

print(f"Celkový počet jedál na nasledujúci deň: {total_meals}")
print("Počty jednotlivých jedál:")
for color, count in color_counts.items():
    print(f"{color}: {count}")
print("Čísla stravníkov s jedlami pre menej ako 20 ľudí:")
for student_id in less_than_20:
    print(student_id)



#18

# Načítanie frekvenčnej tabuľky znakov
with open("18 frekv.txt", "r") as file:
    frequency_table = {}
    for line in file:
        char, count = line.split()
        frequency_table[char] = int(count)

# Získanie frekvenčnej tabuľky zašifrovaného textu
with open("18 sifro.txt", "r") as file:
    encrypted_text = file.read()
    encrypted_frequency_table = {}
    for char in encrypted_text:
        if char in encrypted_frequency_table:
            encrypted_frequency_table[char] += 1
        else:
            encrypted_frequency_table[char] = 1

# Vytvorenie mapovania pre dešifrovanie
decryption_mapping = {}
for encrypted_char, encrypted_count in encrypted_frequency_table.items():
    decrypted_char = None
    for decrypted_char, decrypted_count in frequency_table.items():
        if encrypted_count == decrypted_count:
            decryption_mapping[encrypted_char] = decrypted_char
            break

# Rozšifrovanie textu
decrypted_text = ""
for char in encrypted_text:
    decrypted_text += decryption_mapping.get(char, char)

# Výpis rozšifrovaného textu
print("Rozšifrovaný text:")
print(decrypted_text)

# Uloženie kľúča do súboru kluc.txt
with open("kluc.txt", "w") as file:
    for encrypted_char, decrypted_char in decryption_mapping.items():
        file.write(f"{encrypted_char} {decrypted_char}\n")


#20

with open("20 cisla.txt", "r") as file:
    for line in file:
        cisla = line.strip().split()
        cislo1 = cisla[0]
        cislo2 = cisla[1]
        def konverzia(cislo1):
            if cislo2 == "2":
                cislo3 = int(cislo1,2)
                print(f"(",cislo1,")",cislo2,"=",cislo3)
            if cislo2 == "8":
                cislo3 = int(cislo1,8)
                print(f"(",cislo1,")", cislo2, "=", cislo3)
            if cislo2 == "16":
                cislo3 = int(cislo1,16)
                print(f"(",cislo1,")", cislo2, "=", cislo3)
            
        print((konverzia(cislo1)))

"""
#21
def check_visited_stations(stations_visited, all_stations):
    return set(stations_visited) == set(all_stations)

def get_winner(start_numbers, times, stations_visited, all_stations):
    for i in range(len(start_numbers)):
        if check_visited_stations(stations_visited[i], all_stations):
            return start_numbers[i]
    return None

def print_results(start_numbers, times, stations_visited):
    print("Výsledková listina:")
    for i in range(len(start_numbers)):
        print(f"Pretekár č. {start_numbers[i]} - Čas: {times[i]} - Navštívené stanovištia: {stations_visited[i]}")

# Načítanie dát zo súborov
with open("21 stanovistia.txt", "r") as f:
    all_stations = [line.strip() for line in f.readlines()]

with open("21 pretekari.txt", "r") as f:
    start_numbers = []
    times = []
    stations_visited = []
    for line in f.readlines():
        data = line.strip().split()
        start_numbers.append(int(data[0]))
        times.append(data[1])
        stations_visited.append(data[2:])

# Kontrola navštívených stanovíšť pre každého pretekára
for i in range(len(start_numbers)):
    if check_visited_stations(stations_visited[i], all_stations):
        print(f"Pretekár č. {start_numbers[i]} navštívil všetky stanovištia.")
    else:
        print(f"Pretekár č. {start_numbers[i]} nenavštívil všetky stanovištia.")

# Vyhodnotenie víťaza
winner = get_winner(start_numbers, times, stations_visited, all_stations)
if winner is not None:
    print(f"Víťaz: Pretekár č. {winner}")
else:
    print("Žiadny pretekár nenavštívil všetky stanovištia.")

# Výpis výsledkovej listiny
print_results(start_numbers, times, stations_visited)

"""


#24
with open("24 mapa.txt" , "r") as mapa:
    maplst = []
    nmaplst = []
    for line in mapa:
        print(line.rstrip())
        maplst.append(line)
    #for i in range(0, len(maplst)):
        #maplst[i] = int(maplst[i])
        #for i in line:
            #res = line(map(int, str(i)))
    for word in maplst:
        word = word.split(" ")
        nmaplst.extend(word)
    for i in range(0, len(nmaplst)):
        nmaplst[i] = int(nmaplst[i])
    ostrovy = 0
    #for i in range(0, len(nmaplst)):
        #if nmaplst[i] > 0:
            #ostrovy += 1
maxostrov = (max(nmaplst))

#print(maplst)
print(nmaplst)
print("Pocet ostrovov je", ostrovy)
Counter(nmaplst)
a = 1
for i in range(15):
    for i in range(0, len(nmaplst)):
        nmaplst.count(a)
    if nmaplst.count(a) > 1:
        ostrovy += 1
    a += 1
#print("Najvacsia rozloha ostrova je", maxostrov)

root = Tk()
canvas = Canvas(root, width= 500, height = 500, bg = "blue")
canvas.pack()
x = 10
y = 10
for i in range (0, len(nmaplst)):
    canvas.create_rectangle(x, y, x + (nmaplst[i]*3), y + (nmaplst[i]*3), fill = "green")
    x += 40
    if x > 400:
        x = 10
        y += 50
root.mainloop()

#25
randkod = random.randint(10000000, 99999999)
print(randkod)
with open("25 kod_a.txt", 'r') as kody:
    udaje = kody.readlines()
    print(udaje)
    for i in range(0, len(udaje)):
        udaje[i] = int(udaje[i])
    print(udaje)
    
    for i in range(len(udaje)):
        x2 = udaje[i]
        x = udaje[i] // 10
        #print(x)
        y = 0 
        xlist = [int(n) for n in str(x)]
        #konkod = ((int(str(x)[:4])) % 2) + ((int(str(x)[len(x)//2-1: len(x)//2+1])))
        #print(xlist)
        xlist2 = []
        for i in (xlist[0:4]):
            xlist2.append(i)
        xlist2 = [str(n) for n in xlist2]
        xx = int("".join(xlist2))
        #print(xx)
        xlist3 = []
        for i in (xlist[2:6]):
            xlist3.append(i)
        xlist3 = [str(n) for n in xlist3]
        xy = int("".join(xlist3))
        #print(xy)
        xlist4 = []
        for i in (xlist[4:8]):
            xlist4.append(i)
        xlist4 = [str(n) for n in xlist4]
        xz = int("".join(xlist4))
        #print(xz)
        konkod = [(xx % 2), (xy % 2) , (xz % 2)]

        konkod[0], konkod[2] = konkod[2], konkod[0]

        konkod = [str(n) for n in konkod]
        konkod2 = int("".join(konkod))

        konkod3 = int(str(konkod2),2)
        print(konkod3)
        xlist.append(konkod3)

        xlist = [str(n) for n in xlist]
        finalkod = int("".join(xlist))
        print(finalkod)
        if finalkod == x2:
            print("dobry kod")
        else:
            print("zly kod")



#27
root = Tk()
canvas = Canvas(root, width= 800, height = 500, bg = "white")
canvas.pack()
x = 10
y = 10
furik = input("Zadaj pocet furikov:")
totaljamy = 0
totalkopec = 0
pocetzarovno = 0
for i in range(10):
    for j in range(10):
        lvl = random.randint(-1, 1)
    
        canvas.create_rectangle(x, y, x + 40, y + 40, fill = "green")
        canvas.create_text(x + 10, y + 20,  text = lvl, fill = "black", font = ("Arial 10"))
        #if lvl < 0:
            #canvas.create_text(x + 30, y + 20,  text = furik, fill = "black", font = ("Arial 10"))
        if lvl > 0:
            totalkopec += lvl
        if lvl < 0:
            totaljamy += lvl
        x += 40
    x = 10
    y += 40
print(totalkopec)
print(abs(totaljamy))
text1 = "Pocet kopcov:"
text2 = "Pocet jam:"
with open("27 kopcejamy.txt", "w") as file:
    file.write(text1 + " " + str(totalkopec) + "\n")
    file.write(text2 + " " + str(abs(totaljamy)))
root.mainloop()

#28
import sys
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 800, height = 500)
canvas.pack()

tajnicka = [i.strip().split() for i in open("28 krizovka1.txt", 'r').readlines()]
n = len(tajnicka)

def kresli():
    # Prazdna
    x, y = 250, 100
    for poz, slovo in tajnicka:
        # Najprv tajnicka, potom ostatne pismena
        poz = int(poz) - 1
        canvas.create_rectangle(x, y, x + 25, y + 25, fill = 'gray')
        _x, _y = x - 25, y
        for i in range(poz - 1, -1, -1): # Dozadu
            canvas.create_rectangle(_x, _y, _x + 25, _y + 25)
            _x -= 25
        _x, _y = x + 25, y
        for i in range(poz + 1, len(slovo)): # Dopredu
            canvas.create_rectangle(_x, _y, _x + 25, _y + 25)
            _x += 25
        y += 25

    # Vyriesena
    x, y = 500, 100
    for poz, slovo in tajnicka:
        # Najprv tajnicka, potom ostatne pismena
        poz = int(poz) - 1
        canvas.create_rectangle(x, y, x + 25, y + 25, fill = 'gray')
        canvas.create_text(x + 12.5, y + 12.5, text = slovo[poz])
        _x, _y = x - 25, y
        for i in range(poz - 1, -1, -1): # Dozadu
            canvas.create_rectangle(_x, _y, _x + 25, _y + 25)
            canvas.create_text(_x + 12.5, _y + 12.5, text = slovo[i])
            _x -= 25
        _x, _y = x + 25, y
        for i in range(poz + 1, len(slovo)): # Dopredu
            canvas.create_rectangle(_x, _y, _x + 25, _y + 25)
            canvas.create_text(_x + 12.5, _y + 12.5, text = slovo[i])
            _x += 25
        y += 25

kresli()

root.mainloop()



#29
#ptext = (open("29 poprehadzovany_text1_vstup.txt", "r").read())
with open("29 poprehadzovany_text1_vstup.txt", "r") as ptext:
    udaje = ptext.readlines()
    ptextlst = []
    for line in udaje:
        for word in line.split():
            ptextlst.append(word)
    print(ptextlst)
    for word in ptextlst:
        lstword = list(word[1:-1])
        if len(lstword) > 2:
            random.shuffle(lstword)
        else:
            pass
        randword = word[0] + "".join(lstword) + word[-1]
        print(randword, end = " ")

#29
with open("30 kompresia_obrazka1.txt", "r") as obraz:
    rozmery = obraz.readline().strip("\n")
    print(rozmery)

"""







