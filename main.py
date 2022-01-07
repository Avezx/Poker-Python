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
# karty do gry
Karta1 = []
Karta2 = []
Karta3 = []
Karta4 = []
Karta5 = []
# karta do zmiany
Karta6 = []

print("Twoje karty:")


# wybieranie pierwszej karty z wylosowanych numerow
owo = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo == 1:
    Karta1.insert(1, "Pik")
elif owo == 2:
    Karta1.insert(1, "Kier")
elif owo == 3:
    Karta1.insert(1, "Trefl")
elif owo == 4:
    Karta1.insert(1, "Karo")
if owo2 == 1:
    Karta1.insert(2, "AS")
elif owo2 == 2:
    Karta1.insert(2, "2")
elif owo2 == 3:
    Karta1.insert(2, "3")
elif owo2 == 4:
    Karta1.insert(2, "4")
elif owo2 == 5:
    Karta1.insert(2, "5")
elif owo2 == 6:
    Karta1.insert(2, "6")
elif owo2 == 7:
    Karta1.insert(2, "7")
elif owo2 == 8:
    Karta1.insert(2, "8")
elif owo2 == 9:
    Karta1.insert(2, "9")
elif owo2 == 10:
    Karta1.insert(2, "10")
elif owo2 == 11:
    Karta1.insert(2, "Walet")
elif owo2 == 12:
    Karta1.insert(2, "Krolowa")
elif owo2 == 13:
    Karta1.insert(2, "Krol")










# wybieranie drugiej karty z wylosowanych numerow
owo3 = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo3 == 1:
    Karta2.insert(1, "Pik")
elif owo3 == 2:
    Karta2.insert(1, "Kier")
elif owo3 == 3:
    Karta2.insert(1, "Trefl")
elif owo3 == 4:
    Karta2.insert(1, "Karo")
if owo2 == 1:
    Karta2.insert(2, "AS")
elif owo2 == 2:
    Karta2.insert(2, "2")
elif owo2 == 3:
    Karta2.insert(2, "3")
elif owo2 == 4:
    Karta2.insert(2, "4")
elif owo2 == 5:
    Karta2.insert(2, "5")
elif owo2 == 6:
    Karta2.insert(2, "6")
elif owo2 == 7:
    Karta2.insert(2, "7")
elif owo2 == 8:
    Karta2.insert(2, "8")
elif owo2 == 9:
    Karta2.insert(2, "9")
elif owo2 == 10:
    Karta2.insert(2, "10")
elif owo2 == 11:
    Karta2.insert(2, "Walet")
elif owo2 == 12:
    Karta2.insert(2, "Krolowa")
elif owo2 == 13:
    Karta2.insert(2, "Krol")










# wybieranie trzeciej karty z wylosowanych numerow
owo4 = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo4 == 1:
    Karta3.insert(1, "Pik")
elif owo4 == 2:
    Karta3.insert(1, "Kier")
elif owo4 == 3:
    Karta3.insert(1, "Trefl")
elif owo4 == 4:
    Karta3.insert(1, "Karo")
if owo2 == 1:
    Karta3.insert(2, "AS")
elif owo2 == 2:
    Karta3.insert(2, "2")
elif owo2 == 3:
    Karta3.insert(2, "3")
elif owo2 == 4:
    Karta3.insert(2, "4")
elif owo2 == 5:
    Karta3.insert(2, "5")
elif owo2 == 6:
    Karta3.insert(2, "6")
elif owo2 == 7:
    Karta3.insert(2, "7")
elif owo2 == 8:
    Karta3.insert(2, "8")
elif owo2 == 9:
    Karta3.insert(2, "9")
elif owo2 == 10:
    Karta3.insert(2, "10")
elif owo2 == 11:
    Karta3.insert(2, "Walet")
elif owo2 == 12:
    Karta3.insert(2, "Krolowa")
elif owo2 == 13:
    Karta3.insert(2, "Krol")










# wybieranie czwartej karty z wylosowanych numerow
owo5 = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo5 == 1:
    Karta4.insert(1, "Pik")
elif owo5 == 2:
    Karta4.insert(1, "Kier")
elif owo5 == 3:
    Karta4.insert(1, "Trefl")
elif owo5 == 4:
    Karta4.insert(1, "Karo")
if owo2 == 1:
    Karta4.insert(2, "AS")
elif owo2 == 2:
    Karta4.insert(2, "2")
elif owo2 == 3:
    Karta4.insert(2, "3")
elif owo2 == 4:
    Karta4.insert(2, "4")
elif owo2 == 5:
    Karta4.insert(2, "5")
elif owo2 == 6:
    Karta4.insert(2, "6")
elif owo2 == 7:
    Karta4.insert(2, "7")
elif owo2 == 8:
    Karta4.insert(2, "8")
elif owo2 == 9:
    Karta4.insert(2, "9")
elif owo2 == 10:
    Karta4.insert(2, "10")
elif owo2 == 11:
    Karta4.insert(2, "Walet")
elif owo2 == 12:
    Karta4.insert(2, "Krolowa")
elif owo2 == 13:
    Karta4.insert(2, "Krol")










# wybieranie piatej karty z wylosowanych numerow
owo6 = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo6 == 1:
    Karta5.insert(1, "Pik")
elif owo6 == 2:
    Karta5.insert(1, "Kier")
elif owo6 == 3:
    Karta5.insert(1, "Trefl")
elif owo6 == 4:
    Karta5.insert(1, "Karo")
if owo2 == 1:
    Karta5.insert(2, "AS")
elif owo2 == 2:
    Karta5.insert(2, "2")
elif owo2 == 3:
    Karta5.insert(2, "3")
elif owo2 == 4:
    Karta5.insert(2, "4")
elif owo2 == 5:
    Karta5.insert(2, "5")
elif owo2 == 6:
    Karta5.insert(2, "6")
elif owo2 == 7:
    Karta5.insert(2, "7")
elif owo2 == 8:
    Karta5.insert(2, "8")
elif owo2 == 9:
    Karta5.insert(2, "9")
elif owo2 == 10:
    Karta5.insert(2, "10")
elif owo2 == 11:
    Karta5.insert(2, "Walet")
elif owo2 == 12:
    Karta5.insert(2, "Krolowa")
elif owo2 == 13:
    Karta5.insert(2, "Krol")










# wybieranie dodatkowej karty z wylosowanych numerow
owo7 = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo7 == 1:
    Karta6.insert(1, "Pik")
elif owo7 == 2:
    Karta6.insert(1, "Kier")
elif owo7 == 3:
    Karta6.insert(1, "Trefl")
elif owo7 == 4:
    Karta6.insert(1, "Karo")
if owo2 == 1:
    Karta6.insert(2, "AS")
elif owo2 == 2:
    Karta6.insert(2, "2")
elif owo2 == 3:
    Karta6.insert(2, "3")
elif owo2 == 4:
    Karta6.insert(2, "4")
elif owo2 == 5:
    Karta6.insert(2, "5")
elif owo2 == 6:
    Karta6.insert(2, "6")
elif owo2 == 7:
    Karta6.insert(2, "7")
elif owo2 == 8:
    Karta6.insert(2, "8")
elif owo2 == 9:
    Karta6.insert(2, "9")
elif owo2 == 10:
    Karta6.insert(2, "10")
elif owo2 == 11:
    Karta6.insert(2, "Walet")
elif owo2 == 12:
    Karta6.insert(2, "Krolowa")
elif owo2 == 13:
    Karta6.insert(2, "Krol")



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







# wybieranie pierwszej karty z wylosowanych numerow
owo = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo == 1:
    Karta1p.insert(1, "Pik")
elif owo == 2:
    Karta1p.insert(1, "Kier")
elif owo == 3:
    Karta1p.insert(1, "Trefl")
elif owo == 4:
    Karta1p.insert(1, "Karo")
if owo2 == 1:
    Karta1p.insert(2, "AS")
elif owo2 == 2:
    Karta1p.insert(2, "2")
elif owo2 == 3:
    Karta1p.insert(2, "3")
elif owo2 == 4:
    Karta1p.insert(2, "4")
elif owo2 == 5:
    Karta1p.insert(2, "5")
elif owo2 == 6:
    Karta1p.insert(2, "6")
elif owo2 == 7:
    Karta1p.insert(2, "7")
elif owo2 == 8:
    Karta1p.insert(2, "8")
elif owo2 == 9:
    Karta1p.insert(2, "9")
elif owo2 == 10:
    Karta1p.insert(2, "10")
elif owo2 == 11:
    Karta1p.insert(2, "Walet")
elif owo2 == 12:
    Karta1p.insert(2, "Krolowa")
elif owo2 == 13:
    Karta1p.insert(2, "Krol")










# wybieranie drugiej karty z wylosowanych numerow
owo3 = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo3 == 1:
    Karta2p.insert(1, "Pik")
elif owo3 == 2:
    Karta2p.insert(1, "Kier")
elif owo3 == 3:
    Karta2p.insert(1, "Trefl")
elif owo3 == 4:
    Karta2p.insert(1, "Karo")
if owo2 == 1:
    Karta2p.insert(2, "AS")
elif owo2 == 2:
    Karta2p.insert(2, "2")
elif owo2 == 3:
    Karta2p.insert(2, "3")
elif owo2 == 4:
    Karta2p.insert(2, "4")
elif owo2 == 5:
    Karta2p.insert(2, "5")
elif owo2 == 6:
    Karta2p.insert(2, "6")
elif owo2 == 7:
    Karta2p.insert(2, "7")
elif owo2 == 8:
    Karta2p.insert(2, "8")
elif owo2 == 9:
    Karta2p.insert(2, "9")
elif owo2 == 10:
    Karta2p.insert(2, "10")
elif owo2 == 11:
    Karta2p.insert(2, "Walet")
elif owo2 == 12:
    Karta2p.insert(2, "Krolowa")
elif owo2 == 13:
    Karta2.insert(2, "Krol")










# wybieranie trzeciej karty z wylosowanych numerow
owo4 = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo4 == 1:
    Karta3p.insert(1, "Pik")
elif owo4 == 2:
    Karta3p.insert(1, "Kier")
elif owo4 == 3:
    Karta3p.insert(1, "Trefl")
elif owo4 == 4:
    Karta3p.insert(1, "Karo")
if owo2 == 1:
    Karta3p.insert(2, "AS")
elif owo2 == 2:
    Karta3p.insert(2, "2")
elif owo2 == 3:
    Karta3p.insert(2, "3")
elif owo2 == 4:
    Karta3p.insert(2, "4")
elif owo2 == 5:
    Karta3p.insert(2, "5")
elif owo2 == 6:
    Karta3p.insert(2, "6")
elif owo2 == 7:
    Karta3p.insert(2, "7")
elif owo2 == 8:
    Karta3p.insert(2, "8")
elif owo2 == 9:
    Karta3p.insert(2, "9")
elif owo2 == 10:
    Karta3p.insert(2, "10")
elif owo2 == 11:
    Karta3p.insert(2, "Walet")
elif owo2 == 12:
    Karta3p.insert(2, "Krolowa")
elif owo2 == 13:
    Karta3p.insert(2, "Krol")










# wybieranie czwartej karty z wylosowanych numerow
owo5 = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo5 == 1:
    Karta4p.insert(1, "Pik")
elif owo5 == 2:
    Karta4p.insert(1, "Kier")
elif owo5 == 3:
    Karta4p.insert(1, "Trefl")
elif owo5 == 4:
    Karta4p.insert(1, "Karo")
if owo2 == 1:
    Karta4p.insert(2, "AS")
elif owo2 == 2:
    Karta4p.insert(2, "2")
elif owo2 == 3:
    Karta4p.insert(2, "3")
elif owo2 == 4:
    Karta4p.insert(2, "4")
elif owo2 == 5:
    Karta4p.insert(2, "5")
elif owo2 == 6:
    Karta4p.insert(2, "6")
elif owo2 == 7:
    Karta4p.insert(2, "7")
elif owo2 == 8:
    Karta4p.insert(2, "8")
elif owo2 == 9:
    Karta4p.insert(2, "9")
elif owo2 == 10:
    Karta4p.insert(2, "10")
elif owo2 == 11:
    Karta4p.insert(2, "Walet")
elif owo2 == 12:
    Karta4p.insert(2, "Krolowa")
elif owo2 == 13:
    Karta4p.insert(2, "Krol")










# wybieranie piatej karty z wylosowanych numerow
owo6 = random.randrange(1 , 5)
owo2 = random.randrange(1 , 13)
if owo6 == 1:
    Karta5p.insert(1, "Pik")
elif owo6 == 2:
    Karta5p.insert(1, "Kier")
elif owo6 == 3:
    Karta5p.insert(1, "Trefl")
elif owo6 == 4:
    Karta5p.insert(1, "Karo")
if owo2 == 1:
    Karta5p.insert(2, "AS")
elif owo2 == 2:
    Karta5p.insert(2, "2")
elif owo2 == 3:
    Karta5p.insert(2, "3")
elif owo2 == 4:
    Karta5p.insert(2, "4")
elif owo2 == 5:
    Karta5p.insert(2, "5")
elif owo2 == 6:
    Karta5p.insert(2, "6")
elif owo2 == 7:
    Karta5p.insert(2, "7")
elif owo2 == 8:
    Karta5p.insert(2, "8")
elif owo2 == 9:
    Karta5p.insert(2, "9")
elif owo2 == 10:
    Karta5p.insert(2, "10")
elif owo2 == 11:
    Karta5p.insert(2, "Walet")
elif owo2 == 12:
    Karta5p.insert(2, "Krolowa")
elif owo2 == 13:
    Karta5p.insert(2, "Krol")




all = Karta1 + Karta2 + Karta3 + Karta4 + Karta5

zmiana = random.randrange(1 , 3)
if zmiana == 1:
    print("przeciwnik zmienia karte (tak na serio nic nie zmienia)")

# kastracja i przeszczep
Karta1.pop(1)
Karta2.pop(1)
Karta3.pop(1)
Karta4.pop(1)
Karta5.pop(1)
print(Karta1)

print("Pokazywanie kart")
print("Uklad")

if Karta1 or Karta2 or Karta3 or Karta4 or Karta5 ==



print()