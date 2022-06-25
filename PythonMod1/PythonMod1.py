from datetime import date, timedelta
import datetime
from turtle import *
import math
import random
 




#Zadanie1

print ("Nauka w Python")

print ("Nauka w PythonA \nNauka w PythonB")

print ("""Nauka w Python1
Nauka w Python2""")


#Zadanie2
x = 20
y = 30

suma = x+y
roznica = x-y
iloczyn = x*y
iloraz = x/y

print (f"Suma to: {suma}")
print (f"Roznica to: {roznica}")
print (f"Iloczyn to: {iloczyn}")
print (f"Iloraz to: {iloraz}")

#Zadanie 3

z = 8

print (z)
print (bin(z))
print (hex(z))
print (oct(z))

#Zadanie 4

q = 7
print (q)
#w = 7L - nie dziala
q = .7
print (q)
q = 7.
print (q)
q = 7,
print (q)
q = 7.0
print (q)
q = 7e-1
print (q)
q = 7e+1
print (q)
q = [3.0,5.12,70e-1][-1]
print (q)
q = int('732')
print (q)
q = int('7')
print (q)
q = {3:[2,5],'a':[5,12],0:[1,7,6]}[0][1:2:1]
print (q)
q= (2+7j).imag
print (q)
#q = 07 - nie dziela
q= 0xA
print (q)
q= 1<<2+3
print (q)
q= (1<<2)+3
print (q)
q= (1<<2)+(1<<1)+1
print (q)
q= 15&7
print (q)
q = 22//3
print (q)
q = 21%14
print (q)

#Zadanie5

w = 5E-1
print (w)
w = (3==3)/2
print (w)
w = (3==3)/2.0
print (w)
w = 1/2
print (w)
w = float(1)/2
print (w)
w = 5.
print (w)
#w = 0.5L - nie dziala
w = 5*((2>3)<2)
print (w)
#w = 1.0>>2 - nie dziala
#w = 1/(('a'== "A"|2<3)+1) - nie dziala (trzeba domknac nawiasy miedzy |)

#Zadanie6
aa = 3
print(aa<<1)
print(aa<<2)
print(aa>>2)
print(aa<<2>>1)
print(aa<<3)   #i przesuniecie bitowe - przyklady

x = 5 * 2.0 
print(x)

x = 3
x=3.5
x="ala ma kota"
x=x+1   # can only concatenate str (not "int") to str


#Zadanie6A


print ("Podaj imie")
imie = input()
print ("Podaj wiek")
wiek = int(input())
STO = 100 - wiek
print (f"Witaj {imie}. Lata pozostale do setki: {STO} :)")


#Zadanie 7
print ("Podaj predkosc w kilometrach")
speedKM = int(input())
speedMI = (speedKM * 0.621)
print (f"Predkosc {speedKM} km to w milach: {speedMI}")


#Zadanie 8

print ("Podaj temperature w stopniach Celcjusza")
Celsius = float(input())
Fahrenheit = float(Celsius * (9/5) + 32)
print (f"{Celsius} C to:  {Fahrenheit} F")

#Zadanie 9

odleglosc = float(input("Podaj przebyta odleglosc: "))
paliwo = float(input("Podaj ilosc spalonego paliwa: "))
print (f"Na setke srednio zostalo spalone {paliwo/odleglosc*100} L.")

#Zadanie 10

dob = int(input("Podaj rok urodzenia: "))
dzis = date.today()
wiek = dzis.year - dob 
print (f"Twoj wiek to: {wiek}")

#Zadanie 11

print (f"Dzis jest {dzis}")
okres = int(input("Podaj liczbe dni: "))
print (f"Za {okres} dzien/dni bedzie {dzis + timedelta(okres)}")

#Zadanie 12

print("""Podaj date w formacie: rok,miesiac,dzien 
Po wprowadzeniu wartosci wcisnij enter.""")
data2 = date(int(input()),int(input()),int(input()))
print(data2)
rok1 = int(input("Podaj rok:"))
miesiac1 = int(input("Podaj liczbe miesiaca:"))
dzien1 = int(input("Podaj liczbe dnia:"))
data1 = date(rok1,miesiac1,dzien1)
print(data1)
roznicaDni = data2 - data1
print ("Roznica dni miedzy datami: ", data2, ", a ", data1, "wynosi: ", roznicaDni.days)

#Zadanie 13

liczba1 = 3.144
print('Usuniecie czesci po przecinku: ' + str(math.trunc(liczba1)))
print('Wartosc górna: ' + str(math.ceil(liczba1)))
print('Wartosc dolna: ' + str(math.floor(liczba1)))

liczba2= 0.12367890123456789
print('Wartosc zaokrąglona do 2 miejsc po przecinku to %.2f' %liczba2)
print('Wartosc zaokrąglona do 3 miejsc po przecinku to %.3f' %liczba2)
print('Wartosc zaokrąglona do 4 miejsc po przecinku to %.4f' %liczba2)
print('Wartosc zaokrąglona do 5 miejsc po przecinku to {0:0.5f}'.format(liczba2))
print('Wartości do 7 miejsc po przecinku ' + str(round(liczba2, 7)))

liczba3 = 3.144
print(f"Zaokraglona w dol: {liczba3.__floor__()}")
print(f"Zaokraglona w gore: {liczba3.__ceil__()}")
print('Wartosc w srodku ciagu znakowego {0}, ktora jest sformatowana z zerami wiadacymi.'.format('%5.3f'.zfill(10) % liczba3))
print('Wartosc w srodku ciagu znakowego {0}, ktora jest sformatowana do lewej.'.format('%5.3f'.ljust(10) % liczba3))
print('Wartosc w srodku ciagu znakowego {0}, ktora jest sformatowana do prawej'.format('%5.3f'.rjust(10) % liczba3))


#Zadanie 14

color('black')
for i in range(6):
    dot(10)
    forward(50)
left(180)
forward(350)
for i in range(4):
    dot(10)
    forward(50)
left(180)
forward(250)
right(90)
forward(50)
for i in range(4):
    dot(10)
    forward(50)
left(180)
forward(300)
for i in range(5):
    dot(10)
    forward(50)
left(180)
forward(150)
left(90)
up()
goto(50, 150)
down()
for i in range(4):
    forward(50)
    right(90)
up()
goto(-150, -50)
down()
for i in range(360):
    forward(1)
    right(1)
done()











