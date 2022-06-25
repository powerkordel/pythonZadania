
import time
import math
import turtle
import random
import statistics



#zad 0
try:
    liczba = int(input("Podaj liczbe: "))
    if (liczba > 0):
        print("Tak")
except:
    print("To nie byla liczba!")
else:
    if(liczba >= 0):
        print("WiekszaRówna")
finally:
    print("Koniec programu.")
    
    
#zad 1
STO = 100
try:
    wiek = int(input("Podaj wiek: "))
except:
    print("Podano bledne dane!")
else:
    print(f"Do stu lat brakuje Ci {STO-wiek} lat.")
    if(wiek < 18):
        print("MLODOCIANY")
    else:
        print("PELNOLETNI")
        
        
#zad 2
imie = input("Podaj imie:")
wiek = int(input("Podaj wiek:"))
plec = input("Podaj plec (kobieta/mezczyzna):")
EMERYTURA_MEZCZYZNA = 65
EMERYTURA_KOBIETA = 60
if(plec == "kobieta"):
    if(wiek >= EMERYTURA_KOBIETA):
       print("EMERYTURA")
    else:
       print("PRACA")
else:
    if(wiek >= EMERYTURA_MEZCZYZNA):
       print("EMERYTURA")
    else:
       print("PRACA")
print("\n\n")


#zad3
for i in range(100):
    print(f"{i + 1},", end = ' ')
print("\n\n")
for i in range(100, 121, 2):
    print(f"{i},",  end = ' ')
print("\n\n")
for i in range(200, 301):
    if(i%3 == 0):
        print(f"{i},", end = ' ')
print("\n\n")
for i in [1,4,6,2,8,9,3,5,5]:
    print(f"{i},", end = ' ')
print("\n\n")
for i in range(20, -1, -1):
    print(f"{i},", end = ' ')
print("\n")
print("lub:\n")
lista = [x for x in range(0,21)]
lista.reverse()
for x in lista:
    print(x,end=',')
print("\n\n")


#zad 4
liczba = 10
while(liczba >= 0):
    if(liczba == 7):
        liczba-=1
        continue
    print(liczba)
    if(liczba > 7):
        print("Koniec ciala petli!")
        liczba-=1
        continue
    if(liczba == 3):
        break
    liczba-=1
print("Petla zakonczona")
print("\n\n")


#zad 5
lista = []
x = -1
ilosc=0
while x != 0:
    try:
        x = int(input("Podaj liczbe: "))
    except:
        print("Podano bledne dane!")
        x = 0
    else:
        if x != 0:
            lista.append(x)
            ilosc+=1
print(f"Ilosc wprowadzonych liczb: {ilosc}")
suma = sum(lista)
print('SUMA:', suma)
print('MAX:',max(lista))
print('MIN',min(lista))
srednia = suma / len(lista)
print('SREDNIA: {0}'.format('%5.5f'.zfill(10) % srednia))

#zad 6
for i in range(18):
    for j in range(i + 1):
        print("*", end = '')
    print('')
print("\n\n")


#zad 7
try:
    poziomy = int(input("Podaj liczbe poziomow: "))
except:
    print("Podano bledne dane!")
else:
    szerokosc = poziomy//5
    wysokosc = poziomy//3
    srodek = poziomy*2//2
    for i in range(0,poziomy):
        for j in range(0,poziomy*2):
            if (j >= srodek-i) and (j <= srodek+i):
                znak = '*'
            else:
                znak = ' '
            print(znak,end='')
        print()
    for i in range(0, wysokosc):
        for j in range(0,poziomy*2):
            if j >= srodek - szerokosc//2 and j <= srodek + szerokosc//2:
                znak = '*'
            else:
                znak = ' '
            print(znak,end='')
        print()


#zad 8
try:
    liczba = int(input('Podaj liczbe: '))
except:
    print('Podano bledne dane!')
else:
    binarnie = []
    while(liczba != 0):
        binarnie.append(liczba % 2)
        liczba = liczba >> 1
    binarnie.reverse()
    for bit in binarnie:
        print(bit,end='')
    print('')


#zad 9

while True:
    liczby = input('Podaj 3 liczby oddzielone spacją:')
    liczby = liczby.split()
    liczba = []
    for n in liczby:
       liczba.append(int(n))
    print(min(liczba))
    i = input("Kontynuowac?[T/N] ")
    if(i.upper() == 'N'):
        break;


#zad 10
waga = float(input("Podaj wage w kg: "))
wzrost = float(input("Podaj wzrost w cm: "))

bmi = waga / (wzrost/100)**2
if(bmi < 16):
   print("Wyglodzenie")
elif(bmi >= 16 and bmi < 17):
        print("Wychudzenie")
elif(bmi >= 17 and bmi < 18.50):
        print("Niedowaga")
elif(bmi >= 18.5 and bmi < 25):
        print("Wartosc prawidlowa")
elif(bmi >= 25 and bmi < 30):
        print("Nadwaga")
elif(bmi >= 30 and bmi < 35):
        print("I stopien otylosci")
elif(bmi >= 35 and bmi < 40):
        print("II stopien otylosci")
else:
        print("Otylosc skrajna")


#zad 11
for i in range(10):
    for j in range(10):
        print("0", end = '')
    print()
print()
char = input("Podaj znak:")
print()
for i in range(10):
    for j in range(10):
        if(i == j):
            print(char, end = '')
        else:
            print("0", end = '')
    print()
print()
for i in range(10):
    for j in range(10):
        if(j == 9 - i):
            print(char, end = '')
        else:
            print("0", end = '')
    print()


#zad 12
decymalna = int(input("Podaj liczbe dziesietna: "))
binarna = []
temp = decymalna
while(temp != 0):
   binarna.append(temp % 2)
   temp = temp >> 1
binarna.reverse()
print(f"Liczba {decymalna} to binarnie: ",end='')
for i in binarna:
   print(i,end='')
print()


#zad 13
binarna = input("Podaj liczbe binarna: ")
wykladnik = 0
liczba = 0
temp = binarna[::-1]
for c in temp:
   liczba += int(c) * 2**wykladnik
   wykladnik += 1
print(f"Liczba {binarna} dziesietnie to: {liczba}")


#zad 14
pierwszaLiczba = int(input("Podaj liczbe1:"))
drugaLiczba = int(input("Podaj liczbe2:"))
for i in range(pierwszaLiczba, drugaLiczba + 1):
    if(i%2 == 0 and i%7 == 0):
        print(f"{i} DWA_SIEDEM")
    elif(i%2 == 0):
        print(f"{i} DWA")
    elif(i%7 == 0):
        print(f"{i} SIEDEM")
    else:
        print(i)


#zad 15
import random
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
liczba = random.randint(a,b)
podejscia = 0
while True:
   strzal = int(input("Podaj liczbe: "))
   podejscia += 1
   if strzal < liczba:
      print("Za malo")
   elif strzal > liczba:
      print("Za duzo")
   else:
      print(f"Brawo! Potrzebowales {podejscia} prob.")
      break


  #zad 16
import random
import time

moneta = ['o','r']
gracz = 0
komputer = 0
while True:
    wybor = input("r czy o? [q - koniec]: ")
    if wybor == 'q':
        break;
    rand = random.randint(0,1)
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    wynik = moneta[rand]
    print(f"Wypadlo: {wynik}")
    if wybor == wynik:
        gracz += 1
    else:
        komputer += 1
    print(f"Gracz: {gracz}, Komputer: {komputer}")



#zad 17
import random
try:
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
except:
    print("Podano bledne dane!")
else:
    pierwsza = True
    liczba = random.randint(a,b)
    print(liczba)
    if(liczba > 1):
        for i in range(2, int(liczba/2)+1):
            if(liczba % i == 0):
                print("Nie liczba pierwsza")
                pierwsza = False
                break
        if(pierwsza):
            print("Liczba pierwsza")
    else:
        print("Nie liczba pierwsza")


#zad 18
import random
from statistics import median

iloscRzutow = int(input("Podaj ilosc rzutow kostka:"))
iloscJedynek = 0
iloscDwojek = 0
iloscTrojek = 0
iloscCzworek = 0
iloscPiatek = 0
iloscSzostek = 0
listaLiczb = []
for i in range(iloscRzutow):
    losowa = random.randint(1, 6)
    listaLiczb.append(losowa)
    print(f"Rzut nr: {i+1} Wyrzucono: {losowa}")
    if(losowa == 1):
        iloscJedynek += 1
    elif(losowa == 2):
        iloscDwojek += 1
    elif(losowa == 3):
        iloscTrojek += 1
    elif(losowa == 4):
        iloscCzworek += 1
    elif(losowa == 5):
        iloscPiatek += 1
    else:
        iloscSzostek += 1
print("Statystyka rzutow:")
print(f"Oczek: 1 ilosc: {iloscJedynek}")
print(f"Oczek: 2 ilosc: {iloscDwojek}")
print(f"Oczek: 3 ilosc: {iloscTrojek}")
print(f"Oczek: 4 ilosc: {iloscCzworek}")
print(f"Oczek: 5 ilosc: {iloscPiatek}")
print(f"Oczek: 6 ilosc: {iloscSzostek}")
listaLiczb.sort()
print(f"Mediana: {median(listaLiczb)}")


#zad 18
try:
    liczba = int(input("Podaj liczbe rzutow: "))
except:
    print("Podano bledne dane!")
else:
    licznik = 1
    statystyka = [0 for i in range(6)]
    lista = []
    while licznik <= liczba:
        wynik = random.randint(1,6)
        lista.append(wynik)
        statystyka[wynik-1] += 1
        print("Rzut nr: {0:3} Wyrzucono: {1:2}".format(licznik, wynik))
        licznik += 1

    print("\nStatystyka rzutow:")
    for c, v in enumerate(statystyka):
        print("Oczek: {0:4} ilosc: {1:4}".format(c+1,v))

    lista.sort()
    print(f"Mediana: {statistics.median(lista)}")


    #zad 19
turtle.penup()
colors = ['green yellow', 'chocolate', 'yellow', 'magenta']
turtle.setpos(-50,50)
turtle.pendown()
for color in colors:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)
time.sleep(2)
turtle.clearscreen()
for i in range(8):
    turtle.forward(30)
    turtle.right(360/8)
turtle.done()
    


from turtle import  *

#zad 20
promien = int(input("Podaj promien: "))
color('black')
goto(100,0)
right(180)
goto(-100,0)
up()
goto(0,0)
down()
right(90)
goto(0, 100)
right(180)
goto(0, -100)
up()
goto(-promien,0)
down()
circle(promien)
done()


#zad 21
from turtle import  *
promien = int(input("Podaj promien: "))
ilosc = int(input("Podaj ilosc okregow (5/10/20/40): "))
color('black')
for i in range(ilosc):
    circle(promien)
    right(360/ilosc)
hideturtle()
done()





#zad 22
n = int(input("Podaj ilosc okregow: "))
m = int(input("Podaj odstep: "))
color('black')
goto(200,0)
right(180)
goto(-200,0)
up()
goto(0,0)
down()
right(90)
goto(0, 200)
right(180)
goto(0, -200)
up()
goto(0, -20)
left(90)
down()
r = 20
for i in range(n):
    circle(r)
    up()
    goto(0, -20 -(m * (i + 1)))
    down()
    r += m
hideturtle()
done()



#zad 23
n = int(input("Podaj ilosc okregow: "))
m = int(input("Podaj roznice promieni: "))
color('black')
goto(200,0)
right(180)
goto(-200,0)
up()
goto(0,0)
down()
right(90)
goto(0, 200)
right(180)
goto(0, -200)
up()
goto(0, -20)
left(90)
down()
r = 20
for i in range(n):
    circle(r)
    r += m
done()


#zad 24

ilosc = int(input("Podaj ilosc choragiewek: "))
color('black')
for i in range(ilosc):
    forward(200)
    for j in range(3):
        left(90)
        forward(30)
    left(90)
    goto(0,0)
    right(360/ilosc)
hideturtle()
done()



#zad 25
try:
    n = int(input("Podaj liczbe bokow: "))
    l = int(input("Podaj dlugosc bokow: "))
except:
    print("Podano bledne dane!")
else:
    angle = 360/n
    for i in range(n):
        turtle.forward(l)
        turtle.right(angle)
hideturtle()
done()







