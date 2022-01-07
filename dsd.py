import random

owo6 = random.randrange(1, 5)
owo2 = random.randrange(1, 13)
Karta4p = []
Karta5p = []

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


a = owos(Karta4p, owo6, owo2)
print(Karta4p)
owo61 = random.randrange(1, 5)
owo21 = random.randrange(1, 13)
a = owos(Karta5p, owo61, owo21)
print(Karta5p)