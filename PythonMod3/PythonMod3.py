

#Zad 0
'''- Lista
Uporządkowana kolekcja elementów, które mogą być zmieniane, zduplikowane.
lista = ['jeden', 'dwa']'''
imiona = []
imiona = ['Jan','Zdzichu','Kleofas']
print (imiona)
#dodawanie na koniec
imiona.append('Genowefa')
imiona.append('Bonifacy')
imiona.append('Jan')
print (imiona)
#prosta pętla, odwrócenie, sortowanie
for imie in imiona:
    print(imie)
imiona.reverse()
print(imiona)
imiona.sort() 
print(imiona)
#wywołanie po indexie
print(imiona[0],imiona[1])
#długość listy, zliczanie elementow
print(len(imiona))
ile_Jan = imiona.count('Jan')
print(ile_Jan)
#pobranie elementu(element zabrany z listy)
print(imiona)
imie = imiona.pop(0)
print(imie)
print(imiona)

#wstawianie
imiona.insert(0,'Eustachy')
print(imiona)
imiona.insert(3,'Eustachy')
print(imiona)

#usuwanie(nie pobiera elementu), usuwany jest pierwszy wystepujacy elemento o tej nazwie
imiona.remove('Eustachy')
print(imiona)
#wyczyszczenie listy
imiona.clear()
print(imiona)

#łączenie list
list1 = ['one', 'two']
list2 = ['three', 'four']
listA = list1 + list2
print(listA)
listA.sort(reverse=True)
print(listA)

#zwracanie indexu wpisanego elementu
print(listA.index('two'))

#wypełnienie listy elementami podniesionymi do potegi 2
potegi = [x**2 for x in range(10)]
print(potegi)

# iterowanie kilku list:
for x1,x2 in zip(list1,list2):
    print(f"{x1} - {x2}")

#wydruk niepełnej listy
lista = [1,2,3,4,5,6,7]
print(lista[2:4])
print(lista[3:]) #od indekxu 3
print(lista[:3]) #od indeksu 0
print(lista[::2]) #co drugi element
print(lista[::-1]) #odwrócona kolejność
del lista[4:]
print(lista)

#transpozycja macierzy
macierz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(macierz)
transponowana = [ [wiersz[i] for wiersz in macierz] for i in range(len(macierz[0])) ]
print(transponowana)

#poniżej lista w liście czyli taka tablica 2D
lista2D = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lista1 in lista2D:
    for x in lista1:
        print(x,end='')
    print()

#kolejne przybliżenia stalej pi
from math import pi
przyblizenia_pi = [str(round(pi,i)) for i in range(10)]
print(przyblizenia_pi)

#rozbicie łańcucha znaków
napis = "ala ma kota"
lista = list(napis)
print(lista)

#utworzenie listy
list0 = list(range(1,10))

#modyfikacja
list0[0:3] = [10]
print(list0)

#ucinanie listy
list0[0:3] = []
print(list0)

#wlasciwosci i zachowanie listy
l5 = list(range(1,10))
print(l5)
x = l5
l5[3:5] = [10]
print(l5)
l5=x
l5[3:4] = [10,11,12]
print(l5)
l5=x
l5[3:12] = [10,11]
print(l5)
l5=x
l5[3:8] = [10,11]
print(l5)
l5[3:5] = "ala ma kota"
print(l5)


#zad 0a
'''- Krotka
Uporządkowana kolekcja elementów, które nie mogą być zmieniane, ale mogą występować duplikaty.
krotka = ('jeden', 'dwa')'''

krotka = (1,2,3,4,5,6,7,8,9,2,11,12)
names = ('Lucjan','Magda','Ildefons','Janusz','Lucjan')
print(names)
rozmiar = len(names)
print(rozmiar)
print(names.count('Lucjan'))
print(names.index('Ildefons'))
#warianty szukania - po danym indexie i w danym przedziale
print(krotka.index(2,4))
print(krotka.index(2,0,10))

krotka_list = ([1,2,3],['a','b','c'],['Ala','Janusz','Tomasz'])
print(krotka_list)
krotka_list[0][1] = 99 #samej krotki nie można modyfikować ale jeśli jej elementem jest np lista to tą listę już mozna
print(krotka_list)


#zad 0b
'''- Zbiór
Nieuporządkowany zestaw danych, nie może zawierać duplikatów. Inna nazwa to tablica haszująca czyli automat sprawdzający czy dana wartość już istnieje w zbiorze.
zbior = {'jeden', 'dwa'}
x = set() - utworzenie pustego zbioru
wybrane operacje na zbiorach: len(), add(), remove(), copy(), clear()
zb = {} uwaga to tworzy słownik nie zbiór!'''

zbior = {'Adam','Tomasz','Kamil','Ala','Janusz','Adam'} #nie ma duplikatów!
print(zbior) #nie wiemy w jakiej kolejności będa przechowywane, elemnty nie są mutowalne czyli łączone

# pusty zbiór:
dane = set()
dane.add('Agata')
dane.add('Zenon')
dane.add('Kamil')
print(dane)

dane.remove('Zenon') #rzuca bład KeyError gdy nie ma elementu
print(dane)
dane.discard('Kamil') #dane.remove('Kamil') - to błąd
print(dane)

multiset = set()
multiset.add('Janek')
multiset.add('Tomek')
lista = ['Kamil','Anna'] #multiset.add(lista) #tego dodać nie można
krotka = ('Marzena','Halina')
multiset.add(krotka)
print(multiset) #za kazdym razem inna kolejność wyświetlania!
#print(multiset[0]) #błąd bo elementy nie są uporządkowane

print("multiset:")
for element in multiset:
    print(element)

s1 = {1,2,3,4}
s2 = {100,200,300,2}
#s3 = s1 + s2 #błąd
print('union')
s3 = s1.union(s2)
print(s3) 
#modyfikacja zbioru do s1 dodaje elementy z s2
print('update')
s1.update(s2)
print(s1)

print("multiset:")
#kolejne elemnty
for element in s3:
    print(element)
    
#porównywanie zbiorów
print('s4')
s4 = s1.difference(s2) #z s1 usunięte sa elementy istniejące w s2
print(s4)

#przecięcie
print('przeciecie')
print('s1:',s1)
print('s2:',s2)
s5 = s1.intersection(s2) #część wspólna
print(s5)

#elementy rózne
s6 = s1.symmetric_difference(s2)
print('symm_dif:',s6)

s6.clear()
print('clear',s6)

# zbiór do listy
lista = [1,2,3]
zb = {10,20,30}
lista.append(zb)
print('lista:',lista) #pojawi sie czwarty element listy
print(lista[3])

#zbior do listy ale jego poszczedgólne elememnty
lista = [1,2,3]
zb = {10,20,30}
lista.extend(zb)
print('lista:',lista) #pojawi sie czwarty element listy
print(lista[3])


#zad 0c

numbers = [1,2,3,4,5,6,7,8,9,10]
num = numbers[:]
print(num)
num1 = numbers[2:6]
print(num1)
num2 = numbers[::2]
print(num2)
num3 = numbers[-1]
print(num3)

slowo = 'PYTHON'
wyrazy =[]
for i in slowo:
    wyrazy.append(i)
print(wyrazy)

napis = ''
znaki = ['P','a','c','a','n','ó','w']
for z in znaki:
    napis += z
print(napis)

lista2D = []
print(lista2D)
for e in numbers: #dla każdego elementu z listy, lista bez znaczenia jaką on ma wartość
    lista2D.append(numbers)
print(lista2D)

print (lista2D[1])

print (lista2D[3][2])


#zad1
from random import randint

n = int(input('Podaj liczbe elementow: '))
_list = [randint(0,100) for _ in range(n)]
print(_list)
m = int(input('Podaj liczbe elemetnow do dodania: '))
for i in range(m):
    _list.append(int(input(f'Podaj element nr {i+1}: ')))
print(_list)
x = int(input('Liczba elementow do dodania na koncu listy: '))
for i in range(x):
    _list.append(randint(0,100))
print(_list)
index = int(input('Podaj indeks: '))
if(index >= 0 and index < len(_list)):
    _list[index] = randint(0,100)
    print(f'Dodano element {_list[index]}')
    print(_list)
else:
    print('Nieprawidowy indeks')
lastItem = _list.pop(int(input(f'Podaj nr indexu: ')))
print('Usunieto element', lastItem, 'Lista po usunieciu: ', _list)
index = int(input('Podaj nr indexu: '))
del _list[index]
print('Usunieto element o indexie ', index, _list)
x = int(input('Podaj element do zliczenia: '))
count = _list.count(x)
print(f'Element {x} wystepuje {count} razy')
_list.sort()
print(_list)
m = int(input('Podaj m: '))
n = int(input('Podaj n: '))
if(m >= 0 and m <= n and m < len(_list) and n < len(_list)):
    while(m<=n):
        print(_list[m], end='')
        if(m != n):
            print(', ', end='')
        m = m+1
print()

#zad2

from random import randint

lista = [["#"] * 5] * 7
print(f"Ilosc wierszy: {len(lista)}")
print(f"Ilosc kolumn: {len(lista[0])}")
for i in range(7):
    for j in range(5):
        print(lista[i][j], end='')
    print()

print('Inne rozwiązanie: ')
    
size = randint(1,15)
_list = [[randint(0,9) for x in range(size)] for x in range(size)]
rows = len(_list)
cols = len(_list[0])
for i in range(len(_list)):
    for j in range(len(_list[i])):
        print(_list[i][j],end='')
    print()
print('Ilosc wierszy:', rows, 'Ilosc kolumn:', cols)

#zad3

lista = [47,57,65,84,3,4,9,3,1,48,57,16,23,59,34,18,67,25]
dlugosc = len(lista)
for i in range(dlugosc):
    for j in range(0, dlugosc - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
for i in range(dlugosc):
    print(lista[i])


#zad4

lista = []
dlugosc = int(input("Podaj ilosc elementow: "))
for i in range(dlugosc):
    lista.append(int(input("Podaj liczbe do wstawienia: ")))
for i in range(dlugosc):
    for j in range(0, dlugosc - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
for i in range(dlugosc):
    print(lista[i])


#zad5

lista = [47,57,65,84,3,4,9,3,1,48,57,16,23,59,34,18,67,25]
najmniejsza = lista[0]
najwieksza = lista[0]
for i in range(1, len(lista)):
    if(lista[i] < najmniejsza):
        najmniejsza = lista[i]
    if(lista[i] > najwieksza):
        najwieksza = lista[i]
print(f"Najmniejsza liczba: {najmniejsza}")
print(f"Najwieksza liczba: {najwieksza}")

#zad6

tekst = 'Napisac program analizujacy statystyke liter w podanym tekscie.'
myDict = dict()
for x in tekst:
    if x in myDict:
        myDict[x] += 1
    elif x >= 'a' and x <= 'z' or x>= 'A' and x<= 'Z':
        myDict[x] = 1

for item in myDict:
    print(f'{item}: {myDict[item]}')


#zad7

stanowiska = ['wozny', 'podawacz recznikow', 'podawacz wody', 'programista']
osoby = [('Jarek', 'Jarecki'), ('Stefan', 'Stefanski'), ('Marek', 'Marecki'), ('Igor', 'Igorski')]
myDict = dict()
for i in range(len(stanowiska)):
    myDict[stanowiska[i]] = osoby[i]

print(myDict)

print()

#zad 15
import turtle

scale = 2.0
fontSize = 15
dotSize = 5*scale
distanceFromDot = 10*scale
titleStyle = ('Arial', int(fontSize*scale), 'italic')
starsStyle = ('Arial', int(fontSize*0.5*scale))
screenW = 1024
screenH = 800

colors = {
'stars':'yellow',
'names':'yellow',
'title':'yellow'
}

startX = screenW/2
startY = screenH/2

stars = {
'Alnitak':(-20,-15),
'Alnilam':(0,-8),
'Mintaka':(21,2),
'T Ori':(57,-100),
'Rigel':(65,-120),
'Saiph':(-70,-110),
'Betelgeza':(-35,115),
'Meissa':(38,140),
'Bellatrix':(67,85)
}

connections = ['Alnitak', 'Alnilam', 'Mintaka', 'T Ori',
'Rigel', 'Saiph', 'Alnitak', 'Betelgeza', 'Meissa', 'Bellatrix', 'Mintaka']

t = turtle.Turtle()
t.speed(0)
s = turtle.Screen()
s.setup(screenW, screenH)
s.bgcolor('blue')

t.hideturtle()
t.penup()
t.pencolor(colors['title'])
t.goto(-screenW/2+(10*scale), screenH/2-(fontSize*2*scale))
t.write('Gwiazdozbior ORIONA', font=titleStyle, align='left')

for s in stars:
    t.goto(stars[s][0]*scale,stars[s][1]*scale)
    t.pencolor(colors['stars'])
    t.dot(dotSize)
    t.forward(distanceFromDot)
    t.pencolor(colors['names'])
    t.write(s, font=starsStyle, align='left')

t.pencolor(colors['stars'])
for c in connections:
    t.goto(stars[c][0]*scale, stars[c][1]*scale)
    t.pendown()
input()

#zad 10

def policz(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    elif type(a) is str and type(b) is int:
        return a*b
    elif type(a) is float and type(b) is float:
        return a+b
    else:
        return None

print(policz(1,2))
print(policz("tekst",3))
print(policz(2.4,3.12))
print(policz(1,1.0))