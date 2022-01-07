import random
from colorama import init, Fore, Back, Style
import sys
import time
# karty przeciwnika
Karta1p = []
Karta2p = []
Karta3p = []
Karta4p = []
Karta5p = []
# twoje karty
Karta1 = []
Karta2 = []
Karta3 = []
Karta4 = []
Karta5 = []
Karta6 = []

print("Twoje karty:")

# losowe numerki!!! kto ich nie kocha?
owo1 = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
owo3 = random.randrange(1 , 5)
owo4 = random.randrange(1 , 13)
owo5 = random.randrange(1 , 5)
owo6 = random.randrange(1 , 13)
owo7 = random.randrange(1 , 5)
owo8 = random.randrange(1 , 13)
owo9 = random.randrange(1 , 5)
owo10 = random.randrange(1 , 13)
owo11 = random.randrange(1 , 5)
owo12 = random.randrange(1 , 13)

owo1p = random.randrange(1 , 5)
owo2p = random.randrange(1 , 13)
owo3p = random.randrange(1 , 5)
owo4p = random.randrange(1 , 13)
owo5p = random.randrange(1 , 5)
owo6p = random.randrange(1 , 13)
owo7p = random.randrange(1 , 5)
owo8p = random.randrange(1 , 13)
owo9p = random.randrange(1 , 5)
owo10p = random.randrange(1 , 13)
owo11p = random.randrange(1 , 5)
owo12p = random.randrange(1 , 13)
# funkcja bym nie musial kopiowac wszystkiego 10 razy
def owos(a, b, c):

    if b == 1:
        a.insert(1, "Pik")
    elif b == 2:
        a.insert(1, "Kier")
    elif b == 3:
        a.insert(1, "Trefl")
    elif b == 4:
        a.insert(1, "Karo")
    if c == 1:
        a.insert(2, "AS")
    elif c == 2:
        a.insert(2, "2")
    elif c == 3:
        a.insert(2, "3")
    elif c == 4:
        a.insert(2, "4")
    elif c == 5:
        a.insert(2, "5")
    elif c == 6:
        a.insert(2, "6")
    elif c == 7:
        a.insert(2, "7")
    elif c == 8:
        a.insert(2, "8")
    elif c == 9:
        a.insert(2, "9")
    elif c == 10:
        a.insert(2, "10")
    elif c == 11:
        a.insert(2, "Walet")
    elif c == 12:
        a.insert(2, "Krolowa")
    elif c == 13:
        a.insert(2, "Krol")

# wybieranie twoich kart z wylosowanych numerow
q = owos(Karta1, owo1, owo2)
qq = owos(Karta2, owo3, owo4)
qqq = owos(Karta3, owo5, owo6)
qqqq = owos(Karta4, owo7, owo8)
qqqqq = owos(Karta5, owo9, owo10)
qqqqqq = owos(Karta6, owo11, owo12)



# zamienianie kart na str
time.sleep(0.5)
string1=""
for i in Karta1:
   string1=string1+i
string2=""
for i in Karta1:
   string2=string2+i+" "
time.sleep(0.5)
print(string2)
for i in Karta2:
   string1=string1+i
string3=""
for i in Karta2:
   string3=string3+i+" "
time.sleep(0.5)
print(string3)
for i in Karta3:
   string1=string1+i
string4=""
for i in Karta3:
   string4=string4+i+" "
time.sleep(0.5)
print(string4)
for i in Karta4:
   string1=string1+i
string5=""
for i in Karta4:
   string5=string5+i+" "
time.sleep(0.5)
print(string5)
for i in Karta5:
   string1=string1+i
string6=""
for i in Karta5:
   string6=string6+i+" "
time.sleep(0.5)
print(string6)
time.sleep(0.5)
for i in Karta6:
   string1=string1+i
string7=""
for i in Karta6:
   string7=string7+i+" "



# system zmiany karty ktory nie wiem jak dziala ale dziala
time.sleep(1.5)
zmiana = str(input("Czy chcesz zamienic jedna ze swoich kart? Y/N "))
if zmiana == "Y":
    wybierz = int(input("Wybierz numer karty ktora chcez zamienic (nr = pozycja karty) "))





    if wybierz == 1:
        oso = "czy chcesz zamienic karte " + string2 + "na losowa karte? Y/N"
        potw = str(input(oso))
        if potw == "Y":
            Karta1.clear()
            Karta1.insert(1,string7)
            print("Wylosowales karte", string7)


    elif wybierz == 2:
        oso = "czy chcesz zamienic karte " + string3 + "na losowa karte? Y/N"
        potw = str(input(oso))
        if potw == "Y":
            Karta2.clear()
            Karta2.insert(1,string7)
            print("Wylosowales karte", string7)
        else:
            print("Prosimy wybrac")
            print("Tak - Y")
            print("Nie - N")


    elif wybierz == 3:
        oso = "czy chcesz zamienic karte " + string4 + "na losowa karte? Y/N"
        potw = str(input(oso))
        if potw == "Y" or "y":
            Karta3.clear()
            Karta3.insert(1,string7)
            print("Wylosowales karte", string7)
        else:
            print("Prosimy wybrac")
            print("Tak - Y")
            print("Nie - N")


    elif wybierz == 4:
        oso = "czy chcesz zamienic karte " + string5 + "na losowa karte? Y/N"
        potw = str(input(oso))
        if potw == "Y" or "y":
            Karta4.clear()
            Karta4.insert(1,string7)
            print("Wylosowales karte", string7)
        else:
            print("Prosimy wybrac")
            print("Tak - Y")
            print("Nie - N")


    elif wybierz == 5:
        oso = "czy chcesz zamienic karte " + string5 + "na losowa karte? Y/N"
        potw = str(input(oso))
        if potw == "Y" or "y":
            Karta5.clear()
            Karta5.insert(1,string7)
            print("Wylosowales karte", string7)
        else:
            print("Prosimy wybrac")
            print("Tak - Y")
            print("Nie - N")
    else:

        sys.exit(0)
        print("error")

# tu chyba znowu zmiana kart na str ale nie jestem pewny
time.sleep(0.5)
string1=""
for i in Karta1:
   string1=string1+i
string2=""
for i in Karta1:
   string2=string2+i+" "
time.sleep(0.5)
print(string2)
for i in Karta2:
   string1=string1+i
string3=""
for i in Karta2:
   string3=string3+i+" "
time.sleep(0.5)
print(string3)
for i in Karta3:
   string1=string1+i
string4=""
for i in Karta3:
   string4=string4+i+" "
time.sleep(0.5)
print(string4)
for i in Karta4:
   string1=string1+i
string5=""
for i in Karta4:
   string5=string5+i+" "
time.sleep(0.5)
print(string5)
for i in Karta5:
   string1=string1+i
string6=""
for i in Karta5:
   string6=string6+i+" "
time.sleep(0.5)
print(string6)
print("Przeciwnik losuje karty")
time.sleep(1)






# losowanie kart przeciwnika
qp = owos(Karta1p, owo1p, owo2p)
qqp = owos(Karta2p, owo3p, owo4p)
qqqp = owos(Karta3p, owo5p, owo6p)
qqqqp = owos(Karta4p, owo7p, owo8p)
qqqqqp = owos(Karta5p, owo9p, owo10p)




all = Karta1 + Karta2 + Karta3 + Karta4 + Karta5
# zmiana kart przeciwnika ktora nic nie robi
zmiana = random.randrange(1 , 3)
if zmiana == 1:
    print("przeciwnik zmienia karte (tak na serio nic nie zmienia)")

# na to nie warto zwracac uwagi 
Karta1.pop(1)
Karta2.pop(1)
Karta3.pop(1)
Karta4.pop(1)
Karta5.pop(1)
print(Karta1)

print("Pokazywanie kart")
print("Uklad")


print(all)
print (all.count())